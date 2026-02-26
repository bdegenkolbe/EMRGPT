# Codebeispiele UKLGPT – SNOMED CT & Europe PMC

## Verzeichnisstruktur

```
Codebeispiele/
├── snomed-snowstorm-api/          ← Original-Beispiele aus IHTSDO/SNOMED-in-5-minutes
│   ├── python/examples.py         ← Python 3: Konzept-Suche, Description-Lookup
│   ├── javascript/app.js          ← AngularJS: Browser-basierte SNOMED-Suche
│   ├── curl/snomed-in-5-min-curl.md ← curl-Beispiele mit Erklärungen
│   ├── go/snomed.go               ← Go: CLI-Tool für SNOMED-Abfragen
│   ├── ruby/examples.rb           ← Ruby: Konzept- und Beschreibungssuche
│   ├── php/Snomed.php             ← PHP/Guzzle: SNOMED-Client-Klasse
│   ├── php/examples.php           ← PHP: Beispielaufrufe
│   ├── example.http               ← HTTP-Datei (für VS Code REST Client)
│   └── LICENSE.md                 ← Apache 2.0 (IHTSDO)
│
├── snomed-fhir-api/               ← UKLGPT-spezifisch: FHIR R4 API
│   ├── snomed_fhir_examples.py    ← $lookup, $expand (ECL), $translate, $subsumes
│   │                                 + NER-Normalisierung, Diagnose→Suchterme
│   └── snomed_to_europepmc_bridge.py ← Integrierter Workflow:
│                                       SNOMED-Diagnose → Terme → Europe PMC Suche
│
└── europe-pmc-api/                ← UKLGPT-spezifisch: Europe PMC REST API
    └── europe_pmc_examples.py     ← Krankheitssuche, Krankheit+Medikament,
                                     Leitlinien, Zitationen, Text-Mining,
                                     Evidence-Matching für Patientendiagnosen
```

## Bezug zur Zielarchitektur

| Codebeispiel | Architektur-Kapitel | Funktion |
|---|---|---|
| `snomed_fhir_examples.py` | Kap. 14.2.1 (Snowstorm FHIR-API) | SNOMED-Lookup, ECL-Suche, ICD-10-Mapping |
| `snomed_fhir_examples.py` → `normalize_ner_entity()` | Kap. 14.2.2 (SNOMED-Autotagging) | NER-Ergebnis → SNOMED-CT normalisieren |
| `europe_pmc_examples.py` | Kap. 7.2.1.1 (Europe PMC) | Literatursuche, Leitlinien, Text-Mining |
| `europe_pmc_examples.py` → `evidence_match_for_patient()` | Kap. 7.2.1.2 (Evidence-Matching) | Diagnosen → aktuelle Publikationen |
| `snomed_to_europepmc_bridge.py` | Kap. 7.2.1.1 + 7.2.1.2 | SNOMED → Terme → Europe PMC (End-to-End) |
| `snomed-snowstorm-api/*` | Kap. 14.2.1 (Referenz) | Original IHTSDO-Beispiele (Snowstorm native API) |

## Schnellstart

```bash
# SNOMED FHIR-API testen
python3 Codebeispiele/snomed-fhir-api/snomed_fhir_examples.py

# Europe PMC testen
python3 Codebeispiele/europe-pmc-api/europe_pmc_examples.py

# Integrierter Workflow: SNOMED → Europe PMC
python3 Codebeispiele/snomed-fhir-api/snomed_to_europepmc_bridge.py
```

Keine externen Abhängigkeiten – alle Beispiele nutzen nur die Python-Standardbibliothek.

## Quellen & Lizenzen

- **SNOMED-in-5-minutes**: [IHTSDO/SNOMED-in-5-minutes](https://github.com/IHTSDO/SNOMED-in-5-minutes) (Apache 2.0)
- **Snowstorm FHIR-API**: [IHTSDO/snowstorm](https://github.com/IHTSDO/snowstorm/blob/master/docs/using-the-fhir-api.md)
- **Europe PMC REST-API**: [europepmc.org/RestfulWebService](https://europepmc.org/RestfulWebService)
- **SNOMED CT Browser**: [browser.ihtsdotools.org](https://browser.ihtsdotools.org)
