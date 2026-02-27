# Projektplan EMRGPT – YouTrack-Tickets

**Version:** 1.0 | **Stand:** 2026-02-27
**Projekt:** EMRGPT – KI-gestützter klinischer Informationsassistent
**Methodik:** PRINCE2 / Agil (Hybrid)
**Referenz:** [Konzept_EMRGPT.md](Konzept_EMRGPT.md) | [PSP_EMRGPT.md](PSP_EMRGPT.md)

---

## Ticket-Konventionen

| Feld | Beschreibung |
|------|-------------|
| **Ticket-ID** | EMRGPT-{Phase}{Nummer}, z.B. EMRGPT-P0-001 |
| **Typ** | Epic / Story / Task / Bug |
| **Priorität** | Blocker / Critical / Major / Normal / Minor |
| **Sprint** | Kalenderwochen-Zuordnung |
| **Label** | Phase, Bereich (Infra, Backend, Frontend, Security, Data, PM) |

---

## Phase 0: Vorprojekt-Abschluss (Feb – Jun 2026)

### Epic: EMRGPT-P0 – Vorprojekt abschließen und LA-Entscheidung herbeiführen

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P0-001 | Story | Vorprojekt-Ergebnisse konsolidieren und QA abschließen | Critical | PM | KW09–KW12 | – | M0.1 |
| EMRGPT-P0-002 | Task | Qualitätsanalyse aller Konzeptdokumente durchführen | Major | PM | KW09–KW10 | – | M0.1 |
| EMRGPT-P0-003 | Task | PSP-Vollständigkeitsprüfung gegen Konzept_EMRGPT.md | Major | PM | KW10–KW11 | P0-002 | M0.1 |
| EMRGPT-P0-004 | Story | Averbis/Meierhofer-Angebot einholen und bewerten | Critical | PM, 4K | KW09–KW13 | – | M0.2 |
| EMRGPT-P0-005 | Task | Anfrage an Meierhofer für Averbis Health Discovery senden | Major | PM | KW09 | – | M0.2 |
| EMRGPT-P0-006 | Task | Variantenvergleich mit Averbis-Angebot finalisieren | Critical | PM | KW12–KW13 | P0-005 | M0.2 |
| EMRGPT-P0-007 | Story | Kostenseite Business Case fertigstellen | Critical | Controlling | KW10–KW16 | P0-004 | M0.3 |
| EMRGPT-P0-008 | Task | IT-Infrastruktur-Sizing durchführen (GPU, Speicher, Netzwerk) | Major | IT-Infra | KW10–KW14 | – | M0.3 |
| EMRGPT-P0-009 | Task | Kostengerüst-Template (Kap. 20) mit konkreten Werten befüllen | Critical | Controlling | KW14–KW16 | P0-008, P0-004 | M0.3 |
| EMRGPT-P0-010 | Story | LA-Entscheidungsvorlage erstellen und präsentieren | Blocker | PM | KW15–KW17 | P0-001, P0-006, P0-007 | M0.4 |
| EMRGPT-P0-011 | Task | Management-Entscheidungsvorlage (3 Entscheidungspunkte) aufbereiten | Critical | PM | KW15–KW16 | P0-001, P0-006 | M0.4 |
| EMRGPT-P0-012 | Task | LA-Präsentation vorbereiten und durchführen | Critical | PM | KW16–KW17 | P0-011 | M0.4 |
| EMRGPT-P0-013 | Story | Projektleiter installieren und Team aufstellen | Critical | Auftraggeber | KW17–KW22 | P0-010 | M0.5 |
| EMRGPT-P0-014 | Task | Stellenausschreibung / interne Besetzung PL vorbereiten | Major | HR, Auftraggeber | KW17–KW19 | P0-010 | M0.5 |
| EMRGPT-P0-015 | Task | Projektteam-Setup und Kick-off Hauptprojekt | Major | PL (neu) | KW20–KW22 | P0-014 | M0.5 |
| EMRGPT-P0-016 | Story | Vorprojekt formal abschließen und abnehmen | Major | Auftraggeber | KW22–KW26 | Alle P0 | M0.6 |
| EMRGPT-P0-017 | Task | Abnahmedokument Vorprojekt erstellen | Major | PM | KW22–KW24 | P0-001 | M0.6 |
| EMRGPT-P0-018 | Task | Formale Abnahme durch Auftraggeber einholen | Major | Auftraggeber | KW24–KW26 | P0-017 | M0.6 |
| EMRGPT-P0-019 | Task | Fachliche Anforderungen mit Fachbereich abstimmen (FA/NFA-Liste) | Critical | Fachbereich | KW09–KW13 | – | M0.1 |
| EMRGPT-P0-020 | Task | Formale Risikobewertung mit Eintrittswahrscheinlichkeiten erstellen | Major | PM | KW10–KW13 | – | M0.1 |

---

## Phase 1: Infrastruktur und Archiv-Migration (Mai – Sep 2026)

### Epic: EMRGPT-P1-INFRA – GPU-Infrastruktur und Basisplattform

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P1-001 | Story | GPU-Infrastruktur beschaffen und bereitstellen | Blocker | IT-Infra | KW18–KW26 | M0.4 (Budgetfreigabe) | M1.1 |
| EMRGPT-P1-002 | Task | GPU-Server spezifizieren (VRAM, Compute, Storage) | Critical | IT-Infra | KW18–KW19 | P0-008 | M1.1 |
| EMRGPT-P1-003 | Task | Beschaffungsprozess starten (Angebot, Genehmigung, Bestellung) | Critical | IT-Infra | KW19–KW22 | P1-002 | M1.1 |
| EMRGPT-P1-004 | Task | GPU-Server installieren und Basisumgebung konfigurieren | Major | IT-Infra | KW22–KW26 | P1-003 | M1.1 |
| EMRGPT-P1-005 | Task | Netzwerk-Segmentierung und Firewall-Regeln für EMRGPT-Zone | Major | IT-Netzwerk | KW20–KW24 | – | M1.1 |

### Epic: EMRGPT-P1-ARCHIV – SAP-DOK-Migration und Dokumentenarchiv

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P1-010 | Story | SAP-DOK-Migration nach HYDMedia abschließen | Blocker | IT, DMI | KW07–KW26 | – (gestartet KW7/2026) | M1.2 |
| EMRGPT-P1-011 | Task | Migration 20 Jahre SAP-Dokumente über DMI-Pipeline überwachen | Critical | IT | KW07–KW22 | – | M1.2 |
| EMRGPT-P1-012 | Task | Migrationsstatus-Reporting und Qualitätsstichproben | Major | IT | KW12–KW26 | P1-011 | M1.2 |
| EMRGPT-P1-013 | Task | Migration formal abschließen und Vollständigkeit bestätigen | Critical | IT | KW24–KW26 | P1-011 | M1.2 |

### Epic: EMRGPT-P1-OCR – OCR-Verarbeitung und Dokumentenqualität

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P1-020 | Story | OCR-Pilottest durchführen und Qualität validieren | Critical | IT | KW18–KW30 | OCR-Installation (Feb 2026) | M1.3 |
| EMRGPT-P1-021 | Task | OCR-Testkorpus definieren (1000 Dokumente, diverse Typen) | Major | IT | KW18–KW20 | – | M1.3 |
| EMRGPT-P1-022 | Task | OCR-Verarbeitung durchführen und Qualitätsrate messen | Major | IT | KW20–KW26 | P1-021 | M1.3 |
| EMRGPT-P1-023 | Task | OCR-Qualitätsbericht erstellen (Ziel: > 90% Erkennungsrate) | Major | IT | KW26–KW30 | P1-022 | M1.3 |

### Epic: EMRGPT-P1-FHIR – Dedalus FHIR-Schnittstelle validieren

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P1-030 | Story | Dedalus FHIR-Schnittstelle validieren (Go/No-Go) | Blocker | IT-Arch | KW22–KW30 | Dedalus-Zusage | M1.4 |
| EMRGPT-P1-031 | Task | FHIR-Testumgebung aufsetzen (DocumentReference, Binary, Patient) | Critical | IT-Arch | KW22–KW24 | – | M1.4 |
| EMRGPT-P1-032 | Task | Performance-Test: Abfragelatenz, Durchsatz, Concurrency | Critical | IT-Arch | KW24–KW28 | P1-031 | M1.4 |
| EMRGPT-P1-033 | Task | Scope-Validierung: verfügbare FHIR-Ressourcen vs. Anforderungen | Major | IT-Arch | KW24–KW26 | P1-031 | M1.4 |
| EMRGPT-P1-034 | Task | Go/No-Go-Entscheidung FHIR dokumentieren | Blocker | IT-Arch, PM | KW28–KW30 | P1-032, P1-033 | M1.4 |

### Epic: EMRGPT-P1-AUTH – Berechtigungskonzept M-KIS

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P1-040 | Story | M-KIS-Berechtigungskonzept fertigstellen | Critical | Security | KW22–KW35 | M-KIS Go-Live-Planung | M1.5 |
| EMRGPT-P1-041 | Task | SAP-Berechtigungsmodell auf M-KIS-Rollen mappen | Critical | M. Schmeißer | KW22–KW28 | – | M1.5 |
| EMRGPT-P1-042 | Task | Sonderberechtigungen PSY/KJP in M-KIS abbilden | Major | Security | KW26–KW30 | P1-041 | M1.5 |
| EMRGPT-P1-043 | Task | Abstimmung Berechtigungskonzept mit Meierhofer | Major | Robert W. | KW28–KW32 | P1-041 | M1.5 |
| EMRGPT-P1-044 | Task | Break-the-Glass-Prozess für Notfallzugriff definieren | Major | Security, DSB | KW30–KW35 | P1-041 | M1.5 |

### Epic: EMRGPT-P1-PLAT – Basisplattform bereitstellen

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P1-050 | Story | Basisinfrastruktur produktionsreif machen | Critical | IT-Infra | KW26–KW39 | M1.1 | M1.6 |
| EMRGPT-P1-051 | Task | Vektor-Datenbank installieren und konfigurieren (Milvus/Qdrant) | Critical | IT-Infra | KW26–KW30 | P1-004 | M1.6 |
| EMRGPT-P1-052 | Task | Graph-Datenbank installieren und konfigurieren (Neo4j) | Critical | IT-Infra | KW26–KW30 | P1-004 | M1.6 |
| EMRGPT-P1-053 | Task | LLM-Instanz deployen und Inferenz-Performance validieren | Critical | IT-Arch | KW30–KW35 | P1-004 | M1.6 |
| EMRGPT-P1-054 | Task | Monitoring-Stack aufsetzen (Prometheus, Grafana, DCGM) | Major | IT-Infra | KW30–KW35 | P1-004 | M1.6 |
| EMRGPT-P1-055 | Task | Backup- und Recovery-Konzept implementieren | Major | IT-Infra | KW35–KW39 | P1-051, P1-052 | M1.6 |

---

## Phase 2: EMRGPT MVP (Jul – Dez 2026)

### Epic: EMRGPT-P2-RAG – Dokumenten-RAG Prototyp

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-001 | Story | Dokumenten-RAG Prototyp entwickeln | Blocker | Backend | KW28–KW35 | M1.3, M1.4 | M2.1 |
| EMRGPT-P2-002 | Task | Embedding-Pipeline für OCR-verarbeitete PDFs implementieren | Critical | Backend | KW28–KW30 | M1.3 | M2.1 |
| EMRGPT-P2-003 | Task | Vektor-Suche mit Chunk-Strategie implementieren | Critical | Backend | KW30–KW32 | P2-002 | M2.1 |
| EMRGPT-P2-004 | Task | FHIR-Connector: DocumentReference→Binary Abruf implementieren | Critical | Backend | KW28–KW32 | M1.4 | M2.1 |
| EMRGPT-P2-005 | Task | Pilotstichprobe indexieren und Suchqualität evaluieren | Critical | Backend | KW32–KW35 | P2-003, P2-004 | M2.1 |
| EMRGPT-P2-006 | Task | Dedup-Logik implementieren (Hash-Vergleich, Timestamp-Gewichtung) | Major | Backend | KW30–KW34 | P2-002 | M2.1 |

### Epic: EMRGPT-P2-AUTH – Berechtigungs-Integration

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-010 | Story | Berechtigungs-Integration M-KIS → EMRGPT validieren | Blocker | Security | KW30–KW39 | M1.5 | M2.2 |
| EMRGPT-P2-011 | Task | Gatekeeper-Service implementieren (Berechtigungsprüfung vor Datenzugriff) | Critical | Backend | KW30–KW35 | M1.5 | M2.2 |
| EMRGPT-P2-012 | Task | M-KIS-Session-/Token-Integration implementieren | Critical | Backend | KW32–KW37 | P2-011 | M2.2 |
| EMRGPT-P2-013 | Task | Berechtigungs-Integrationstests mit M-KIS-Testumgebung | Critical | QA | KW37–KW39 | P2-012 | M2.2 |

### Epic: EMRGPT-P2-AUDIT – Audit-Trail und Logging

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-020 | Story | Audit-Trail und Logging implementieren | Critical | Backend | KW30–KW39 | – | M2.3 |
| EMRGPT-P2-021 | Task | Revisionssicheres Logging aller LLM-Abfragen und Datenzugriffe | Critical | Backend | KW30–KW35 | – | M2.3 |
| EMRGPT-P2-022 | Task | Logging-Dashboard in Grafana einrichten | Major | IT-Infra | KW35–KW37 | P2-021 | M2.3 |
| EMRGPT-P2-023 | Task | Compliance-Review Logging-Konzept durch ISB und DSB | Major | ISB, DSB | KW37–KW39 | P2-021 | M2.3 |

### Epic: EMRGPT-P2-UI – Frontend / Benutzeroberfläche

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-030 | Story | EMRGPT-Frontend für MVP entwickeln | Critical | Frontend | KW30–KW40 | – | M2.4 |
| EMRGPT-P2-031 | Task | Chat-Interface mit Patientenkontext-Auswahl implementieren | Critical | Frontend | KW30–KW35 | – | M2.4 |
| EMRGPT-P2-032 | Task | Quellenangaben-Panel (Dokument, Datum, Typ) einbauen | Critical | Frontend | KW33–KW37 | P2-031 | M2.4 |
| EMRGPT-P2-033 | Task | Sicherheits- und Transparenzelemente (Disclaimer, Confidence) | Major | Frontend | KW35–KW38 | P2-031 | M2.4 |
| EMRGPT-P2-034 | Task | M-KIS-Integration (Aufruf aus Patientenkontext) | Critical | Frontend | KW36–KW40 | P2-012, P2-031 | M2.4 |

### Epic: EMRGPT-P2-PROMPT – Prompt-Pipeline und Orchestrierung

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-040 | Story | Prompt-Pipeline für medizinische Qualitätssicherung implementieren | Critical | Backend | KW32–KW40 | P2-001 | M2.4 |
| EMRGPT-P2-041 | Task | Domain-aware Prompt Orchestration implementieren | Critical | Backend | KW32–KW36 | – | M2.4 |
| EMRGPT-P2-042 | Task | Medizinische Prompt-Pipeline (Kontext→Retrieval→Validierung→Antwort) | Critical | Backend | KW34–KW38 | P2-041 | M2.4 |
| EMRGPT-P2-043 | Task | Halluzinations-Erkennung und -Filterung implementieren | Major | Backend | KW36–KW40 | P2-042 | M2.4 |

### Epic: EMRGPT-P2-MVP – MVP Go-Live und Pilot

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-050 | Story | MVP Go-Live auf 1 Pilotstation (Go/No-Go Okt 2026) | Blocker | PM, PL | KW39–KW43 | M1.6, M2.1–M2.3 | M2.4 |
| EMRGPT-P2-051 | Task | End-to-End-Test auf Pilotstation durchführen | Blocker | QA | KW39–KW40 | Alle P2-Epics | M2.4 |
| EMRGPT-P2-052 | Task | Security-Audit vor Go-Live | Critical | ISB | KW40–KW41 | P2-010, P2-020 | M2.4 |
| EMRGPT-P2-053 | Task | DSB-Freigabe für Pilotbetrieb einholen | Critical | DSB | KW41–KW42 | P2-052 | M2.4 |
| EMRGPT-P2-054 | Task | Pilotstation-Schulung für klinisches Personal | Major | Fachbereich | KW42–KW43 | – | M2.4 |
| EMRGPT-P2-055 | Task | Go-Live Pilotstation und Monitoring-Phase starten | Blocker | PL | KW43 | P2-051, P2-053 | M2.4 |

### Epic: EMRGPT-P2-FEEDBACK – Pilotfeedback und Iteration

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P2-060 | Story | Pilotfeedback auswerten und Iterationsplanung | Critical | PM | KW44–KW48 | M2.4 | M2.5 |
| EMRGPT-P2-061 | Task | Feedback-Sammlung von Pilotstation (2 Wochen) | Major | Fachbereich | KW44–KW46 | M2.4 | M2.5 |
| EMRGPT-P2-062 | Task | Feedback auswerten und Verbesserungsplan erstellen | Major | PM, Backend | KW46–KW48 | P2-061 | M2.5 |
| EMRGPT-P2-063 | Task | Kritische Verbesserungen umsetzen | Major | Backend | KW48–KW50 | P2-062 | M2.6 |
| EMRGPT-P2-070 | Story | MVP auf 3 weitere Stationen ausrollen | Major | PL | KW49–KW52 | M2.5 | M2.6 |
| EMRGPT-P2-071 | Task | Rollout-Planung und Stationsauswahl | Major | PL, Fachbereich | KW49 | P2-062 | M2.6 |
| EMRGPT-P2-072 | Task | Schulung und Go-Live auf 3 Stationen | Major | Fachbereich | KW50–KW52 | P2-071 | M2.6 |

---

## Phase 3: Vollausbau (Q1 – Q2/2027)

### Epic: EMRGPT-P3-GRAPH – GraphRAG-Integration

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P3-001 | Story | GraphRAG-Integration (strukturierte Fakten aus UKLytics/DWH) | Critical | Backend | KW01–KW04/2027 | DWH-Anbindung | M3.1 |
| EMRGPT-P3-002 | Task | DWH-Extraktor für Diagnosen, Medikation, Labor implementieren | Critical | Backend | KW01–KW02/2027 | – | M3.1 |
| EMRGPT-P3-003 | Task | FHIR→Neo4j Graph-Transformation implementieren | Critical | Backend | KW02–KW03/2027 | P3-002 | M3.1 |
| EMRGPT-P3-004 | Task | GraphRAG-Abfragen in Orchestrierungsschicht integrieren | Critical | Backend | KW03–KW04/2027 | P3-003 | M3.1 |

### Epic: EMRGPT-P3-LEITLINIEN – Leitlinien-RAG und Evidenz

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P3-010 | Story | Leitlinien-RAG (Globales Wissen) integrieren | Major | Backend | KW04–KW08/2027 | – | M3.2 |
| EMRGPT-P3-011 | Task | Leitlinien-Korpus aufbauen und indexieren | Major | Backend | KW04–KW06/2027 | – | M3.2 |
| EMRGPT-P3-012 | Task | Leitlinien-Retrieval in Prompt-Pipeline integrieren | Major | Backend | KW06–KW08/2027 | P3-011 | M3.2 |
| EMRGPT-P3-013 | Story | Europe PMC-Anbindung produktiv setzen | Major | Backend | KW06–KW09/2027 | M3.2 | M3.2a |
| EMRGPT-P3-014 | Task | Europe PMC API-Integration implementieren | Major | Backend | KW06–KW07/2027 | – | M3.2a |
| EMRGPT-P3-015 | Task | Evidence-Matching-Algorithmus implementieren | Major | Backend | KW07–KW09/2027 | P3-014 | M3.2a |

### Epic: EMRGPT-P3-SNOMED – SNOMED-CT und OCR-Vollverarbeitung

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P3-020 | Story | Vollständige OCR-Verarbeitung des Dokumentenbestands | Critical | IT | KW01–KW13/2027 | Rechenkapazität | M3.3 |
| EMRGPT-P3-021 | Task | OCR-Batch-Verarbeitung für 21 Mio. Dokumente planen und starten | Critical | IT | KW01–KW04/2027 | – | M3.3 |
| EMRGPT-P3-022 | Task | Qualitäts-Monitoring der OCR-Verarbeitung | Major | IT | KW04–KW13/2027 | P3-021 | M3.3 |
| EMRGPT-P3-023 | Story | SNOMED-Autotagging-Pipeline produktiv setzen | Major | Backend | KW08–KW13/2027 | M3.3 | M3.3a |
| EMRGPT-P3-024 | Task | NER-Modell für medizinische Entitäten trainieren/konfigurieren | Major | Backend | KW08–KW10/2027 | – | M3.3a |
| EMRGPT-P3-025 | Task | Snowstorm On-Premise bereitstellen und validieren | Major | IT-Infra | KW08–KW13/2027 | – | M3.3b |
| EMRGPT-P3-026 | Task | NER→Snowstorm FHIR-API Pipeline integrieren | Major | Backend | KW10–KW13/2027 | P3-024, P3-025 | M3.3a |

### Epic: EMRGPT-P3-LABOR – Labor-FHIR-Connector

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P3-030 | Story | Labor-FHIR-Connector über UKLytics produktiv setzen | Major | IT | KW09–KW17/2027 | DWH-Team | M3.4 |
| EMRGPT-P3-031 | Task | FHIR-Mapping für Labordaten (Observation-Ressource) implementieren | Major | Backend | KW09–KW13/2027 | – | M3.4 |
| EMRGPT-P3-032 | Task | Labordaten in GraphRAG integrieren | Major | Backend | KW13–KW17/2027 | P3-031 | M3.4 |

### Epic: EMRGPT-P3-ROLLOUT – Klinikweiter Rollout

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P3-040 | Story | Klinikweiter Rollout EMRGPT (Go/No-Go) | Blocker | PL | KW17–KW22/2027 | M3.1–M3.4 | M3.5 |
| EMRGPT-P3-041 | Task | Rollout-Plan für alle Klinikbereiche erstellen | Critical | PL | KW17–KW18/2027 | – | M3.5 |
| EMRGPT-P3-042 | Task | Champions-Netzwerk aktivieren (2 Champions pro Klinik) | Major | Fachbereich | KW18–KW20/2027 | P3-041 | M3.5 |
| EMRGPT-P3-043 | Task | Schulungsprogramm klinikweit durchführen | Major | Fachbereich | KW18–KW22/2027 | P3-042 | M3.5 |
| EMRGPT-P3-044 | Task | Evidence-Panel und SNOMED-Tags im Frontend aktivieren | Major | Frontend | KW17–KW20/2027 | M3.2a, M3.3a | M3.5 |
| EMRGPT-P3-045 | Task | Go-Live klinikweit und Hypercare-Phase (2 Wochen) | Blocker | PL | KW22/2027 | P3-041–P3-044 | M3.5 |

### Epic: EMRGPT-P3-CLOSE – Projektabschluss

| Ticket-ID | Typ | Titel | Priorität | Assignee | Sprint | Abhängigkeit | Meilenstein |
|-----------|-----|-------|-----------|----------|--------|-------------|-------------|
| EMRGPT-P3-050 | Story | Projektabschluss und Übergabe an Linienbetrieb | Major | PL | KW22–KW26/2027 | Betriebskonzept | M3.6 |
| EMRGPT-P3-051 | Task | Betriebshandbuch finalisieren und an IT-Betrieb übergeben | Major | IT-Arch | KW22–KW24/2027 | – | M3.6 |
| EMRGPT-P3-052 | Task | SLA-Vereinbarung mit IT-Betrieb abschließen | Major | PL, IT-Betrieb | KW23–KW25/2027 | P3-051 | M3.6 |
| EMRGPT-P3-053 | Task | Lessons Learned und Projektabschlussbericht | Major | PL | KW24–KW26/2027 | – | M3.6 |
| EMRGPT-P3-054 | Task | Formaler Projektabschluss durch Lenkungsausschuss | Major | Auftraggeber | KW26/2027 | P3-053 | M3.6 |

---

## Zusammenfassung

| Phase | Epics | Tickets | Zeitraum | Kritische Meilensteine |
|-------|-------|---------|----------|----------------------|
| Phase 0 | 1 | 20 | Feb – Jun 2026 | M0.4 (LA-Entscheidung), M0.5 (PL installiert) |
| Phase 1 | 6 | 29 | Mai – Sep 2026 | M1.4 (FHIR Go/No-Go), M1.6 (Plattform ready) |
| Phase 2 | 7 | 36 | Jul – Dez 2026 | M2.4 (MVP Go-Live Okt 2026 = SAP-Abschaltung) |
| Phase 3 | 6 | 31 | Q1 – Q2/2027 | M3.5 (Klinikweiter Rollout), M3.6 (Projektabschluss) |
| **Gesamt** | **20** | **116** | **Feb 2026 – Jun 2027** | **4 Go/No-Go-Entscheidungen** |
