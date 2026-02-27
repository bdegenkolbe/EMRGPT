# EMRGPT – KI-gestützter Klinischer Informationsassistent

**Universitätsklinikum Leipzig (UKL)**
**Stand: Februar 2026**

---

## Folie 1: Titel

# EMRGPT
### Der KI-gestützte klinische Informationsassistent des UKL

**Intelligente Recherche in 21 Millionen Patientendokumenten**

Vorprojekt-Ergebnis | Empfehlung für Lenkungsausschuss

---

## Folie 2: Das Problem

### Medizinische Altdaten werden unzugänglich

- **Oktober 2026:** SAP i.s.h.med wird abgeschaltet
- **21 Mio. Dokumente** müssen archiviert und zugänglich bleiben
- **Nur M-KIS (Meierhofer)** als neues führendes System
- **Aktuell:** Ärzte suchen **15–50 Minuten pro Tag** nach Informationen
- **HYDMedia-Archiv** ist komplex und wird daher oft nicht konsequent genutzt
- **Konsequenz:** Ärzte befragen Patienten erneut statt in der Akte zu suchen

---

## Folie 3: Die Vision

### EMRGPT – Die Brücke der Altdaten

```
   Frage in natürlicher                    Antwort mit Quellen-
   Sprache stellen              ──►        verweis in 10 Sek.

   "Hat der Patient               "Ja, Laborbefund vom 15.03.2024
    eine Penicillin-               zeigt Allergie-Nachweis.
    Allergie?"                     [Quelle: Arztbrief, 15.03.2024]"
```

**Von 7,5 Minuten Suchzeit auf 10 Sekunden.**

---

## Folie 4: Kernfunktionen

### Was kann EMRGPT?

| Funktion | Beschreibung |
|----------|-------------|
| **Intelligente Dokumentensuche** | Semantische Suche in natürlicher Sprache über alle Altdokumente |
| **Automatische Zusammenfassung** | KI-generierte Zusammenfassungen ganzer Patientenakten |
| **Quellenbasierte Antworten** | Jede Antwort mit Verweis auf Originaldokument, Datum, Typ |
| **Evidence-Matching** | Automatischer Abgleich mit aktueller Studienlage (Europe PMC) |
| **SNOMED-Tagging** | Automatische medizinische Codierung aller Dokumente |
| **M-KIS-Integration** | Direktaufruf aus dem Patientenkontext im neuen KIS |

---

## Folie 5: Architektur im Überblick

### Vier Wissensschichten – Ein Assistent

```
┌─────────────────────────────────────────────────────────────┐
│                    EMRGPT Frontend                          │
│              Chat-Interface im M-KIS                        │
├─────────────────────────────────────────────────────────────┤
│              Orchestrierungsschicht                          │
│         Domain-aware Prompt Pipeline                        │
│     (Qualitätssicherung, Halluzinations-Filterung)         │
├──────────┬──────────┬───────────────┬───────────────────────┤
│Patienten-│Dokumenten-│   GraphRAG    │  Evidenz- und        │
│   RAG    │   RAG     │(FHIR/SNOMED) │  Studien-Service     │
│          │           │              │                       │
│Episodisch│21 Mio.   │Strukturierte │Europe PMC,           │
│On-Demand │PDFs + OCR │Fakten (DWH)  │Leitlinien            │
└──────────┴──────────┴───────────────┴───────────────────────┘
             Berechtigungen: M-KIS → Gatekeeper
```

---

## Folie 6: Use Cases

### Vier zentrale Anwendungsfälle

**UC-1: Intelligente Dokumentenrecherche**
- Arzt stellt Frage in natürlicher Sprache
- System durchsucht alle relevanten Dokumente des Patienten
- Antwort mit Quellenangabe in Sekunden

**UC-2: Automatische Aktenzusammenfassung**
- Vollständige Übersicht über Patientenhistorie
- Chronologisch, nach Fachgebiet oder nach Relevanz
- Ideal für Aufnahme, Verlegung, Tumorboard

**UC-3: Dokumentations-Compliance**
- Prüfung auf Vollständigkeit und Konsistenz
- Unterstützung bei Qualitätssicherung

**UC-4: Evidence-Matching und SNOMED-Tagging**
- Automatischer Abgleich mit aktuellen Studien
- Medizinische Codierung der Dokumentenbasis

---

## Folie 7: Innovationsaspekte

### Was macht EMRGPT besonders?

1. **FHIR-konformer klinischer Graph**
   - Interoperabilität nach internationalem Standard
   - ISiK Stufe 3 kompatibel (gematik)

2. **SNOMED-CT als Referenzterminologie**
   - Einheitliche medizinische Semantik
   - Snowstorm On-Premise Terminologieserver

3. **Episodisches Patienten-RAG**
   - Privacy by Design: Daten werden on-demand geladen, nie dauerhaft im LLM
   - TTL-Mechanismus für automatische Datenlöschung

4. **Mehrstufige Prompt-Pipeline**
   - Qualitätssicherung vor jeder Antwort
   - Halluzinations-Erkennung und -Filterung

5. **Strikte Trennung: Fakten, Dokumente, Leitlinien**
   - Keine Vermischung von Patientendaten mit globalem Wissen

6. **Evidenz- und Studien-Service**
   - Vierte Wissensschicht mit Europe PMC-Anbindung

---

## Folie 8: Sicherheit und Datenschutz

### Höchste Standards für Patientendaten

| Aspekt | Umsetzung |
|--------|-----------|
| **Berechtigungen** | M-KIS als Permission-Master, Gatekeeper vor jedem Zugriff |
| **PSY/KJP-Schutz** | Sonderberechtigungen für sensible Fachbereiche |
| **Notfallzugriff** | Break-the-Glass mit dokumentierter Begründung |
| **Audit-Trail** | Revisionssichere Protokollierung aller Abfragen |
| **DSGVO** | Privacy by Design, Zweckbindung, episodische Verarbeitung |
| **On-Premise** | Keine Patientendaten in externer Cloud |
| **EU AI Act** | Transparenz, Risikomanagement, menschliche Aufsicht |
| **KRITIS** | BSI-konforme Infrastruktur |

---

## Folie 9: Nutzenquantifizierung

### Messbare Effizienzgewinne

| Kennzahl | Heute | Mit EMRGPT |
|----------|-------|------------|
| Suchzeit pro Anfrage | 5–10 Min. | ca. 10 Sek. |
| Rechercheaufwand pro Arzt/Tag | 15–50 Min. | ca. 1–2 Min. |
| Hochrechnung UKL (500 Ärzte) | – | **250 Arztstunden/Tag** Einsparung |
| Informationslücken | Häufig | Signifikant reduziert |
| Doppelbefragungen von Patienten | Regelmäßig | Nahezu eliminiert |

**Qualitative Verbesserungen:**
- Höhere Patientensicherheit durch vollständigere Information
- Reduktion der Frustrationslast beim klinischen Personal
- Bessere interdisziplinäre Zusammenarbeit

---

## Folie 10: Variantenvergleich

### Eigenlösung EMRGPT vs. Averbis/Meierhofer

| Kriterium | EMRGPT (Eigenlösung) | Averbis/Meierhofer |
|-----------|---------------------|-------------------|
| **Datenhoheit** | Vollständig (On-Premise) | Eingeschränkt (Vendor-Abhängigkeit) |
| **Archivdaten-Zugriff** | 21 Mio. Dokumente via RAG | Nur über HYDMedia-Standard |
| **KI-Pipeline-Kontrolle** | Vollständig | Black Box |
| **SNOMED/FHIR-Integration** | Nativ | Begrenzt |
| **Innovationstiefe** | Hoch (GraphRAG, Evidence) | Mittel (Medical Summary) |
| **Vendor Lock-in** | Kein | Hoch |
| **Betriebsaufwand** | Höher (eigenes Team) | Geringer (SaaS) |
| **Initialkosten** | Höher | Geringer |

**Empfehlung: Eigenlösung EMRGPT mit MVP-Ansatz**

---

## Folie 11: Umsetzungsfahrplan

### 4 Phasen bis zum Vollbetrieb

```
2026                                                          2027
Feb   Mär   Apr   Mai   Jun   Jul   Aug   Sep   Okt   Nov   Dez   Q1    Q2
 │◄── Phase 0: Vorprojekt ──►│                                             │
 │     LA-Entscheidung Apr    │                                             │
 │                      │◄── Phase 1: Infrastruktur + Archiv ──►│         │
 │                      │     GPU, FHIR, OCR, Berechtigungen     │         │
 │                            │◄── Phase 2: EMRGPT MVP ────►│             │
 │                            │     RAG, Pilot, Rollout       │             │
 │                                                       │◄─ SAP OFF ─►│  │
 │                                                            │◄── Phase 3: Vollausbau ──►│
 │                                                            │     GraphRAG, SNOMED, Rollout│
```

**Harter Termin:** MVP Go-Live zur SAP-Abschaltung im Oktober 2026

---

## Folie 12: Entscheidungsbedarf

### Drei Entscheidungen für den Lenkungsausschuss

1. **Umsetzungsvariante wählen:**
   Eigenlösung EMRGPT vs. Averbis/Meierhofer
   *Empfehlung: Eigenlösung mit MVP-Ansatz*

2. **Ressourcen freigeben:**
   Budget, Infrastruktur, Personal für Hauptprojekt

3. **Projektleiter installieren:**
   PM-Exzellenz als erklärtes Projektziel

### Konsequenzen bei Nicht-Entscheidung:
- Altdaten nur über manuelle Archivrecherche zugänglich
- Effizienzgewinne werden nicht realisiert
- Strategischer Nachteil gegenüber anderen Universitätskliniken

---

## Folie 13: Team und Kontakt

### Projektorganisation

| Rolle | Person/Bereich |
|-------|---------------|
| Auftraggeber | [zu benennen] |
| Projektleiter | [zu installieren – PM-Exzellenz] |
| IT-Architektur | Gert, Carina, Valentin |
| Fachbereich Medizin | Felix, Martin Neef, Niko v.D. |
| KIS-Verantwortlicher | Robert W. |
| Datenschutz | Hr. Sünkel |
| Informationssicherheit | S. Krause |

**Dokumentation:**
- Konzept_EMRGPT.md – Vollständige Zielarchitektur (22 Kapitel)
- PSP_EMRGPT.md – Produktstrukturplan (PRINCE2)
- Projektplan.md – 116 YouTrack-Tickets in 4 Phasen
