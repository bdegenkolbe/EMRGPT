"""
SNOMED→Europe PMC Bridge für UKLGPT
=====================================
Integriertes Beispiel: Kombiniert SNOMED CT FHIR-API mit Europe PMC
zur automatischen Evidenz-Zuordnung auf Basis von Patientendiagnosen.

Workflow (entspricht Kap. 7.2.1.1 + 7.2.1.2 der Zielarchitektur):
1. SNOMED-CT-Codes der Patientendiagnosen → Snowstorm $lookup
2. Synonyme und Display-Terms extrahieren
3. Europe PMC Suche mit den extrahierten Termen
4. Ergebnis: Evidenz-Karten für das UI

DSGVO: Keine Patientendaten verlassen das System.
       Nur medizinische Fachbegriffe werden als Suchterme verwendet.
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime

# --- Konfiguration ---
SNOWSTORM_FHIR = "https://snowstorm.ihtsdotools.org/fhir"
EPMC_SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
SNOMED_SYSTEM = "http://snomed.info/sct"
CURRENT_YEAR = datetime.now().year
USER_AGENT = "UKLGPT-Prototype/1.0 (kontakt@ukl.de)"


def http_get_json(url: str) -> dict:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")
    req.add_header("User-Agent", USER_AGENT)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ============================================================
# Schritt 1: SNOMED-Konzept → Display-Term + Synonyme
# ============================================================
def get_snomed_terms(sctid: str) -> dict:
    """
    Ruft den bevorzugten Term und alle Synonyme eines SNOMED-Konzepts
    über die Snowstorm FHIR $lookup-Operation ab.
    """
    url = (
        f"{SNOWSTORM_FHIR}/CodeSystem/$lookup"
        f"?system={urllib.parse.quote(SNOMED_SYSTEM)}"
        f"&code={sctid}"
        f"&property=*"
    )
    data = http_get_json(url)

    result = {"sctid": sctid, "display": "", "synonyms": []}
    for param in data.get("parameter", []):
        if param.get("name") == "display":
            result["display"] = param.get("valueString", "")
        elif param.get("name") == "designation":
            value = ""
            for part in param.get("part", []):
                if part.get("name") == "value":
                    value = part.get("valueString", "")
            if value and value != result["display"]:
                result["synonyms"].append(value)
    return result


# ============================================================
# Schritt 2: SNOMED-ECL → Untertypen für breitere Suche
# ============================================================
def get_subtypes(sctid: str, max_count: int = 5) -> list:
    """
    Ruft die häufigsten Untertypen eines SNOMED-Konzepts ab.
    Nützlich um die Suche in Europe PMC zu erweitern.
    """
    ecl = f"< {sctid}"
    url = (
        f"{SNOWSTORM_FHIR}/ValueSet/$expand"
        f"?url={urllib.parse.quote(SNOMED_SYSTEM + '?fhir_vs=ecl/' + ecl)}"
        f"&count={max_count}"
        f"&includeDesignations=true"
    )
    data = http_get_json(url)
    return [
        entry.get("display", "")
        for entry in data.get("expansion", {}).get("contains", [])
    ]


# ============================================================
# Schritt 3: Europe PMC Suche
# ============================================================
def search_epmc(disease_term: str, max_results: int = 5) -> tuple:
    """
    Sucht Europe PMC nach Publikationen zu einem Krankheitsbegriff.
    Sortiert nach Zitationshäufigkeit, filtert auf letzte 2 Jahre.
    """
    query = (
        f'DISEASE:"{disease_term}" '
        f'AND PUB_YEAR:[{CURRENT_YEAR - 2} TO {CURRENT_YEAR}]'
    )
    url = (
        f"{EPMC_SEARCH}"
        f"?query={urllib.parse.quote(query)}"
        f"&format=json"
        f"&pageSize={max_results}"
        f"&sort=CITED%20desc"
        f"&resultType=core"
    )
    data = http_get_json(url)
    articles = []
    for a in data.get("resultList", {}).get("result", []):
        articles.append({
            "pmid": a.get("pmid"),
            "doi": a.get("doi"),
            "title": a.get("title"),
            "journal": a.get("journalTitle"),
            "year": a.get("pubYear"),
            "cited_by": a.get("citedByCount", 0),
            "is_open_access": a.get("isOpenAccess") == "Y",
            "abstract_snippet": (a.get("abstractText") or "")[:200],
        })
    return data.get("hitCount", 0), articles


# ============================================================
# Integrierter Workflow: SNOMED → Terme → Europe PMC
# ============================================================
def evidence_for_diagnosis(sctid: str) -> dict:
    """
    Kompletter Evidence-Matching-Workflow für eine einzelne Diagnose.

    Input:  SNOMED-CT-Code (z.B. "84114007" für Herzinsuffizienz)
    Output: Evidenz-Karte mit Publikationen und Metadaten

    Ablauf:
    1. SNOMED $lookup → Display-Term + Synonyme
    2. Europe PMC Suche mit dem Hauptterm
    3. Zusammenstellung der Evidenz-Karte
    """
    # Schritt 1: SNOMED-Terme abrufen
    snomed = get_snomed_terms(sctid)
    primary_term = snomed["display"]

    # Schritt 2: Europe PMC mit dem Hauptterm
    hit_count, articles = search_epmc(primary_term, max_results=5)

    # Evidenz-Karte zusammenstellen
    return {
        "diagnosis": {
            "sctid": sctid,
            "display": primary_term,
            "synonyms": snomed["synonyms"][:5],
        },
        "evidence": {
            "source": "Europe PMC",
            "query_term": primary_term,
            "total_hits": hit_count,
            "articles": articles,
        },
        "metadata": {
            "retrieved_at": datetime.now().isoformat(),
            "search_window": f"{CURRENT_YEAR - 2}–{CURRENT_YEAR}",
            "ranking": "by citation count (descending)",
        },
    }


def evidence_for_patient(diagnosis_sctids: list) -> list:
    """
    Evidence-Matching für einen gesamten Patientenfall.

    Input:  Liste von SNOMED-CT-Codes der aktiven Diagnosen
    Output: Liste von Evidenz-Karten (eine pro Diagnose)

    Beispiel:
        evidence_for_patient(["84114007", "49436004"])
        → Evidenz für Herzinsuffizienz + Vorhofflimmern
    """
    return [evidence_for_diagnosis(sctid) for sctid in diagnosis_sctids]


# ============================================================
# Demo
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("SNOMED → Europe PMC Bridge (UKLGPT Evidence-Matching)")
    print("=" * 60)

    # Beispiel: Patient mit Herzinsuffizienz und Vorhofflimmern
    patient_diagnoses = [
        "84114007",  # Heart failure
        "49436004",  # Atrial fibrillation
    ]

    print(f"\nPatient hat {len(patient_diagnoses)} aktive Diagnosen.")
    print("Starte Evidence-Matching...\n")

    for sctid in patient_diagnoses:
        print(f"--- Diagnose: SCTID {sctid} ---")

        try:
            card = evidence_for_diagnosis(sctid)
            diag = card["diagnosis"]
            print(f"  Display: {diag['display']}")
            print(f"  Synonyme: {diag['synonyms'][:3]}")
            print(f"  Europe PMC Treffer: {card['evidence']['total_hits']}")
            print(f"  Top-Publikationen:")
            for a in card["evidence"]["articles"][:3]:
                oa = " [OA]" if a["is_open_access"] else ""
                print(f"    [{a['year']}] {a['title'][:70]}...")
                print(f"           {a['journal']} | Zit: {a['cited_by']}{oa}")
        except Exception as e:
            print(f"  Fehler: {e}")

        print()

    print("✓ Evidence-Matching abgeschlossen.")
    print("  → Keine Patientendaten wurden übermittelt.")
    print("  → Nur SNOMED-Terme als Suchbegriffe verwendet.")
