"""
Europe PMC REST-API Beispiele für UKLGPT
=========================================
Nutzt die Europe PMC REST-API für:
- Volltextsuche mit klinischen Feldern (DISEASE, CHEM, GENE_PROTEIN)
- Annotations-API (Text-Mining: Krankheiten, Gene, Chemikalien)
- Zitations- und Referenzabruf
- Evidence-Matching: SNOMED-Diagnose → aktuelle Publikationen

Referenz: https://europepmc.org/RestfulWebService
API-Docs: https://europepmc.org/searchsyntax
Lizenz:   Open Access (Europe PMC, EMBL-EBI)

DSGVO-Konformität: Keine Patientendaten werden übermittelt.
Alle Anfragen enthalten ausschließlich medizinische Fachbegriffe.
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime

# --- Konfiguration ---
EPMC_BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest"
EPMC_SEARCH = f"{EPMC_BASE}/search"
CURRENT_YEAR = datetime.now().year


def epmc_get(url: str) -> dict:
    """HTTP GET mit JSON-Parsing."""
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")
    req.add_header("User-Agent", "UKLGPT-Prototype/1.0 (kontakt@ukl.de)")
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ============================================================
# 1. Einfache Suche nach Krankheitsbegriff
# ============================================================
def search_by_disease(disease: str, max_results: int = 10) -> list:
    """
    Sucht Publikationen zu einer Krankheit.

    Nutzt das DISEASE-Feld (Text-Mining-basiert, präziser als Freitext).

    Beispiel: search_by_disease("heart failure")
    """
    query = f'DISEASE:"{disease}" AND PUB_YEAR:[{CURRENT_YEAR - 2} TO {CURRENT_YEAR}]'
    url = (
        f"{EPMC_SEARCH}"
        f"?query={urllib.parse.quote(query)}"
        f"&format=json"
        f"&pageSize={max_results}"
        f"&sort=CITED%20desc"
        f"&resultType=core"
    )
    data = epmc_get(url)
    results = []
    for article in data.get("resultList", {}).get("result", []):
        results.append({
            "pmid": article.get("pmid"),
            "doi": article.get("doi"),
            "title": article.get("title"),
            "authors": article.get("authorString"),
            "journal": article.get("journalTitle"),
            "year": article.get("pubYear"),
            "cited_by": article.get("citedByCount", 0),
            "is_open_access": article.get("isOpenAccess") == "Y",
            "abstract": article.get("abstractText", "")[:300] + "...",
        })
    return data.get("hitCount", 0), results


# ============================================================
# 2. Kombinierte Suche (Krankheit + Medikament)
# ============================================================
def search_disease_and_drug(disease: str, drug: str, max_results: int = 10) -> list:
    """
    Findet Publikationen zur Kombination Krankheit + Medikament.

    Beispiel: search_disease_and_drug("heart failure", "sacubitril")
    """
    query = (
        f'DISEASE:"{disease}" AND CHEM:"{drug}" '
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
    data = epmc_get(url)
    return data.get("hitCount", 0), [
        {
            "pmid": a.get("pmid"),
            "title": a.get("title"),
            "journal": a.get("journalTitle"),
            "year": a.get("pubYear"),
            "cited_by": a.get("citedByCount", 0),
        }
        for a in data.get("resultList", {}).get("result", [])
    ]


# ============================================================
# 3. Leitlinien und Systematic Reviews suchen
# ============================================================
def search_guidelines(disease: str, max_results: int = 5) -> list:
    """
    Sucht gezielt nach klinischen Leitlinien und Systematic Reviews
    zu einer Krankheit.

    Beispiel: search_guidelines("diabetes mellitus type 2")
    """
    query = (
        f'DISEASE:"{disease}" '
        f'AND (PUB_TYPE:"review" OR PUB_TYPE:"guideline" OR TITLE:"guideline" OR TITLE:"systematic review") '
        f'AND PUB_YEAR:[{CURRENT_YEAR - 3} TO {CURRENT_YEAR}]'
    )
    url = (
        f"{EPMC_SEARCH}"
        f"?query={urllib.parse.quote(query)}"
        f"&format=json"
        f"&pageSize={max_results}"
        f"&sort=CITED%20desc"
        f"&resultType=core"
    )
    data = epmc_get(url)
    return data.get("hitCount", 0), [
        {
            "pmid": a.get("pmid"),
            "doi": a.get("doi"),
            "title": a.get("title"),
            "journal": a.get("journalTitle"),
            "year": a.get("pubYear"),
            "cited_by": a.get("citedByCount", 0),
            "is_open_access": a.get("isOpenAccess") == "Y",
        }
        for a in data.get("resultList", {}).get("result", [])
    ]


# ============================================================
# 4. Zitationen eines Artikels abrufen
# ============================================================
def get_citations(source: str, article_id: str, max_results: int = 10) -> list:
    """
    Ruft Artikel ab, die einen bestimmten Artikel zitieren.

    Beispiel: get_citations("MED", "33378469")
    """
    url = (
        f"{EPMC_BASE}/{source}/{article_id}/citations"
        f"?format=json"
        f"&page=1"
        f"&pageSize={max_results}"
    )
    data = epmc_get(url)
    return [
        {
            "pmid": c.get("id"),
            "title": c.get("title"),
            "journal": c.get("journalAbbreviation"),
            "year": c.get("pubYear"),
        }
        for c in data.get("citationList", {}).get("citation", [])
    ]


# ============================================================
# 5. Text-Mining-Annotationen abrufen
# ============================================================
def get_annotations(source: str, article_id: str) -> list:
    """
    Ruft Text-Mining-Annotationen (Krankheiten, Gene, Chemikalien)
    für einen Artikel ab.

    Beispiel: get_annotations("MED", "33378469")
    """
    url = (
        f"{EPMC_BASE}/{source}/{article_id}/textMinedTerms"
        f"?format=json"
        f"&page=1"
        f"&pageSize=50"
    )
    data = epmc_get(url)
    annotations = {}
    for term in data.get("semanticTypeList", {}).get("semanticType", []):
        sem_type = term.get("name", "unknown")
        annotations[sem_type] = [
            {"term": t.get("term"), "count": t.get("count")}
            for t in term.get("tmSummary", [])[:5]
        ]
    return annotations


# ============================================================
# 6. UKLGPT Evidence-Matching: SNOMED-Diagnosen → Publikationen
# ============================================================
def evidence_match_for_patient(diagnoses: list, max_per_diagnosis: int = 5) -> dict:
    """
    Kernfunktion für das automatische Evidence-Matching (Kap. 7.2.1.2).

    Nimmt eine Liste von Patientendiagnosen (als Strings, idealerweise
    SNOMED-Display-Terms) und ruft für jede die relevantesten
    aktuellen Publikationen aus Europe PMC ab.

    Parameter:
        diagnoses: Liste von Diagnose-Strings
                   (z.B. ["Heart failure", "Atrial fibrillation"])
        max_per_diagnosis: Anzahl Treffer pro Diagnose

    Rückgabe: Dict mit Diagnose als Key, Publikationsliste als Value.

    DSGVO: Es werden NUR medizinische Fachbegriffe übermittelt,
           KEINE Patientendaten (Name, Geburtsdatum, Fall-Nr. etc.).
    """
    evidence = {}
    for diagnosis in diagnoses:
        hit_count, articles = search_by_disease(diagnosis, max_per_diagnosis)
        guidelines_count, guidelines = search_guidelines(diagnosis, 3)

        evidence[diagnosis] = {
            "total_publications": hit_count,
            "top_articles": articles,
            "total_guidelines": guidelines_count,
            "top_guidelines": guidelines,
        }
    return evidence


# ============================================================
# Demo
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Europe PMC REST-API Beispiele für UKLGPT")
    print("=" * 60)

    # 1. Krankheitssuche
    print("\n--- 1. Suche: 'heart failure' (letzte 2 Jahre, nach Zitationen) ---")
    count, articles = search_by_disease("heart failure", 3)
    print(f"  Treffer gesamt: {count}")
    for a in articles:
        print(f"  [{a['year']}] {a['title'][:80]}... (Zitationen: {a['cited_by']})")

    # 2. Kombinierte Suche
    print("\n--- 2. Kombiniert: 'heart failure' + 'sacubitril' ---")
    count, articles = search_disease_and_drug("heart failure", "sacubitril", 3)
    print(f"  Treffer gesamt: {count}")
    for a in articles:
        print(f"  [{a['year']}] {a['title'][:80]}...")

    # 3. Leitlinien
    print("\n--- 3. Leitlinien zu 'diabetes mellitus type 2' ---")
    count, guidelines = search_guidelines("diabetes mellitus type 2", 3)
    print(f"  Treffer gesamt: {count}")
    for g in guidelines:
        print(f"  [{g['year']}] {g['title'][:80]}... (OA: {g['is_open_access']})")

    # 4. Evidence-Matching (Kernfunktion)
    print("\n--- 4. Evidence-Matching für Patientendiagnosen ---")
    patient_diagnoses = ["Heart failure", "Atrial fibrillation"]
    evidence = evidence_match_for_patient(patient_diagnoses, 2)
    for diag, data in evidence.items():
        print(f"\n  Diagnose: {diag}")
        print(f"    Publikationen: {data['total_publications']}")
        print(f"    Leitlinien: {data['total_guidelines']}")
        for a in data["top_articles"]:
            print(f"    - [{a['year']}] {a['title'][:60]}... (Zit: {a['cited_by']})")

    print("\n✓ Alle Beispiele abgeschlossen.")
