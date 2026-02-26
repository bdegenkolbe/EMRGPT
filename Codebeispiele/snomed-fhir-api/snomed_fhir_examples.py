"""
SNOMED CT FHIR-API Beispiele für UKLGPT
========================================
Nutzt die Snowstorm FHIR R4-API für:
- Konzept-Lookup ($lookup)
- Hierarchische Suche mit ECL ($expand)
- Terminologie-Mapping SNOMED→ICD-10 ($translate)
- Hierarchie-Prüfung ($subsumes)

Referenz: https://github.com/IHTSDO/snowstorm/blob/master/docs/using-the-fhir-api.md
Lizenz:   Apache 2.0 (IHTSDO/SNOMED-in-5-minutes)

Phase 1: Öffentlicher IHTSDO-Server (nicht für Produktion)
Phase 2: On-Premise Snowstorm (http://snowstorm.ukl.internal:8080/fhir)
"""

import json
import urllib.request
import urllib.parse

# --- Konfiguration ---
# Phase 1: Öffentlicher Server
FHIR_BASE = "https://snowstorm.ihtsdotools.org/fhir"
# Phase 2 (On-Premise):
# FHIR_BASE = "http://snowstorm.ukl.internal:8080/fhir"

SNOMED_SYSTEM = "http://snomed.info/sct"


def fhir_get(url: str) -> dict:
    """HTTP GET mit JSON-Parsing."""
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/fhir+json")
    req.add_header("User-Agent", "UKLGPT-Prototype/1.0 (kontakt@ukl.de)")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ============================================================
# 1. $lookup – Konzept-Details abrufen
# ============================================================
def concept_lookup(sctid: str) -> dict:
    """
    Ruft Bezeichnung, Definitionen und Eigenschaften eines
    SNOMED-CT-Konzepts ab.

    Beispiel: concept_lookup("84114007")  → Herzinsuffizienz
    """
    url = (
        f"{FHIR_BASE}/CodeSystem/$lookup"
        f"?system={urllib.parse.quote(SNOMED_SYSTEM)}"
        f"&code={sctid}"
    )
    data = fhir_get(url)

    result = {"sctid": sctid}
    for param in data.get("parameter", []):
        name = param.get("name")
        if name == "display":
            result["display"] = param.get("valueString")
        elif name == "designation":
            # Synonyme sammeln
            desig = {}
            for part in param.get("part", []):
                desig[part["name"]] = part.get("valueString") or part.get("valueCoding", {}).get("code")
            result.setdefault("synonyms", []).append(desig)
    return result


# ============================================================
# 2. $expand – Hierarchische Suche mit ECL
# ============================================================
def expand_ecl(ecl: str, filter_text: str = "", count: int = 20) -> list:
    """
    Sucht SNOMED-Konzepte mittels Expression Constraint Language (ECL).

    Beispiele:
        expand_ecl("< 84114007")          → Alle Untertypen von Herzinsuffizienz
        expand_ecl("< 71388002", "append") → Prozeduren die 'append' enthalten
        expand_ecl("<< 404684003")         → Klinische Befunde (inkl. Self)
    """
    url = (
        f"{FHIR_BASE}/ValueSet/$expand"
        f"?url={urllib.parse.quote(SNOMED_SYSTEM + '?fhir_vs=ecl/' + ecl)}"
        f"&count={count}"
        f"&includeDesignations=true"
    )
    if filter_text:
        url += f"&filter={urllib.parse.quote(filter_text)}"

    data = fhir_get(url)
    concepts = []
    for entry in data.get("expansion", {}).get("contains", []):
        concepts.append({
            "sctid": entry.get("code"),
            "display": entry.get("display"),
            "system": entry.get("system"),
        })
    return concepts


# ============================================================
# 3. $translate – SNOMED CT → ICD-10 Mapping
# ============================================================
def translate_to_icd10(sctid: str) -> list:
    """
    Übersetzt ein SNOMED-CT-Konzept in ICD-10-Codes.

    Beispiel: translate_to_icd10("84114007")
    → [{"icd10": "I50.9", "equivalence": "equivalent"}]
    """
    url = (
        f"{FHIR_BASE}/ConceptMap/$translate"
        f"?system={urllib.parse.quote(SNOMED_SYSTEM)}"
        f"&code={sctid}"
        f"&targetsystem={urllib.parse.quote('http://hl7.org/fhir/sid/icd-10')}"
    )
    data = fhir_get(url)
    mappings = []
    for group in data.get("group", []):
        for element in group.get("element", []):
            for target in element.get("target", []):
                mappings.append({
                    "icd10": target.get("code"),
                    "display": target.get("display"),
                    "equivalence": target.get("equivalence"),
                })
    return mappings


# ============================================================
# 4. $subsumes – Hierarchie-Prüfung
# ============================================================
def check_subsumes(parent_sctid: str, child_sctid: str) -> str:
    """
    Prüft ob Konzept A ein Übertyp von Konzept B ist.

    Beispiel: check_subsumes("84114007", "441530006")
    → "subsumes" (Herzinsuffizienz subsumiert Chronische Herzinsuffizienz)
    """
    url = (
        f"{FHIR_BASE}/CodeSystem/$subsumes"
        f"?system={urllib.parse.quote(SNOMED_SYSTEM)}"
        f"&codeA={parent_sctid}"
        f"&codeB={child_sctid}"
    )
    data = fhir_get(url)
    for param in data.get("parameter", []):
        if param.get("name") == "outcome":
            return param.get("valueCode")
    return "unknown"


# ============================================================
# 5. UKLGPT-spezifisch: Diagnose-Terme für Europe PMC extrahieren
# ============================================================
def get_search_terms_for_diagnosis(sctid: str) -> list:
    """
    Extrahiert alle Synonyme eines SNOMED-Konzepts zur Verwendung
    als Suchterme in Europe PMC.

    Beispiel: get_search_terms_for_diagnosis("84114007")
    → ["Heart failure", "Cardiac failure", "Herzinsuffizienz", ...]
    """
    info = concept_lookup(sctid)
    terms = set()
    if "display" in info:
        terms.add(info["display"])
    for syn in info.get("synonyms", []):
        if "value" in syn:
            terms.add(syn["value"])
    return sorted(terms)


# ============================================================
# 6. UKLGPT-spezifisch: NER-Ergebnis normalisieren
# ============================================================
def normalize_ner_entity(text: str, semantic_tag: str = "disorder") -> list:
    """
    Nimmt einen NER-erkannten Freitext-Term und normalisiert ihn
    zu einem SNOMED-CT-Konzept.

    Parameter:
        text:         NER-erkannter Term (z.B. "Herzinsuffizienz")
        semantic_tag: SNOMED Semantic Tag Filter
                      ("disorder", "procedure", "substance", "body structure")

    Rückgabe: Liste von Kandidaten mit SCTID und Display-Name.

    Beispiel: normalize_ner_entity("Herzinsuffizienz", "disorder")
    → [{"sctid": "84114007", "display": "Heart failure"}]
    """
    # ECL für den semantic_tag-Filter
    ecl_roots = {
        "disorder": "<< 404684003",       # Clinical finding
        "procedure": "<< 71388002",        # Procedure
        "substance": "<< 105590001",       # Substance
        "body structure": "<< 123037004",  # Body structure
        "organism": "<< 410607006",        # Organism
    }
    ecl = ecl_roots.get(semantic_tag, "<< 138875005")  # Fallback: SNOMED Root

    return expand_ecl(ecl, filter_text=text, count=5)


# ============================================================
# Demo
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("SNOMED CT FHIR-API Beispiele für UKLGPT")
    print("=" * 60)

    # 1. Konzept-Lookup
    print("\n--- 1. $lookup: Herzinsuffizienz (84114007) ---")
    info = concept_lookup("84114007")
    print(json.dumps(info, indent=2, ensure_ascii=False))

    # 2. ECL-Suche: Untertypen von Herzinsuffizienz
    print("\n--- 2. $expand: Untertypen von Herzinsuffizienz ---")
    subtypes = expand_ecl("< 84114007", count=10)
    for c in subtypes:
        print(f"  {c['sctid']}: {c['display']}")

    # 3. NER-Normalisierung
    print("\n--- 3. NER-Normalisierung: 'Herzinsuffizienz' → SNOMED ---")
    candidates = normalize_ner_entity("heart failure", "disorder")
    for c in candidates:
        print(f"  {c['sctid']}: {c['display']}")

    # 4. Suchterme für Europe PMC
    print("\n--- 4. Diagnose-Terme für Europe PMC ---")
    terms = get_search_terms_for_diagnosis("84114007")
    print(f"  Suchterme: {terms}")

    print("\n✓ Alle Beispiele abgeschlossen.")
