# Präsentation Vorprojekt EMRGPT
## Entscheidungsgrundlage für den Lenkungsausschuss

**Universitätsklinikum Leipzig (UKL)**
**Stand: Februar 2026 | Vorprojekt-Abschluss**

---

## Folie 1: Titel und Agenda

# Vorprojekt EMRGPT – Ergebnisse und Entscheidungsgrundlage

### Agenda

1. Ausgangslage und Handlungsdruck
2. Ergebnisse des Vorprojekts
3. Technische Machbarkeit
4. Variantenvergleich mit Bewertung
5. Sicherheit, Datenschutz und Compliance
6. Kosten und Nutzen
7. Risiken und Maßnahmen
8. Umsetzungsfahrplan
9. Entscheidungsbedarf

---

## Folie 2: Ausgangslage

### Warum dieses Vorprojekt?

**Harter Fakt:** SAP i.s.h.med wird im **Oktober 2026** abgeschaltet.

| Aspekt | Situation |
|--------|-----------|
| **Altdaten** | 21 Mio. medizinische Dokumente im HYDMedia-Archiv |
| **Neues KIS** | M-KIS (Meierhofer) als einziges führendes System |
| **Archivzugriff** | HYDMedia Viewer als manuelle Recherche-Alternative |
| **Problem** | Ärzte benötigen 15–50 Min./Tag für Informationsrecherche |
| **Risiko** | Ohne Lösung werden Altdaten faktisch unzugänglich |

**Aufgabe des Vorprojekts:** Machbarkeit und Umsetzungsvariante für einen KI-gestützten Zugang zu den Altdaten klären.

---

## Folie 3: Methodik und Scope

### Wie wurde das Vorprojekt durchgeführt?

**Methodik:** PRINCE2-Produktstrukturplan (PSP) mit 39 definierten Produkten

**Abgedeckte Bereiche:**

| Bereich | PSP-Produkte | Status |
|---------|-------------|--------|
| 1. Projektorganisation | 6 Produkte (1.1–1.6) | 4 ERGÄNZT, 2 Teilweise |
| 2. Fachlich | 5 Produkte (2.1–2.3.1) | 3 Abgedeckt, 2 ERGÄNZT |
| 3. Technisch | 11 Produkte (3.1–3.9 inkl. 3.1.1, 3.3.1) | 4 Abgedeckt, 3 ERGÄNZT, 3 Teilweise, 1 Entfällt |
| 4. Sicherheit | 6 Produkte (4.1–4.6) | 3 ERGÄNZT, 2 Abgedeckt, 1 Teilweise |
| 5. Management Summary | 3 Produkte (5.1–5.3) | 1 ERGÄNZT, 2 Teilweise |
| 6. Abschlussdokumentation | 3 Produkte (6.1–6.3) | 2 ERGÄNZT, 1 OFFEN |
| 7. Ergänzungen | 5 Produkte (7.1–7.5) | 5 ERGÄNZT |

**Ergebnis:** 39 PSP-Produkte, davon 29 abgedeckt/ergänzt, 8 teilweise, 1 offen, 1 entfällt. Dokumentiert in Konzept_EMRGPT.md (22 Kapitel, ca. 3.500 Zeilen).

---

## Folie 4: Fachliche Ergebnisse

### Was soll EMRGPT leisten?

**4 definierte Use Cases:**

| UC | Beschreibung | Priorität |
|----|-------------|-----------|
| UC-1 | **Intelligente Dokumenten- und Befundrecherche** – Semantische Suche in natürlicher Sprache | MUSS |
| UC-2 | **Automatisierte Aktenzusammenfassung** – Chronologische, fachgebietsbezogene Übersichten | SOLL |
| UC-3 | **Qualitätssicherung und Dokumentations-Compliance** – Vollständigkeitsprüfung | KANN |
| UC-4 | **Evidence-Matching und SNOMED-Tagging** – Studienabgleich und automatische Codierung | SOLL |

**16 funktionale + 12 nicht-funktionale Anforderungen** spezifiziert (Kap. 0.10).

**Kritische MUSS-Anforderungen:**
- Semantische Suche über 21 Mio. Dokumente (FA-01)
- Quellenbasierte Antworten mit Dokumentverweis (FA-02)
- M-KIS-Integration (FA-08)
- Berechtigungsprüfung vor jedem Zugriff (NFA-03)
- On-Premise-Betrieb, keine externe Cloud (NFA-06)

---

## Folie 5: Technische Machbarkeit

### Architektur und Technologie-Stack

**Ergebnis: Technisch machbar mit RAG-Architektur (Retrieval-Augmented Generation)**

**Vier Wissensschichten:**

| Schicht | Funktion | Technologie |
|---------|----------|-------------|
| **Patienten-RAG** | Episodische On-Demand-Abfragen pro Patient | Vektor-DB + FHIR-Connector |
| **Dokumenten-RAG** | Volltextsuche über 21 Mio. OCR-PDFs | Vektor-DB (Milvus/Qdrant) |
| **GraphRAG** | Strukturierte Fakten (Diagnosen, Medikation, Labor) | Neo4j + FHIR/SNOMED |
| **Evidenz-Service** | Studien, Leitlinien, Europe PMC | API-Integration |

**Validierte Schnittstellen:**
- HYDMedia FHIR R4 (ISiK Stufe 3) – DocumentReference → Binary
- UKLytics/DWH für strukturierte Daten
- SAP IS-H/i.s.h.med Connectors (BAPI, HL7, FHIR, IHE)

---

## Folie 6: Dokumentenpipeline – Ist-Zustand

### Datenflüsse und Qualitätsprobleme

**Pipeline-Übersicht:**
```
Subsysteme → Cloverleaf → DMI Klassifizierung → HYDMedia → EMRGPT
(Copra, Medavis,  (HL7 MDM    (IHE + KDL)      (21 Mio.
 SAP, IDScorer,    Normalis.)                    PDFs auf
 Viewpoint, Scan)                                ISILON)
```

**Identifizierte Datenqualitätsprobleme (KRITISCH):**

| Problem | Auswirkung | Lösungsansatz |
|---------|-----------|---------------|
| Duplikate (3–5x) | Mehrfachfunde verfälschen Ergebnisse | Dedup-Logik, Hash-Vergleich |
| Verbucher nicht IHE-konform | Nicht durchsuchbar | Nachklassifizierung oder Ausschluss |
| OCR nur für computergenerierte Dokumente | Handschrift nicht erkannt | OCR-Installation Feb 2026 |
| Fehlende Labordaten | Keine Laborbefunde über HYDMedia | Separater FHIR-Connector UKLytics |
| SAP-DOK noch nicht migriert | 20 Jahre Altdaten fehlen | Migration gestartet KW7/2026 |

---

## Folie 7: Kritischer Befund – HYDMedia-Berechtigungslücke

### KRITISCH: Need-to-Know-Prinzip nicht umgesetzt

**Befund:**
- HYDMedia-Standardzugriff über SAP-Weiterleitung: Nur aktive Akten
- Erweiterter Zugriff über Citrix: **Zugriff auf ALLE Akten ALLER Patienten**
- AD-Gruppen existieren, aber NICHT in HYDMedia für Zugriffssteuerung hinterlegt

**Konsequenz für EMRGPT:**
- EMRGPT darf das HYDMedia-Berechtigungskonzept **NICHT** übernehmen
- Berechtigungshoheit **MUSS** aus M-KIS abgeleitet werden
- FHIR-Abfrage an HYDMedia erst nach erfolgreicher M-KIS-Berechtigungsprüfung

**Maßnahme:** Gatekeeper-Architektur mit M-KIS als Permission-Master (Kap. 12)

---

## Folie 8: Variantenvergleich

### Eigenlösung EMRGPT vs. Averbis/Meierhofer (Medical Summary)

| Kriterium | Gewicht | EMRGPT | Averbis |
|-----------|---------|--------|---------|
| Datenhoheit und Kontrolle | 20% | Hoch (On-Premise) | Gering (Vendor-abhängig) |
| Archivdaten-Integration | 20% | Vollständig (21 Mio. via RAG) | Eingeschränkt |
| Innovationstiefe | 15% | Hoch (GraphRAG, SNOMED, Evidence) | Mittel (Medical Summary) |
| Unabhängigkeit | 15% | Hoch (kein Vendor Lock-in) | Gering (Averbis + Meierhofer) |
| Betriebsaufwand | 10% | Höher (eigenes Team nötig) | Geringer (SaaS) |
| Initialkosten | 10% | Höher (Infrastruktur + Entwicklung) | Geringer |
| Time-to-Market | 10% | Moderat (MVP Okt 2026) | Schneller (aber eingeschränkt) |

**Bewertung Eigenlösung: Strategisch überlegen**
**Bewertung Averbis: Schneller verfügbar, aber eingeschränkt und abhängig**

---

## Folie 9: Risiken der Averbis-Variante

### Warum die Marktlösung strategisch nachteilig ist

1. **Vendor Lock-in:** Doppelte Abhängigkeit (Meierhofer + Averbis)
2. **Black Box KI-Pipeline:** Keine Kontrolle über Qualität und Verhalten des LLM
3. **Eingeschränkter Archivzugriff:** Nicht alle 21 Mio. Dokumente abdeckbar
4. **Keine SNOMED/GraphRAG-Integration:** Kein strukturierter Wissensgraph
5. **Fehlende Datenhoheit:** Patientendaten potenziell in Anbieter-Cloud
6. **Innovationsbegrenzung:** Eigene Weiterentwicklung nicht möglich

**Offene Punkte (noch zu klären):**
- Averbis-Angebot und Preismodell ausstehend
- Leistungsumfang Medical Summary für UKL-Spezifika
- Vertragliche Zusagen zu Datenhoheit und DSGVO

---

## Folie 10: Sicherheit und Compliance

### Umfassend konzipiert und dokumentiert

| Bereich | Status | Konzept-Kapitel |
|---------|--------|----------------|
| **DSGVO-Konformität** | Abgedeckt – Privacy by Design, episodische Verarbeitung, Zweckbindung | Kap. 13.1, 14.4 |
| **Berechtigungskonzept** | ERGÄNZT – SAP-Modell auf M-KIS gemappt, PSY/KJP-Schutz | Kap. 12, 12.1.1 |
| **Break-the-Glass** | Abgedeckt – Notfallzugriff mit Begründungspflicht | Kap. 12.4 |
| **KRITIS-Konformität** | ERGÄNZT – Schutzbedarfsanalyse, BSI-Anforderungen | Kap. 13.4 |
| **EU AI Act** | Abgedeckt – Transparenz, Risikomanagement, Aufsicht | Kap. 13.3 |
| **Incident-Response** | ERGÄNZT – Meldepflichten (DSGVO Art. 33/34, BSI), KI-spezifische Response | Kap. 19 |
| **Audit-Trail** | Abgedeckt – Revisionssichere Protokollierung | Kap. 12.6, 14.6 |

**Noch ausstehend:** Formale DSFA im Hauptprojekt durchzuführen.

---

## Folie 11: Kosten und Nutzen

### Business Case (Grobrahmen)

**Nutzenseite (quantifiziert):**
- 250 Arztstunden/Tag Einsparungspotenzial bei der Informationsrecherche
- Reduktion von Informationslücken und Doppelbefragungen
- Höhere Patientensicherheit durch vollständigere Datengrundlage

**Kostenseite (Template – noch zu befüllen):**

| Kostenblock | Eigenlösung | Averbis |
|-------------|------------|---------|
| GPU-Infrastruktur | Zu kalkulieren | Entfällt (Cloud) |
| LLM-Lizenzen/API | Zu kalkulieren | In Lizenz |
| Personal (Dev + Betrieb) | Zu kalkulieren | Gering |
| OCR-Verarbeitung | Zu kalkulieren | Nicht enthalten |
| Lizenz Averbis/Meierhofer | Entfällt | Angebot ausstehend |

**Preisreferenz hAIppokrates/GreenBay:** 1.000–2.500 EUR/Monat + 8.000 EUR Implementierung

**Handlungsbedarf:** Kostenseite muss bis April 2026 detailliert werden (IT-Sizing + Averbis-Angebot).

---

## Folie 12: Risikobewertung

### Top-Risiken des Hauptprojekts

| Risiko | Eintritt | Auswirkung | Maßnahme |
|--------|----------|-----------|----------|
| FHIR-Schnittstelle nicht performant | Mittel | Hoch – Kein Dokumentenzugriff | Fallback: ISILON-Direktzugriff, Go/No-Go M1.4 |
| MVP nicht rechtzeitig zur SAP-Abschaltung | Mittel | Hoch – Kein KI-Zugang | Fallback: HYDMedia Viewer (Ist-Zustand) |
| Berechtigungsmigration M-KIS verzögert | Mittel | Hoch – Kein Sicherheitskonzept | Temporäre Whitelist + Logging |
| OCR-Qualität unzureichend | Gering | Mittel – Eingeschränkte Suche | Beschränkung auf computergenerierte Dokumente |
| GPU-Beschaffung verzögert (Lieferzeiten) | Mittel | Hoch – Verzögerung aller Phasen | Frühzeitige Bestellung nach Budgetfreigabe |
| Akzeptanz klinisches Personal | Gering | Mittel – Geringe Nutzung | Champions-Netzwerk, Pilotierung, Schulung |
| Datenqualität (Duplikate, fehlende Daten) | Hoch | Mittel – Qualitätsprobleme | Dedup-Logik, Qualitäts-Monitoring |

**Risikostrategie:** Stufenweise Umsetzung mit 4 Go/No-Go-Entscheidungspunkten.

---

## Folie 13: Umsetzungsfahrplan

### 4 Phasen mit klaren Go/No-Go-Punkten

| Phase | Zeitraum | Ziel | Go/No-Go |
|-------|----------|------|----------|
| **Phase 0** | Feb – Jun 2026 | Vorprojekt abschließen, LA-Entscheidung, PL installieren | **M0.4:** LA-Entscheidung (Apr 2026) |
| **Phase 1** | Mai – Sep 2026 | GPU-Infra, SAP-DOK-Migration, FHIR-Validierung, Berechtigungen | **M1.4:** FHIR Go/No-Go (Jul 2026) |
| **Phase 2** | Jul – Dez 2026 | Dokumenten-RAG, MVP, Pilot auf 1 Station, Rollout auf 3 | **M2.4:** MVP Go-Live (Okt 2026) |
| **Phase 3** | Q1 – Q2/2027 | GraphRAG, SNOMED, Leitlinien, klinikweiter Rollout | **M3.5:** Vollbetrieb (Mai 2027) |

**Kritischer Pfad:**
```
SAP-DOK-Migration → FHIR validiert → Dokumenten-RAG → MVP Go-Live ← SAP OFF (Okt 2026)
                                           ↑
                              M-KIS-Berechtigungen
```

**27 Meilensteine, 116 YouTrack-Tickets, 20 Epics** (Detail: Projektplan.md)

---

## Folie 14: Kritische Abhängigkeiten

### Was muss klappen, damit es funktioniert?

| Abhängigkeit | Termin | Status | Risiko |
|-------------|--------|--------|--------|
| Dedalus FHIR-Zusage und Validierung | Jul 2026 | Offen | Hoch |
| SAP-DOK-Migration (20 Jahre) | Jun 2026 | Gestartet (KW7/2026) | Mittel |
| M-KIS Go-Live und Berechtigungshoheit | Aug 2026 | In Planung | Mittel |
| GPU-Infrastruktur Beschaffung | Jun 2026 | Noch nicht begonnen | Mittel |
| OCR-Installation und Validierung | Jul 2026 | Installation Feb 2026 | Gering |
| Averbis-Angebot für Vergleich | Mär 2026 | Ausstehend | Gering |

---

## Folie 15: Change-Management

### Klinische Einführung in 3 Phasen

**Phase A – Pilotstation (Okt–Nov 2026):**
- 1 Station, ca. 20 Nutzer
- Intensives Feedback und tägliches Monitoring
- Bug-Fixing und Anpassungen

**Phase B – Erweiterter Pilot (Dez 2026 – Feb 2027):**
- 3 weitere Stationen
- Champions-Netzwerk: 2 Ansprechpartner pro Klinik
- Strukturierte Feedback-Schleifen

**Phase C – Klinikweiter Rollout (ab Q2/2027):**
- Alle Klinikbereiche
- E-Learning + Präsenzschulungen
- Hypercare-Phase mit verstärktem Support

**Erfolgsmessung:** Nutzungsrate, Suchzeitersparnis, Nutzerzufriedenheit, Fehlerrate

---

## Folie 16: Kommunikationsplan

### Strukturierte Projektsteuerung

| Maßnahme | Zielgruppe | Format | Frequenz |
|----------|-----------|--------|----------|
| Lenkungsausschuss-Bericht | Vorstand | Entscheidungsvorlage | Monatlich |
| Projekt-Statusbericht | IT-Leitung, Auftraggeber | Ampellogik | 2-wöchentlich |
| Technisches Jour fixe | IT-Architektur, Entwicklung | Arbeitsbesprechung | Wöchentlich |
| Fachbereich-Abstimmung | Ärztlicher Direktor, Medizin | Workshop | Monatlich |
| Datenschutz/Sicherheits-Review | DSB, ISB | Review-Meeting | Bei Meilensteinen |
| Externe Partner-Abstimmung | Meierhofer, Dedalus | Jour fixe | Monatlich |
| Change-Management-Info | Klinisches Personal | Newsletter | Quartalsweise |

**Eskalationswege:** PL → Auftraggeber → Lenkungsausschuss → Vorstand

---

## Folie 17: Entscheidungsbedarf

### Drei Entscheidungen werden erbeten

#### Entscheidung 1: Umsetzungsvariante
| Option | Beschreibung |
|--------|-------------|
| **A: Eigenlösung EMRGPT** (empfohlen) | KI-Informationsassistent mit RAG-Architektur, On-Premise, volle Kontrolle |
| **B: Averbis/Meierhofer** | Medical Summary im M-KIS, SaaS/Cloud, Vendor-abhängig |
| **C: Keine Umsetzung** | Altdaten nur über manuellen HYDMedia Viewer zugänglich |

#### Entscheidung 2: Ressourcenfreigabe
- Budget für GPU-Infrastruktur, Lizenzen, Personal
- Konkretisierung nach Kostengerüst (Kap. 20, bis April 2026)

#### Entscheidung 3: Projektleiter installieren
- PM-Exzellenz als erklärtes Projektziel
- Mandat für operative Steuerung des Umsetzungsprojekts

---

## Folie 18: Konsequenzen der Optionen

### Was passiert bei welcher Entscheidung?

| Szenario | Konsequenz |
|----------|-----------|
| **Eigenlösung EMRGPT genehmigt** | MVP zu SAP-Abschaltung (Okt 2026), Vollbetrieb Q2/2027, strategische KI-Readiness |
| **Averbis/Meierhofer genehmigt** | Schnellere Teillösung, aber eingeschränkter Funktionsumfang, Vendor Lock-in, keine Archivdaten-Integration |
| **Keine Entscheidung / Verschiebung** | Altdaten nach SAP-Abschaltung nur manuell zugänglich, Effizienzgewinne nicht realisiert, strategischer Nachteil |
| **Entscheidung verzögert sich > Apr 2026** | MVP-Termin Okt 2026 gefährdet, Infrastruktur-Vorlauf von 8–12 Wochen kann nicht eingehalten werden |

---

## Folie 19: Empfehlung des Vorprojekts

### Klare Empfehlung für Eigenlösung

**Die Eigenlösung EMRGPT bietet:**
- Signifikant höhere Datenhoheit und Unabhängigkeit
- Zugang zu allen 21 Mio. Archivdokumenten
- Volle Kontrolle über KI-Pipeline und Datenverarbeitung
- Innovationstiefe (GraphRAG, SNOMED, Evidence-Matching)
- DSGVO-Konformität durch On-Premise-Betrieb
- Strategische KI-Readiness für das UKL

**Empfohlenes Vorgehen:**
1. Eigenlösung EMRGPT mit MVP-Ansatz genehmigen
2. Budget und Infrastruktur freigeben
3. Projektleiter mit PM-Exzellenz schnellstmöglich installieren
4. Parallel: Averbis-Angebot als Vergleichsbasis einholen

---

## Folie 20: Nächste Schritte

### Sofortmaßnahmen nach LA-Entscheidung

| Nr | Maßnahme | Verantwortlich | Frist |
|----|----------|---------------|-------|
| 1 | LA-Entscheidung herbeiführen | PM | Apr 2026 |
| 2 | Projektleiter installieren | Auftraggeber | Mai 2026 |
| 3 | GPU-Infrastruktur bestellen | IT-Infra | Mai 2026 |
| 4 | Averbis-Angebot einholen (parallel) | PM | Mär 2026 |
| 5 | Fachliche Anforderungen mit Fachbereich abstimmen | Fachbereich | Mär 2026 |
| 6 | Kostengerüst mit Controlling befüllen | Controlling | Apr 2026 |
| 7 | FHIR-Testumgebung aufsetzen | IT-Architektur | Jun 2026 |
| 8 | DSFA-Vorprüfung anstoßen | DSB | Q2 2026 |

**Vollständige Dokumentation:**
- Konzept_EMRGPT.md (22 Kapitel, Zielarchitektur)
- PSP_EMRGPT.md (Produktstrukturplan, PRINCE2)
- Projektplan.md (116 Tickets, 4 Phasen)
- Projektplan_Gantt.csv (Gantt-Chart für Excel)
