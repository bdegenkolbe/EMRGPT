# Produktstrukturplan (PSP) EMRGPT – Vorprojekt

**Version:** 2.0 | **Stand:** 2026-02-27 | **Methodik:** PRINCE2
**Referenzdokument:** [Konzept_EMRGPT.md](Konzept_EMRGPT.md) (Zielarchitektur v2.0)

---

## Inhaltsverzeichnis

1. [Projektorganisation](#1-projektorganisation)
2. [Fachlich](#2-fachlich)
3. [Technisch](#3-technisch)
4. [Rechtebewertung und Sicherheit](#4-rechtebewertung-und-sicherheit)
5. [Management Summary](#5-management-summary)
6. [Abschlussdokumentation](#6-abschlussdokumentation)
7. [Ergänzende Produkte](#7-ergänzende-produkte)

---

## Gesamtübersicht PSP-Produkte

| PSP-Nr | PSP-Produkt | Konzept-Kapitel | Status | Verantwortlich |
|--------|-------------|-----------------|--------|----------------|
| 1.1 | Projektauftrag Vorprojekt | Kap. 0 (Management Summary) | Teilweise | Auftraggeber |
| 1.2 | Projektorganisation | Kap. 0.3, Kap. 0.9 (RACI) | ERGÄNZT | Projektmanager |
| 1.3 | Stakeholderanalyse | Kap. 0.4 | ERGÄNZT | Projektmanager |
| 1.4 | Kommunikationsplan | Kap. 0.8 | ERGÄNZT | Projektmanager |
| 1.5 | Vorläufiger Business Case | Kap. 0.5, Kap. 20 (Kostengerüst) | ERGÄNZT | Auftraggeber |
| 1.6 | Risiko- und Chancenliste | Kap. 1.4 + QUALITAETSANALYSE.md | Teilweise | Projektmanager |
| 2.1 | Zielbild EMRGPT | Kap. 1, 2, 3.1 | Abgedeckt | PM, Carina, Gert, Robert W. |
| 2.2 | Use-Case-Beschreibung LLM-Anbindung | Kap. 3.3 + Use Case Beschreibung 02.docx | Abgedeckt | Fachbereich |
| 2.2.1 | Kostenanalyse | Kap. 0.5, Kap. 20 (Kostengerüst) | ERGÄNZT | PMO / Controlling |
| 2.3 | Fachliche Anforderungen | Kap. 3.2, 3.3, Kap. 0.10 | ERGÄNZT | Fachbereich |
| 2.3.1 | Daten aus UKLytics | Kap. 8 (Datenzufluss DWH→GraphRAG) | Abgedeckt | IT |
| 3.1 | Technische Zielarchitektur | Kap. 4–12, Kap. 0.6 | Umfassend | IT-Architektur |
| 3.1.1 | Infrastruktur | Kap. 7, 8, Kap. 0.7 | Teilweise | IT-Infrastruktur |
| 3.2 | Marktanalyse | Kap. 16 (Variantenvergleich) | ERGÄNZT | PM, 4K |
| 3.3 | Analyse HYDMedia | Kap. 2.4, 3.2.6 | Abgedeckt | Valentin |
| 3.3.1 | Schnittstellenbeschreibung FHIR | Kap. 3.2.6.2, Kap. 0.6 | ERGÄNZT | Schnittstellenverantwortlicher |
| 3.4 | Analyse DMI Lösung | Kap. 2.1 | Teilweise | Valentin, Carina |
| ~~3.5~~ | ~~Vergleich HYDMedia vs. DMI~~ | – | ENTFÄLLT | – |
| 3.6 | Schnittstellenübersicht | Kap. 8, 10 | Abgedeckt | IT-Architektur, Valentin |
| 3.7 | Technisches Vorgehensmodell | Kap. 5, 6, 9 | Abgedeckt | IT-Architektur, 4K |
| 3.8 | Zugriff auf ISILON | Kap. 3.2.6.1 | Teilweise | IT-Infrastruktur |
| 3.9 | KIS-Dokumentenzugriff (Meierhofer) | Kap. 16 | ERGÄNZT | Robert W., Carina, Valentin |
| 4.1 | Datenschutzkonzept | Kap. 13.1 | Abgedeckt | DSB (Hr. Sünkel) |
| 4.2 | DSFA (Vorprüfung) | Kap. 13.1 | Teilweise | DSB (Hr. Sünkel) |
| 4.3 | Informationssicherheitsbewertung | Kap. 12, 13.4, Kap. 19 | ERGÄNZT | ISB (S. Krause) |
| 4.4 | Berechtigungskonzept | Kap. 12, Kap. 12.1.1 | ERGÄNZT | M. Schmeißer, Fr. Stallmach, Fr. Schmidt-Morich |
| 4.5 | SAP-Berechtigungsanalyse | Kap. 12.1, Kap. 12.1.1, Kap. 0.6 | ERGÄNZT | M. Schmeißer, Fr. Stallmach, Fr. Schmidt-Morich |
| 4.6 | Logging-/Nachvollziehbarkeitskonzept | Kap. 12.6 | Abgedeckt | IT-Sicherheit, PM |
| 5.1 | Entscheidungsgrundlage Datenhaltung | Kap. 2 | Teilweise | PM, Carina |
| 5.2 | Entscheidungsgrundlage LLM-Anbindung | Kap. 5, 6, 7, 16 | Teilweise | IT-Architektur, Carina, PM |
| 5.3 | Management-Entscheidungsvorlage | Kap. 0 | ERGÄNZT | PM |
| 6.1 | Empfehlung für Hauptprojekt | Kap. 0, 16.4 | ERGÄNZT | PM |
| 6.2 | Grober Umsetzungsfahrplan | Kap. 17 | ERGÄNZT | PM |
| 6.3 | Abnahmedokument Vorprojekt | – | OFFEN | Auftraggeber |
| 7.1 | Betriebskonzept (Gerüst) | Kap. 18 | ERGÄNZT | IT-Betrieb |
| 7.2 | Incident-Response-Plan | Kap. 19 | ERGÄNZT | ISB / DSB |
| 7.3 | Kostengerüst-Template | Kap. 20 | ERGÄNZT | PMO / Controlling |
| 7.4 | Change-Management-Konzept | Kap. 21 | ERGÄNZT | Fachbereich / PMO |
| 7.5 | SAP IS-H/i.s.h.med KI-Konnektor | Kap. 22 | ERGÄNZT | IT-Architektur |

**Legende:** ERGÄNZT = in Konzept-Dokument ausgearbeitet | OFFEN = noch zu erstellen | Teilweise = Grundlage vorhanden, Ergänzung nötig | ~~Durchgestrichen~~ = entfällt

---

## 1. Projektorganisation

### 1.1 Projektauftrag Vorprojekt

**Zweck:** Der Projektauftrag legitimiert das Vorprojekt EMRGPT formal und schafft eine verbindliche Grundlage für alle Beteiligten. Er beschreibt die Zielsetzung der Anbindung eines LLM an die Datenhaltungsebene auf strategischer Ebene. Zudem grenzt er das Vorprojekt klar vom möglichen Hauptprojekt ab. Der Projektauftrag definiert den Nutzen für die Organisation und stellt den Bezug zur Digitalisierungsstrategie her.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Ziele, Scope, Nicht-Ziele, Budgetrahmen, Zeitrahmen, Auftraggeber |
| **Qualitätskriterien** | Vollständig, genehmigt, verständlich |
| **Abnahmekriterien** | Schriftliche Freigabe durch Auftraggeber |
| **Verantwortlich** | Auftraggeber |
| **Konzept-Referenz** | Kap. 0 – Management Summary und Entscheidungsbedarf |
| **Status** | Teilweise – Separater Projektauftrag erforderlich |

### 1.2 Projektorganisation

**Zweck:** Die Projektorganisation stellt sicher, dass alle Rollen, Verantwortlichkeiten und Entscheidungswege klar definiert sind. Sie ermöglicht eine strukturierte Zusammenarbeit zwischen IT, Fachbereich, Datenschutz und Informationssicherheit. Durch klare Rollenzuordnung werden Doppelarbeiten und Unklarheiten vermieden.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Rollenbeschreibung, Organigramm, Vertretungsregelung |
| **Qualitätskriterien** | Vollständig, nachvollziehbar |
| **Abnahmekriterien** | Bestätigung durch Projektleitung |
| **Verantwortlich** | Projektmanager |
| **Konzept-Referenz** | Kap. 0.3 (Projektorganisation), Kap. 0.9 (RACI-Matrix) |
| **Status** | ERGÄNZT – inkl. RACI-Matrix mit allen PSP-Produkten |

**Rollen im Projekt (aus Konzept Kap. 0.3):**

| Rolle | Person/Bereich |
|-------|---------------|
| Auftraggeber | [zu benennen] |
| Projektleiter | [PM-Exzellenz erforderlich – zu installieren] |
| IT-Architektur | Gert, Carina, Valentin |
| Fachbereich Medizin | Felix, Martin Neef, Niko v.D. |
| KIS-Verantwortlicher | Robert W. |
| Datenschutz | Hr. Sünkel |
| Informationssicherheit | S. Krause |
| Berechtigungen | M. Schmeißer, Fr. Stallmach, Fr. Schmidt-Morich |

### 1.3 Stakeholderanalyse

**Zweck:** Die Stakeholderanalyse identifiziert alle Personen und Organisationen, die Einfluss auf das Vorprojekt haben oder davon betroffen sind. Sie bewertet deren Interessen, Erwartungen und Einflussmöglichkeiten. Dadurch können Risiken frühzeitig erkannt und adressiert werden.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Stakeholderliste, Einfluss-/Interessenmatrix |
| **Qualitätskriterien** | Vollständig, aktuell |
| **Abnahmekriterien** | Freigabe durch Lenkungsausschuss |
| **Verantwortlich** | Projektmanager |
| **Konzept-Referenz** | Kap. 0.4 – Stakeholder-Übersicht |
| **Status** | ERGÄNZT – 12 Stakeholder-Gruppen identifiziert und bewertet |

### 1.4 Kommunikationsplan

**Zweck:** Der Kommunikationsplan legt fest, wie, wann und mit wem im Projekt kommuniziert wird. Er sorgt für Transparenz und verhindert Informationsdefizite. Unterschiedliche Informationsbedarfe der Stakeholder werden berücksichtigt.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Kommunikationsmatrix (7 Maßnahmen), Termine, Formate |
| **Qualitätskriterien** | Klar, realistisch |
| **Abnahmekriterien** | Zustimmung der Projektleitung |
| **Verantwortlich** | Projektmanager |
| **Konzept-Referenz** | Kap. 0.8 – Kommunikationsplan mit Eskalationswegen |
| **Status** | ERGÄNZT – LA-Bericht, Statusbericht, Tech-Jour-fixe, Fachbereich-Abstimmung, DS/IS-Review, Externe Partner, Change-Info |

### 1.5 Vorläufiger Business Case

**Zweck:** Der vorläufige Business Case bewertet den strategischen und wirtschaftlichen Nutzen von EMRGPT. Er stellt Vergleichsdaten (Kosten, Nutzen, qualitative Mehrwerte) gegenüber. Risiken und Annahmen werden transparent dokumentiert.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Nutzenargumentation, Kostenabschätzung, Risiken |
| **Qualitätskriterien** | Plausibel, nachvollziehbar |
| **Abnahmekriterien** | Genehmigung durch Lenkungsausschuss |
| **Verantwortlich** | Auftraggeber |
| **Konzept-Referenz** | Kap. 0.5 (Business Case), Kap. 20 (Kostengerüst-Template) |
| **Status** | ERGÄNZT – Nutzen quantifiziert (250 Arztstunden/Tag Einsparungspotenzial), Kostengerüst-Template vorhanden, konkrete Werte durch Controlling zu befüllen |

**Kernkennzahlen:**
- Suchanfragen pro Arzt/Tag: 2–5 (ambulant), 3–5 (stationär)
- Zeitersparnis pro Anfrage: von 7,5 Min. auf ca. 10 Sek.
- Hochrechnung UKL: ca. 250 Arztstunden/Tag eingesparte Recherchezeit

### 1.6 Risiko- und Chancenliste

**Zweck:** Die Risiko- und Chancenliste erfasst systematisch alle identifizierten Projektrisiken und -chancen. Sie ermöglicht eine strukturierte Bewertung hinsichtlich Eintrittswahrscheinlichkeit und Auswirkung. Maßnahmen zur Risikominimierung werden definiert.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Risiko-ID, Beschreibung, Bewertung, Maßnahme |
| **Qualitätskriterien** | Vollständig, aktuell |
| **Abnahmekriterien** | Kenntnisnahme durch Projektleitung |
| **Verantwortlich** | Projektmanager |
| **Konzept-Referenz** | Kap. 1.4 (Kritische Erfolgsfaktoren), QUALITAETSANALYSE.md (Risiko-Register) |
| **Status** | Teilweise – Risiken im Konzept identifiziert, formale Risikobewertung mit Eintrittswahrscheinlichkeiten noch zu erstellen |

---

## 2. Fachlich

### 2.1 Zielbild EMRGPT

**Zweck:** Das Zielbild EMRGPT beschreibt die angestrebte ganzheitliche Lösung aus fachlicher und technischer Perspektive. Es vermittelt eine gemeinsame Vision für alle Beteiligten und ordnet EMRGPT in die bestehende Systemlandschaft ein.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Vision, Nutzen, Architektur-Skizze |
| **Qualitätskriterien** | Verständlich, konsistent |
| **Abnahmekriterien** | Zustimmung des Auftraggebers |
| **Verantwortlich** | PM, Carina, Gert, Robert W. |
| **Konzept-Referenz** | Kap. 1 (Zielbeschreibung), Kap. 2 (Nutzen/Innovation), Kap. 3.1 (Klinischer Informationsassistent) |
| **Status** | Abgedeckt – Vision, Nutzen, Innovation (6 Innovationsaspekte), Anwendungsszenarien dokumentiert |

**Kerninhalte aus dem Konzept:**
- Legacy Data Bridge: Konsolidiertes Dokumentenarchiv für 21 Mio. Altdokumente
- Vier Wissensdomänen: Patienten-RAG, Dokumenten-RAG, GraphRAG, Evidenz-/Studien-Service
- FHIR-konformer klinischer Graph mit SNOMED-CT-Normalisierung
- Episodisches Patienten-RAG mit Zweckbindung (Privacy by Design)

### 2.2 Use-Case-Beschreibung LLM-Anbindung

**Zweck:** Die Use-Case-Beschreibung konkretisiert den praktischen Einsatz von EMRGPT im klinischen Alltag. Sie beschreibt, wie das LLM auf Patientendokumente zugreift und Mehrwert erzeugt.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Akteure, Ablauf, Datenquellen, Nutzen |
| **Qualitätskriterien** | Praxisnah, eindeutig |
| **Abnahmekriterien** | Freigabe durch Fachbereich |
| **Verantwortlich** | Fachbereich (Felix, Carina, Martin Neef, Niko v.D.) |
| **Konzept-Referenz** | Kap. 3.3 (Use Cases 1–4), Use Case Beschreibung 02.docx |
| **Status** | Abgedeckt – 4 Use Cases definiert |

**Definierte Use Cases:**
1. **UC-1:** Intelligente Dokumenten- und Befundrecherche (Kap. 3.3.1)
2. **UC-2:** Automatisierte Zusammenfassung von Patientenakten (Kap. 3.3.2)
3. **UC-3:** Unterstützung Qualitätssicherung und Dokumentations-Compliance (Kap. 3.3.3)
4. **UC-4:** Automatisches Evidence-Matching und SNOMED-Tagging (Kap. 3.3.4)

#### 2.2.1 Kostenanalyse

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | CAPEX/OPEX-Struktur, TCO-Vergleich Eigenlösung vs. Averbis |
| **Verantwortlich** | PMO / Controlling |
| **Konzept-Referenz** | Kap. 0.5 (Business Case), Kap. 0.7 (Preisreferenz hAIppokrates), Kap. 20 (Kostengerüst-Template) |
| **Status** | ERGÄNZT – Template vorhanden, Werte durch IT/Controlling zu befüllen |

### 2.3 Fachliche Anforderungen

**Zweck:** Die fachlichen Anforderungen beschreiben, welche Informationen und Funktionen das LLM bereitstellen soll. Sie stellen sicher, dass medizinische, administrative und rechtliche Bedürfnisse berücksichtigt werden.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | 16 funktionale Anforderungen (FA-01 bis FA-16), 12 nicht-funktionale Anforderungen (NFA-01 bis NFA-12) |
| **Qualitätskriterien** | Vollständig, verständlich |
| **Abnahmekriterien** | Freigabe Fachbereich |
| **Verantwortlich** | Fachbereich (Carina, Niko v.D., Martin Neef) |
| **Konzept-Referenz** | Kap. 0.10 (Anforderungsliste), Kap. 3.2, 3.3 |
| **Status** | ERGÄNZT – Entwurf vorhanden, Abstimmung mit Fachbereich erforderlich |

**Kritische Anforderungen (MUSS):**
- FA-01: Semantische Suche über 21 Mio. Dokumente
- FA-02: Quellenbasierte Antworten
- FA-08: M-KIS-Integration
- FA-09: GraphRAG-Faktenabfrage
- NFA-03: Berechtigungsprüfung vor jedem Datenzugriff
- NFA-06: On-Premise-Betrieb

#### 2.3.1 Daten aus UKLytics

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | IT |
| **Konzept-Referenz** | Kap. 8 (Datenzufluss DWH→GraphRAG) |
| **Status** | Abgedeckt – DWH als Quelle für strukturierte Fakten (Diagnosen, Medikation, Labor) |

---

## 3. Technisch

### 3.1 Technische Zielarchitektur

**Zweck:** Die technische Zielarchitektur beschreibt die angestrebte Systemlandschaft für EMRGPT auf hoher Ebene. Sie zeigt das Zusammenspiel von LLM, Datenhaltung, Schnittstellen und Sicherheit.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Architekturdiagramm, Schichtenbeschreibung (6 Schichten) |
| **Qualitätskriterien** | Konsistent, nachvollziehbar |
| **Abnahmekriterien** | Freigabe IT-Architektur |
| **Verantwortlich** | IT-Architektur (Gert, Carina) |
| **Konzept-Referenz** | Kap. 4 (Frontend/UI), 5 (Orchestrierungsschicht), 6 (Prompt-Pipeline), 7 (Datenschicht), 8–10 (Schnittstellen), 15 (Gesamtarchitektur) |
| **Status** | Umfassend – inkl. Dokumentenpipeline und Datenqualitätsanalyse |

**Architekturschichten:**
1. Frontend / UI (Präsentationsschicht) – Kap. 4
2. Applikations- und Orchestrierungsschicht – Kap. 5
3. Qualitätssicherung (Prompt-Pipeline) – Kap. 6
4. Datenschicht (Vier RAG-Domänen) – Kap. 7
5. Schnittstellen (Integrationsschicht) – Kap. 8–10
6. Berechtigungs- und Sicherheitskonzept – Kap. 12

#### 3.1.1 Infrastruktur

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | IT-Infrastruktur |
| **Konzept-Referenz** | Kap. 7 (Datenschicht), Kap. 8 (DWH-Anbindung), Kap. 0.7 (Preisreferenz), Kap. 18.5 (Kapazitätsplanung) |
| **Status** | Teilweise – Sizing und konkrete Kosten offen, Preisreferenz hAIppokrates ergänzt |

### 3.2 Marktanalyse

**Zweck:** Strukturierter Vergleich zwischen Eigenlösung EMRGPT und Marktlösung Averbis/Meierhofer.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Variantenvergleich, Bewertungsmatrix (gewichtet) |
| **Verantwortlich** | PM, 4K |
| **Konzept-Referenz** | Kap. 16 (Variantenvergleich), Kap. 16.3 (Bewertungsmatrix), Kap. 16.4 (Empfehlung) |
| **Status** | ERGÄNZT – Empfehlung: Eigenlösung mit MVP-Ansatz |

### 3.3 Analyse HYDMedia

**Zweck:** Analyse der bestehenden Lösung im Hinblick auf LLM-Anbindung.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Systembeschreibung, Schnittstellen, Bewertung |
| **Qualitätskriterien** | Technisch korrekt, vollständig |
| **Abnahmekriterien** | Bestätigung durch IT |
| **Verantwortlich** | Valentin |
| **Konzept-Referenz** | Kap. 2.4 (PDF-Archivierung), Kap. 3.2.6 (HYDMedia-Analyse), Kap. 0.6 (Dokumentenpipeline) |
| **Status** | Abgedeckt – inkl. KRITISCHER Befund: HYDMedia-Berechtigungslücke (Need-to-Know nicht umgesetzt) |

#### 3.3.1 Schnittstellenbeschreibung FHIR

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | FHIR-Ressourcen (Patient, Encounter, DocumentReference, Binary), ISiK Stufe 3 |
| **Verantwortlich** | Schnittstellenverantwortlicher |
| **Konzept-Referenz** | Kap. 3.2.6.2 (FHIR-Schnittstelle), Kap. 0.6 (Conformance Statement) |
| **Status** | ERGÄNZT – FHIR R4, ISiK Stufe 3, DocumentReference→Binary als zentraler Pfad |

### 3.4 Analyse DMI Lösung

**Zweck:** Analyse der DMI-Lösung (AVP Infinity) zur Datenhaltung und Dokumentenklassifizierung.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Systemübersicht, Architektur, Bewertung |
| **Verantwortlich** | Valentin, Carina |
| **Konzept-Referenz** | Kap. 2.1 (Archivsystem), Kap. 0.6 (Dokumentenpipeline – DMI-Klassifizierung) |
| **Status** | Teilweise – Dokumentenpipeline über DMI beschrieben, Detailanalyse noch ausstehend |

### ~~3.5 Vergleich HYDMedia vs. DMI~~

**Status:** ENTFÄLLT – ersetzt durch Variantenvergleich EMRGPT vs. Averbis/Meierhofer (Kap. 16)

### 3.6 Schnittstellenübersicht

**Zweck:** Identifikation aller relevanten technischen Schnittstellen im Zielbild.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Übersichtsgrafik, Schnittstellenliste |
| **Verantwortlich** | IT-Architektur, Valentin |
| **Konzept-Referenz** | Kap. 8 (DWH-Anbindung), Kap. 10 (FHIR-Connector) |
| **Status** | Abgedeckt – Datenflüsse und Systemintegration dokumentiert |

### 3.7 Technisches Vorgehensmodell

**Zweck:** Beschreibung möglicher Integrationsansätze für das LLM (RAG, Middleware, API).

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Variantenbeschreibung, Bewertung |
| **Verantwortlich** | IT-Architektur, 4K |
| **Konzept-Referenz** | Kap. 5 (Orchestrierungsschicht), Kap. 6 (Prompt-Pipeline), Kap. 9 (LLM-Integration) |
| **Status** | Abgedeckt – RAG-Architektur mit vier Wissensdomänen gewählt |

### 3.8 Zugriff auf ISILON

**Zweck:** Analyse der technischen Bereitstellung von Patientendokumenten auf ISILON.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Analysebericht |
| **Verantwortlich** | IT-Infrastruktur – Carina fragt Daniel |
| **Konzept-Referenz** | Kap. 3.2.6.1 (ISILON-Zugriff) |
| **Status** | Teilweise – 21 Mio. PDFs auf ISILON dokumentiert, Performance-/Sicherheitsanalyse noch ausstehend |

### 3.9 KIS-Dokumentenzugriff (Meierhofer)

**Zweck:** Dokumentation der Zugriffsmöglichkeiten auf Dokumente im neuen M-KIS.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Schnittstellenbeschreibung, Nutzungsszenarien |
| **Verantwortlich** | Robert W., Carina, Valentin |
| **Konzept-Referenz** | Kap. 16 (Variantenvergleich inkl. M-KIS-Integration) |
| **Status** | ERGÄNZT – Meierhofer/Averbis-Integration bewertet |

---

## 4. Rechtebewertung und Sicherheit

### 4.1 Datenschutzkonzept

**Zweck:** Rechtskonformer Umgang mit Patientendaten unter Berücksichtigung von DSGVO, Zweckbindung und Datenminimierung.

| Attribut | Beschreibung |
|----------|-------------|
| **Zusammensetzung** | Datenschutzanalyse, Maßnahmen |
| **Qualitätskriterien** | DSGVO-konform |
| **Verantwortlich** | DSB (Hr. Sünkel) |
| **Konzept-Referenz** | Kap. 13.1 (DSGVO), Kap. 14.4 (Episodische Datenverarbeitung), Kap. 14.5 (Least Privilege) |
| **Status** | Abgedeckt – Privacy by Design, episodische Verarbeitung mit TTL, Zweckbindung dokumentiert |

### 4.2 Datenschutz-Folgenabschätzung (Vorprüfung)

**Zweck:** Vorprüfung, ob eine formale DSFA erforderlich ist.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | DSB (Hr. Sünkel) |
| **Konzept-Referenz** | Kap. 13.1 |
| **Status** | Teilweise – Vorprüfung empfohlen, formale DSFA im Hauptprojekt durchzuführen |

### 4.3 Informationssicherheitsbewertung

**Zweck:** Analyse von Schutzbedarf und Risiken bezüglich Verfügbarkeit, Vertraulichkeit und Integrität.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | ISB (S. Krause) |
| **Konzept-Referenz** | Kap. 12 (Sicherheitsarchitektur), Kap. 13.4 (KRITIS), Kap. 19 (Incident-Response) |
| **Status** | ERGÄNZT – Schutzbedarfsanalyse, KRITIS-Konformität, Incident-Response-Plan mit Meldepflichten |

### 4.4 Berechtigungskonzept

**Zweck:** Definition, wer welche Daten über das LLM einsehen darf, inkl. Rollen, Fachbereiche und Zugriffsszenarien.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | M. Schmeißer, Fr. Stallmach, Fr. Schmidt-Morich |
| **Konzept-Referenz** | Kap. 12 (Sicherheitskonzept), Kap. 12.1.1 (SAP-Berechtigungsmodell), Kap. 12.3.3 (PSY/KJP-Schutz), Kap. 12.4 (Break-the-Glass) |
| **Status** | ERGÄNZT – SAP-Modell detailliert gemappt (BA-Typen, SBG, OE-Schutz PSY/KJP) |

### 4.5 SAP-Berechtigungsanalyse

**Zweck:** Untersuchung bestehender SAP-Rollen und -Berechtigungen zur Ableitung für EMRGPT.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | M. Schmeißer, Fr. Stallmach, Fr. Schmidt-Morich |
| **Konzept-Referenz** | Kap. 12.1 (SAP-Berechtigungen), Kap. 12.1.1 (Detailanalyse), Kap. 0.6 (HYDMedia-Lücke), Kap. 22.5 (Berechtigungsmigration) |
| **Status** | ERGÄNZT – Migration der Berechtigungshoheit auf M-KIS dokumentiert, HYDMedia Need-to-Know-Lücke als KRITISCH identifiziert |

### 4.6 Logging- und Nachvollziehbarkeitskonzept

**Zweck:** Protokollierung aller Zugriffe und LLM-Anfragen für Compliance und Audit.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | IT-Sicherheit, PM |
| **Konzept-Referenz** | Kap. 12.6 (Audit-Trail), Kap. 14.6 (Governance) |
| **Status** | Abgedeckt – Revisionssicherer Audit-Trail für alle Abfragen und Zugriffe konzipiert |

---

## 5. Management Summary

### 5.1 Entscheidungsgrundlage Datenhaltung

**Zweck:** Strukturierte Vorbereitung der Datenhaltungsentscheidung (FHIR-Archiv, Vektor-DB, Graph-DB, Hybrid).

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | PM, Carina |
| **Konzept-Referenz** | Kap. 2 (Nutzen und Innovation), Kap. 2.5 (Hybride Strategie) |
| **Status** | Teilweise – Hybride Strategie empfohlen, Detailentscheidung durch Hauptprojekt |

### 5.2 Entscheidungsgrundlage LLM-Anbindung

**Zweck:** Bewertung verschiedener Varianten der LLM-Anbindung.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | IT-Architektur, Carina, PM |
| **Konzept-Referenz** | Kap. 5 (Orchestrierung), Kap. 6 (Prompt-Pipeline), Kap. 7 (Datenschicht), Kap. 16 (Variantenvergleich) |
| **Status** | Teilweise – RAG-Architektur favorisiert, Variantenvergleich durchgeführt |

### 5.3 Management-Entscheidungsvorlage

**Zweck:** Zusammenfassung aller Vorprojekt-Ergebnisse als Entscheidungsgrundlage.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | PM |
| **Konzept-Referenz** | Kap. 0 (Management Summary und Entscheidungsbedarf) |
| **Status** | ERGÄNZT – Drei Entscheidungspunkte formuliert: Umsetzungsvariante, Ressourcenfreigabe, Projektleiter-Installation |

---

## 6. Abschlussdokumentation

### 6.1 Empfehlung für Hauptprojekt

**Zweck:** Klare Handlungsempfehlung auf Basis aller Vorprojekt-Erkenntnisse.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | PM |
| **Konzept-Referenz** | Kap. 0 (Empfehlung), Kap. 16.4 (Variantenempfehlung) |
| **Status** | ERGÄNZT – Empfehlung: Eigenlösung EMRGPT mit MVP-Ansatz und stufenweiser Umsetzung |

### 6.2 Grober Umsetzungsfahrplan

**Zweck:** Phasenplan mit Meilensteinen und Abhängigkeiten für das Hauptprojekt.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | PM |
| **Konzept-Referenz** | Kap. 17 (Umsetzungsfahrplan – 4 Phasen, 27 Meilensteine) |
| **Status** | ERGÄNZT – Phase 0 bis Phase 3 (Feb 2026 – Jun 2027), kritischer Pfad und Rollback-Strategie dokumentiert |

### 6.3 Abnahmedokument Vorprojekt

**Zweck:** Formale Bestätigung des erfolgreichen Vorprojekt-Abschlusses.

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | Auftraggeber |
| **Status** | OFFEN – Am Ende des Vorprojekts zu erstellen |

---

## 7. Ergänzende Produkte (ab v1.4)

### 7.1 Betriebskonzept (Gerüst)

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | IT-Betrieb |
| **Konzept-Referenz** | Kap. 18 (SLA, Monitoring, Support, Backup/DR, Release-Management) |
| **Status** | ERGÄNZT – Gerüst vorhanden, konkrete SLA-Werte als Vorschlag |

### 7.2 Incident-Response-Plan

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | ISB / DSB |
| **Konzept-Referenz** | Kap. 19 (Vorfallkategorien, Eskalation, DSGVO-Meldepflicht, KI-spezifische Response) |
| **Status** | ERGÄNZT – inkl. Halluzinations-Response und Berechtigungsfehler-Protokoll |

### 7.3 Kostengerüst-Template

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | PMO / Controlling |
| **Konzept-Referenz** | Kap. 20 (CAPEX/OPEX-Struktur, TCO-Vergleich) |
| **Status** | ERGÄNZT – Template mit Kostenblöcken, Werte durch IT und Controlling zu befüllen |

### 7.4 Change-Management-Konzept

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | Fachbereich / PMO |
| **Konzept-Referenz** | Kap. 21 (Pilotierung, Champions-Netzwerk, Schulung, Feedback, Erfolgsmessung) |
| **Status** | ERGÄNZT – 3-Phasen-Pilotierung (Station → Erweiterter Pilot → Klinikweiter Rollout) |

### 7.5 SAP IS-H/i.s.h.med KI-Konnektor

| Attribut | Beschreibung |
|----------|-------------|
| **Verantwortlich** | IT-Architektur |
| **Konzept-Referenz** | Kap. 22 (Systemübersicht, Connectoren, KI-Integrationspfade, FHIR-Transformation, Berechtigungsmigration) |
| **Status** | ERGÄNZT – BAPI, HL7, FHIR-Fähigkeiten, IHE-Profile und Empfehlungen für Connector-Strategie |

---

## Offene Punkte und Handlungsbedarf

| Nr | Offener Punkt | Verantwortlich | Frist | Priorität |
|----|--------------|----------------|-------|-----------|
| OP-01 | Projektauftrag formal erstellen und genehmigen | Auftraggeber | Mär 2026 | Hoch |
| OP-02 | Projektleiter mit PM-Exzellenz installieren | Auftraggeber | Mai 2026 | Kritisch |
| OP-03 | Kostengerüst mit konkreten Werten befüllen | IT / Controlling | Apr 2026 | Hoch |
| OP-04 | Averbis/Meierhofer-Angebot einholen und bewerten | PM | Mär 2026 | Hoch |
| OP-05 | Formale Risikobewertung mit Eintrittswahrscheinlichkeiten erstellen | PM | Mär 2026 | Mittel |
| OP-06 | ISILON-Performance- und Sicherheitsanalyse durchführen | IT-Infrastruktur | Apr 2026 | Mittel |
| OP-07 | DSFA formell im Hauptprojekt durchführen | DSB | Q3/2026 | Hoch |
| OP-08 | Abnahmedokument Vorprojekt erstellen | Auftraggeber | Jun 2026 | Mittel |
| OP-09 | Fachliche Anforderungen mit Fachbereich abstimmen | Fachbereich | Mär 2026 | Hoch |
| OP-10 | GPU-Infrastruktur-Sizing und Beschaffung einleiten | IT-Infrastruktur | Apr 2026 | Hoch |
