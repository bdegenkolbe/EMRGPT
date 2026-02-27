# Summary

## [Übersetzte 'Besprechungsinformationen']
> [Übersetzte 'Datum:'] 2026-02-27 10:02:00
> [Übersetzte 'Ort: [Ort einfügen]']
> [Übersetzte 'Teilnehmende:'] [Speaker 1] [Speaker 2] [Speaker 3] [Speaker 4] [Speaker 5] [Speaker 6] [Speaker 7] [Speaker 8] [Speaker 9]
## [Übersetzte 'Besprechungsnotizen']
- Technische Einbindung von HydeMedia in Averbes/MKIS-Architektur
  - Ziel: Externes Dokumentenrepository HydeMedia mit Averbes „Medical Summary“ und MKIS integrieren; Event-basierte Anbindung, um pro Fall/Patient relevante historische Dokumente aus HydeMedia zu laden.
  - Schnittstellen: Präferenz für REST-API; FHIR möglich, muss spezifiziert werden. HL7 für MKIS→Medical Summary-Datenfluss vorgesehen.
  - HydeMedia-Schnittstellenqualität abhängig von UKL-Bestellung; Entscheidung über Standard (REST vs. FHIR) steht aus. Averbes kann beide Varianten integrieren.
  - Schlussfolgerung: Technische Machbarkeit bestätigt; genaue Schnittstellenspezifikation erforderlich.
- Datenhaltung, Cloud-Nutzung und Vektordatenbank
  - On-Prem-Persistenz: Dokumente und strukturierte Daten lokal im Medical Summary Backend; Vektordatenbank lokal, Berechnungen in der Cloud, Speicherung on-prem.
  - LLM in Azure (EU, Schweden) mit temporärer Verarbeitung; keine Massendatenmigration. Alternativen: Stackit (DE), Arvato, Telekom zur Minimierung US-Zugriffsrisiken; Stackit meist teurer.
  - RAG-Ansatz: Temporäre Verarbeitung, Daten verbleiben primär on-prem; kein Transfer von 30 Mio. Dokumenten in die Cloud.
  - Datenschutz: Bedarf an AVV, TOMs, Unterauftragnehmerlisten, Datenschutzkonzept. In Sachsen Cloud-Freigabe unklar; Termin mit Landesdatenschützer angesetzt.
  - Schlussfolgerung: Compliance-Anforderungen adressierbar, Entscheidung zur Cloud-Nutzung standortabhängig offen.
- Brownfield-Ansatz und Altdatenmigration
  - MKIS-Einführung als Brownfield: Keine vollständige Migration aller Altdaten aus SAP; Altdaten rechtssicher in HydeMedia archiviert (100 Jahre).
  - Strukturierte Altdaten werden zu PDFs konvertiert und in HydeMedia abgelegt; Randapplikationen/Register zusätzlich zu ISH/ISH Med berücksichtigen.
  - Hoher Anfangsbedarf an Altdatenzugriff, später sinkend; Architektur muss breite Quellabdeckung und frühe Verfügbarkeit sicherstellen.
- Dokumentenqualität, KDL-Labels und OCR
  - Heterogene, teils schlechte Qualität (Mehrfach-Scans, Handyfotos, inkonsistente Zeitstempel); Modelle robust, aber Grenzen bei sehr schlechter Qualität.
  - HydeMedia speichert PDFs; OCR-Kennung seit letzter Woche implementiert. Unklar, ob OCR rückwirkend auf alle Bestände läuft.
  - KDL-Klassifikation seit ca. 2 Jahren verpflichtend; rückwirkende Klassifizierung vermutlich nicht erfolgt. Label-Qualität im Archiv unklar; Risiko für Filterlogik im Medical Summary.
  - Prüfen, ob FHIR-Daten direkt befüllt werden können, um OCR-Nachstrukturierung zu vermeiden.
  - Schlussfolgerung: Schrittweises Vorgehen und Qualitäts-/Labelprüfung notwendig; schlechtere Label- und OCR-Qualität kann Dienstleistungsaufwand deutlich erhöhen.
- Vorgehensmodell für Datenübernahme und Performance
  - Präferenz für ADT-getriebenes Onboarding: Ab ADT-Meldung eines neuen Patienten Embedding relevanter Dokumente; keine Masseneinspielung historischer Bestände aus Performance- und Relevanzgründen.
  - Fokus auf aktuelle/jüngere Akten; Tiefenrecherche im Archiv nur für Spezialfälle. Optionale Vor-Klassifikation via Erkennungs-/Validierungsprompts (z. B. Arztbrief, OP-Bericht); Möglichkeit zur Nutzerkorrektur in der Anwendung.
  - Schlussfolgerung: ADT-first, schrittweise Einsortierung, ergänzende Validierung und optional Nutzerkorrekturen.
- Pilotstatus, Testphasen und Kostenrahmen
  - Asklepios in Testphase (bis 3 Monate), danach Lizenzierung und Live-Betrieb; Greifswald verzögert (IT-Leiterwechsel); UMG plant Testphase mit anschließender Lizenzierung. In der Testphase fallen Dienstleistungstage an, Lizenzkosten erst danach.
  - Anbindung Archiv/CMS (historische Daten) mit 10–20 Tagen Entwicklungsaufwand zusätzlich zu Teststellung; Identity-Integration (OIDC/SSO) Standard ohne Zusatzkosten; UI bleibt unverändert, HydeMedia-Dokumente werden automatisch zugeordnet.
  - Exakte Aufwandsabschätzung erst nach Detailprüfung der Datenlage (Dokumententypen, Qualität, Labelstatus) möglich; grobe Preisindikation vorab möglich.
- Zeitplan, Prioritäten und Governance (KIS-Einführung zum 1.10.)
  - Projektteam priorisiert KIS-Einführung; parallele Einführung weiterer Systeme zum 1.10. kritisch. Klinikführung fordert Übersichtsfunktion zum 1.10. zur Entlastung der Versorgung.
  - Entscheidung außerhalb des Kernprojektteams; Eskalation an Vorstand/Lenkungsausschuss erforderlich (z. B. Abstimmung mit Dr. Vasipki).
  - Schlussfolgerung: Realistische Roadmap und Minimalfunktion („Übersicht“) definieren, Erwartungsmanagement sichern.
- Rollen und Zuständigkeiten
  - 4K Analytics: Bewertung/Entscheidungsvorlage, Warehouse-Projektleitung.
  - Mayerhofer: Produktmanagement medizinische Dokumentation, Integration Medical Dialogue/EMCIS; Themen Arztbrief/Medical Peak.
  - Averbes: Medical Summary, Health Discovery (NLP), technische Integration, Partnermanagement, kaufmännisch.
  - Exklusivität: Integration von Averbes mit MKIS exklusiv über Mayerhofer.
  - Schlussfolgerung: Klare Partnerlandschaft; technische Ansprechpartner benannt.
## [Übersetzte 'Nächste Schritte']
- [ ] Schnittstellenspezifikation für HydeMedia (REST vs. FHIR) klären und dokumentieren; HL7-Datenflüsse MKIS↔Medical Summary konkretisieren.
- [ ] Event-basierten Abrufprozess (z. B. ADT/Fallanlage) für historische Dokumente definieren; ADT-first-Strategie und Backlog-Plan festlegen.
- [ ] Systemlandschaft und Quellenliste (SAP, Randapplikationen/Register) final erfassen; exemplarische Dokumentensätze bereitstellen.
- [ ] Detailanalyse durchführen: Dokumentenqualität, KDL-/OCR-Status, Label-Qualität; Klärung, ob OCR rückwirkend läuft; FHIR-Strategie für strukturierte Daten prüfen.
- [ ] Compliance-/Datenschutzanforderungen für Cloud-/LLM-Nutzung bestätigen: AVV, TOMs, Unterauftragnehmer; Architekturskizze bereitstellen; Referenzen (Klinikum Rheine) mitsenden.
- [ ] Datenschützertermin (Sachsen) durchführen; Ergebnisse zur Cloud-Freigabe und Anforderungen dokumentieren; eingereichte Unterlagen (Greifswald/Patrick) nachverfolgen.
- [ ] Kostenangebot aktualisieren: Teststellung + 10–20 Tage für Archiv-/HydeMedia-Anbindung; Grobschätzung verfeinern nach Analyse.
- [ ] Interne Klärung: Priorisierung Übersichtsfunktion bis 1.10. mit Dr. Vasipki; Thema in Lenkungsausschuss zur Entscheidung und Roadmap.
- [ ] Entscheidung zur Implementierung von Validierungs- und Nutzerkorrekturfunktionen treffen.
- [ ] Abstimmung mit HydeMedia-Anbieter zu verfügbaren APIs, OCR-Status und notwendigen Erweiterungen.
- [ ] [Mehr einfügen]
## [Übersetzte 'KI-/AI-Empfehlungen']
> 1. Entscheidung zwischen REST-API und FHIR für HydeMedia-Zugriff offen; Auswirkungen auf Zeitplan und Aufwand klären.
> 2. Ereignissteuerung präzisieren: Welche Events (z. B. ADT) laden welche Dokumente; Performance-/Backlog-Strategie definieren.
> 3. Unklare rechtliche Lage zur Cloud-Nutzung (insb. Sachsen) und Umfang der Datenschutzunterlagen konkretisieren; Unterlagen vorab bereitstellen.
> 4. OCR-Rückwirkung und KDL-Label-Qualität im Archiv ungeklärt; Schnelltest mit repräsentativen Proben zur Risikobewertung durchführen.
> 5. FHIR-Strategie festlegen: Direkte Nutzung strukturierter Daten statt PDF-OCR prüfen, um ineffiziente Prozesse zu vermeiden.
> 6. Realistische Roadmap bis 1.10. mit Minimalfunktion („Übersicht“), klaren Meilensteinen und Verantwortlichkeiten verabschieden.
> 7. Ressourcen- und Roadmap-Planung für MKIS-Integration inkl. HydeMedia-Anbindung verbindlich machen; Aufwände und Rollen transparent.