Vorprojekt EMRgpt

![](media/image1.png){width="2.1693602362204722in"
height="9.228472222222223in"}

1\. Projektorganisation [3](#_Toc256000000)

1.1. Projektauftrag Vorprojekt [3](#_Toc256000001)

1.2. Projektorganisation [4](#_Toc256000002)

1.3. Stakeholderanalyse [4](#_Toc256000003)

1.4. Kommunikationsplan [4](#_Toc256000004)

1.5. Vorläufiger Business Case [4](#_Toc256000005)

1.6. Risiko- und Chancenliste [5](#_Toc256000006)

2\. Fachlich [5](#_Toc256000007)

2.1. Zielbild EMRgpt [5](#_Toc256000008)

2.2. Use-Case-Beschreibung LLM-Anbindung [5](#_Toc256000009)

2.2.1. Kostenanalyse [5](#_Toc256000010)

2.3. Fachliche Anforderungen [5](#_Toc256000011)

2.3.1. Daten aus UKLytics [5](#_Toc256000012)

3\. Technisch [6](#_Toc256000013)

3.1. Technische Zielarchitektur [6](#_Toc256000014)

3.1.1. Infrastruktur [6](#_Toc256000015)

3.2. Marktanalyse [6](#_Toc256000016)

3.3. Analyse HYDMedia [6](#_Toc256000017)

3.3.1. Schnittstellenbeschreibung FHIR [6](#_Toc256000018)

3.4. Analyse DMI Lösung [6](#_Toc256000019)

3.5. Vergleich HYDMedia vs. DMI [7](#_Toc256000020)

3.6. Schnittstellenübersicht [7](#_Toc256000021)

3.7. Technisches Vorgehensmodell [7](#_Toc256000022)

3.8. Zugriff auf ISILON [7](#_Toc256000023)

3.9. KIS-Dokumentenzugriff (Meierhofer) [7](#_Toc256000024)

4\. Rechtebewertung und Sicherheit [8](#_Toc256000025)

4.1. Datenschutzkonzept [8](#_Toc256000026)

4.2. Datenschutz-Folgenabschätzung (Vorprüfung) [8](#_Toc256000027)

4.3. Informationssicherheitsbewertung [8](#_Toc256000028)

4.4. Berechtigungskonzept [8](#_Toc256000029)

4.5. SAP-Berechtigungsanalyse [8](#_Toc256000030)

4.6. Logging- und Nachvollziehbarkeitskonzept [9](#_Toc256000031)

5\. Management Summary [9](#_Toc256000032)

5.1. Entscheidungsgrundlage Datenhaltung [9](#_Toc256000033)

5.2. Entscheidungsgrundlage LLM-Anbindung [9](#_Toc256000034)

5.3. Management-Entscheidungsvorlage [9](#_Toc256000035)

6\. Abschlussdokumentation [9](#_Toc256000036)

6.1. Empfehlung für Hauptprojekt [9](#_Toc256000037)

6.2. Grober Umsetzungsfahrplan [10](#_Toc256000038)

6.3. Abnahmedokument Vorprojekt [10](#_Toc256000039)

1.  []{#_Toc256000000 .anchor}Projektorganisation

    1.  []{#_Toc256000001 .anchor}Projektauftrag Vorprojekt

> **Zweck:** Der Projektauftrag legitimiert das Vorprojekt EMRgpt formal
> und schafft eine verbindliche Grundlage für alle Beteiligten. Er
> beschreibt die Zielsetzung der Anbindung eines LLM an
> Datenhaltungsebene auf strategischer Ebene. Zudem grenzt er das
> Vorprojekt klar vom möglichen Hauptprojekt ab. Der Projektauftrag
> definiert den Nutzen für die Organisation und stellt den Bezug zur
> Digitalisierungsstrategie her. Er dient als Referenzdokument für
> Governance, Priorisierung und Ressourcenbindung.
>
> **Zusammensetzung:** Ziele, Scope, Nicht-Ziele, Budgetrahmen,
> Zeitrahmen, Auftraggeber
>
> **Qualitätskriterien:** Vollständig, genehmigt, verständlich
>
> **Abnahmekriterien:** Schriftliche Freigabe durch Auftraggeber
>
> **Verantwortlich:** Auftraggeber

2.  []{#_Toc256000002 .anchor}Projektorganisation

> **Zweck:** Die Projektorganisation stellt sicher, dass alle Rollen,
> Verantwortlichkeiten und Entscheidungswege klar definiert sind. Sie
> ermöglicht eine strukturierte Zusammenarbeit zwischen IT, Fachbereich,
> Datenschutz und Informationssicherheit. Durch klare Rollenzuordnung
> werden Doppelarbeiten und Unklarheiten vermieden. Die
> Projektorganisation stellt die Einbindung aller relevanten Stakeholder
> sicher. Sie bildet die Grundlage für eine effiziente Projektsteuerung
> nach PRINCE2.
>
> **Zusammensetzung:** Rollenbeschreibung, Organigramm,
> Vertretungsregelung
>
> **Qualitätskriterien:** Vollständig, nachvollziehbar
>
> **Abnahmekriterien:** Bestätigung durch Projektleitung
>
> **Verantwortlich:** Projektmanager

3.  []{#_Toc256000003 .anchor}Stakeholderanalyse

> **Zweck:** Die Stakeholderanalyse identifiziert alle Personen und
> Organisationen, die Einfluss auf das Vorprojekt haben oder davon
> betroffen sind. Sie bewertet deren Interessen, Erwartungen und
> Einflussmöglichkeiten. Dadurch können Risiken frühzeitig erkannt und
> adressiert werden. Die Analyse unterstützt eine zielgerichtete
> Kommunikation. Sie trägt wesentlich zur Akzeptanz der späteren
> Entscheidung bei.
>
> **Zusammensetzung:** Stakeholderliste, Einfluss-/Interessenmatrix
>
> **Qualitätskriterien:** Vollständig, aktuell
>
> **Abnahmekriterien:** Freigabe durch Lenkungsausschuss
>
> **Verantwortlich:** Projektmanager

4.  []{#_Toc256000004 .anchor}Kommunikationsplan

> **Zweck:** Der Kommunikationsplan legt fest, wie, wann und mit wem im
> Projekt kommuniziert wird. Er sorgt für Transparenz und verhindert
> Informationsdefizite. Unterschiedliche Informationsbedarfe der
> Stakeholder werden berücksichtigt. Der Plan unterstützt eine
> konsistente Projektkommunikation. Er ist ein zentrales Instrument zur
> Steuerung von Erwartungen.
>
> **Zusammensetzung:** Kommunikationsmatrix, Termine, Formate
>
> **Qualitätskriterien:** Klar, realistisch
>
> **Abnahmekriterien:** Zustimmung der Projektleitung
>
> **Verantwortlich:** Projektmanager

5.  []{#_Toc256000005 .anchor}Vorläufiger Business Case

> **Zweck:** Der vorläufige Business Case bewertet den strategischen und
> wirtschaftlichen Nutzen von EMRgpt. Er stellt Vergleichsdaten( z.B.
> Kosten, Nutzen und qualitative Mehrwerte) gegenüber. Risiken und
> Annahmen werden transparent dokumentiert. Der Business Case dient als
> Entscheidungsgrundlage für die Fortführung als Hauptprojekt. Er wird
> im Verlauf des Projekts verfeinert.
>
> **Zusammensetzung:** Nutzenargumentation, Kostenabschätzung, Risiken
>
> **Qualitätskriterien:** Plausibel, nachvollziehbar
>
> **Abnahmekriterien:** Genehmigung durch Lenkungsausschuss
>
> **Verantwortlich:** Auftraggeber

6.  []{#_Toc256000006 .anchor}Risiko- und Chancenliste

> **Zweck:** Die Risiko- und Chancenliste erfasst systematisch alle
> identifizierten Projektrisiken und -chancen. Sie ermöglicht eine
> strukturierte Bewertung hinsichtlich Eintrittswahrscheinlichkeit und
> Auswirkung. Maßnahmen zur Risikominimierung werden definiert. Die
> Liste unterstützt eine vorausschauende Projektsteuerung. Sie wird
> regelmäßig aktualisiert.
>
> **Zusammensetzung:** Risiko-ID, Beschreibung, Bewertung, Maßnahme
>
> **Qualitätskriterien:** Vollständig, aktuell
>
> **Abnahmekriterien:** Kenntnisnahme durch Projektleitung
>
> **Verantwortlich:** Projektmanager

2.  []{#_Toc256000007 .anchor}Fachlich

    1.  []{#_Toc256000008 .anchor}Zielbild EMRgpt

  -----------------------------------------------------------------------
  Verbindung        verweist auf [[Technische
                    Zielarchitektur]{.underline}](#_Toc256000014)
  ----------------- -----------------------------------------------------

  -----------------------------------------------------------------------

> **Zweck:** Das Zielbild EMRgpt beschreibt die angestrebte
> ganzheitliche Lösung aus fachlicher und technischer Perspektive. Es
> vermittelt eine gemeinsame Vision für alle Beteiligten. Das Zielbild
> ordnet EMRgpt in die bestehende Systemlandschaft ein. Es dient als
> Leitplanke für alle weiteren Analysen und Entscheidungen. Zudem
> unterstützt es die strategische Kommunikation gegenüber dem
> Management.
>
> **Zusammensetzung:** Vision, Nutzen, Architektur-Skizze
>
> **Qualitätskriterien:** Verständlich, konsistent
>
> **Abnahmekriterien:** Zustimmung des Auftraggebers
>
> **Verantwortlich:** Projektmanager, Carina(Erstellen), Gert , Robert
> W.

2.  []{#_Toc256000009 .anchor}Use-Case-Beschreibung LLM-Anbindung

> **Zweck:** Die Use-Case-Beschreibung konkretisiert den praktischen
> Einsatz von hAIppokrates im klinischen Alltag. Sie beschreibt, wie das
> LLM auf Patientendokumente zugreift und Mehrwert erzeugt. Der Use Case
> bildet die fachliche Grundlage für technische und rechtliche
> Bewertungen. Er stellt sicher, dass die Lösung an realen Anforderungen
> ausgerichtet ist. Zudem dient er als Referenz für spätere
> Implementierungen.
>
> **Zusammensetzung:** Akteure, Ablauf, Datenquellen, Nutzen
>
> **Qualitätskriterien:** Praxisnah, eindeutig
>
> **Abnahmekriterien:** Freigabe durch Fachbereich
>
> **Verantwortlich:** Fachbereich (Felix, Carina, Martin Neef, Niko
> v.D.) 

1.  []{#_Toc256000010 .anchor}Kostenanalyse

```{=html}
<!-- -->
```
3.  []{#_Toc256000011 .anchor}Fachliche Anforderungen

> **Zweck:** Die fachlichen Anforderungen beschreiben, welche
> Informationen und Funktionen das LLM bereitstellen soll. Sie stellen
> sicher, dass medizinische, administrative und rechtliche Bedürfnisse
> berücksichtigt werden. Die Anforderungen bilden die Basis für
> technische Lösungsvarianten. Sie verhindern eine rein
> technologiegetriebene Umsetzung. Zudem dienen sie als Referenz für die
> spätere Erfolgsmessung.
>
> **Zusammensetzung:** Anforderungsliste, Priorisierung
>
> **Qualitätskriterien:** Vollständig, verständlich
>
> **Abnahmekriterien:** Freigabe Fachbereich
>
> **Verantwortlich:** Fachbereich (Carina, Niko v.D., Martin Neef)

1.  []{#_Toc256000012 .anchor}Daten aus UKLytics

```{=html}
<!-- -->
```
3.  []{#_Toc256000013 .anchor}Technisch

    1.  []{#_Toc256000014 .anchor}Technische Zielarchitektur

  -----------------------------------------------------------------------
  Verbindung             beginnt bei [[Zielbild
                         EMRgpt]{.underline}](#_Toc256000008)
  ---------------------- ------------------------------------------------

  -----------------------------------------------------------------------

> **Zweck:** Die technische Zielarchitektur beschreibt die angestrebte
> Systemlandschaft für EMRgpt auf hoher Ebene. Sie zeigt das
> Zusammenspiel von LLM, Datenhaltung, Schnittstellen und Sicherheit.
> Dadurch entsteht ein gemeinsames technisches Verständnis. Die
> Architektur dient als Leitlinie für Lösungsbewertungen. Sie reduziert
> spätere Architekturkonflikte.
>
> **Zusammensetzung:** Architekturdiagramm, Beschreibung
>
> **Qualitätskriterien:** Konsistent, nachvollziehbar
>
> **Abnahmekriterien:** Freigabe IT-Architektur
>
> **Verantwortlich:** IT-Architekt, Gert, Carina

1.  []{#_Toc256000015 .anchor}Infrastruktur

```{=html}
<!-- -->
```
2.  []{#_Toc256000016 .anchor}Marktanalyse

> Anbietersuche EMRgpt 
>
>  
>
> Liegt bei 4K

3.  []{#_Toc256000017 .anchor}Analyse HYDMedia

> **Zweck:** Die Analyse HYDMedia untersucht die bestehende Lösung im
> Hinblick auf eine LLM-Anbindung. Sie beschreibt Architektur,
> Schnittstellen und Datenstrukturen. Stärken und Einschränkungen werden
> transparent dargestellt. Die Analyse dient als Grundlage für den
> Vergleich mit der DMI-Lösung. Sie unterstützt eine fundierte
> Entscheidungsfindung.
>
> **Zusammensetzung:** Systembeschreibung, Schnittstellen, Bewertung
>
> **Qualitätskriterien:** Technisch korrekt, vollständig
>
> **Abnahmekriterien:** Bestätigung durch IT
>
> **Verantwortlich:** Valentin

1.  []{#_Toc256000018 .anchor}Schnittstellenbeschreibung FHIR

> **Zweck:** Dieses Produkt beschreibt die FIHR-Schnittstelle von
> HYDMedia im Detail. Es klärt verfügbare Daten, Zugriffsmechanismen und
> technische Einschränkungen. Die Beschreibung ist Grundlage für
> Machbarkeitsbewertungen. Sie reduziert Implementierungsrisiken. Zudem
> unterstützt sie die Abstimmung mit externen Partnern.
>
> **Zusammensetzung:** Technische Spezifikation
>
> **Qualitätskriterien:** Technisch korrekt
>
> **Abnahmekriterien:** Freigabe IT
>
> **Verantwortlich:** Schnittstellenverantwortlicher

4.  []{#_Toc256000019 .anchor}Analyse DMI Lösung

> **Zweck:** Diese Analyse beschreibt die von DMI bereitgestellte Lösung
> zur Datenhaltung. Sie untersucht die Eignung für den Einsatz mit einem
> LLM. Schnittstellen, Sicherheitsmechanismen und Integrationsaufwand
> werden bewertet. Die Ergebnisse werden vergleichbar zur
> HYDMedia-Analyse dokumentiert. Ziel ist eine objektive
> Entscheidungsbasis.
>
> **Zusammensetzung:** Systemübersicht, Architektur, Bewertung
>
> **Qualitätskriterien:** Vergleichbar, strukturiert
>
> **Abnahmekriterien:** Freigabe durch IT-Leitung
>
> **Verantwortlich:** Valentin (Carina)

5.  []{#_Toc256000020 .anchor}Vergleich HYDMedia vs. DMI

> **Zweck:** Dieses Produkt stellt einen strukturierten Vergleich
> zwischen HYDMedia und der DMI-Lösung dar. Es bewertet beide Optionen
> anhand definierter Kriterien wie Technik, Sicherheit und Integration.
> Der Vergleich schafft Transparenz für Entscheidungsträger. Subjektive
> Präferenzen werden dadurch reduziert. Er bildet die Grundlage für eine
> fundierte Entscheidung.
>
> **Zusammensetzung:** Kriterienmatrix, Bewertung
>
> **Qualitätskriterien:** Objektiv, vollständig
>
> **Abnahmekriterien:** Zustimmung Lenkungsausschuss
>
> **Verantwortlich:** Projektmanager, Valentin

6.  []{#_Toc256000021 .anchor}Schnittstellenübersicht

> **Zweck:** Die Schnittstellenübersicht identifiziert alle relevanten
> technischen Schnittstellen im Zielbild. Sie stellt Datenflüsse und
> Abhängigkeiten transparent dar. Dadurch werden Integrationsrisiken
> frühzeitig erkannt. Die Übersicht dient als Grundlage für
> Detailbeschreibungen. Sie unterstützt die technische Abstimmung
> zwischen Systemen.
>
> **Zusammensetzung:** Übersichtsgrafik, Schnittstellenliste
>
> **Qualitätskriterien:** Vollständig, aktuell
>
> **Abnahmekriterien:** Bestätigung IT
>
> **Verantwortlich:** IT-Architekt, Valentin

7.  []{#_Toc256000022 .anchor}Technisches Vorgehensmodell

> **Zweck:** Das technische Vorgehensmodell beschreibt mögliche
> Integrationsansätze für das LLM. Es stellt Varianten wie RAG,
> Middleware oder direkte API-Anbindung gegenüber. Dadurch werden
> technische Optionen transparent. Das Modell unterstützt die
> Entscheidungsfindung. Es schafft Klarheit über Komplexität und
> Risiken.
>
> **Zusammensetzung:** Variantenbeschreibung, Bewertung
>
> **Qualitätskriterien:** Vergleichbar, verständlich
>
> **Abnahmekriterien:** Zustimmung IT-Leitung
>
> **Verantwortlich:** IT-Architekt, 4K

8.  []{#_Toc256000023 .anchor}Zugriff auf ISILON

> **Zweck:** Dieses Produkt analysiert, wie Patientendokumente auf
> ISILON technisch bereitgestellt werden können. Es berücksichtigt
> Performance, Sicherheit und Zugriffsrechte. Die Analyse ist essenziell
> für die Datenverfügbarkeit des LLM. Sie deckt mögliche technische
> Einschränkungen auf. Zudem unterstützt sie die Abstimmung mit
> Storage-Verantwortlichen.
>
> **Zusammensetzung:** Analysebericht
>
> **Qualitätskriterien:** Vollständig, korrekt
>
> **Abnahmekriterien:** Bestätigung IT
>
> **Verantwortlich:** IT-Infrastruktur (Anfrage Systemmanagement, wer?)
> -- Carina fragt Daniel

9.  []{#_Toc256000024 .anchor}KIS-Dokumentenzugriff (Meierhofer)

> **Zweck:** Dieses Produkt dokumentiert die durch Meierhofer
> vorgestellten Zugriffsmöglichkeiten auf Dokumente im KIS. Es
> beschreibt verfügbare Schnittstellen und Nutzungsszenarien. Die
> Informationen sind Grundlage für Integrationsentscheidungen. Sie
> ermöglichen eine realistische Bewertung des Aufwands. Zudem
> unterstützen sie die Abstimmung mit dem KIS-Hersteller.
>
> **Zusammensetzung:** Präsentation, Protokoll
>
> **Qualitätskriterien:** Nachvollziehbar
>
> **Abnahmekriterien:** Kenntnisnahme Projektteam
>
> **Verantwortlich:** KIS-Verantwortlicher, Robert W., Carina, Valentin

4.  []{#_Toc256000025 .anchor}Rechtebewertung und Sicherheit

    1.  []{#_Toc256000026 .anchor}Datenschutzkonzept

> **Zweck:** Das Datenschutzkonzept beschreibt den rechtskonformen
> Umgang mit Patientendaten. Es berücksichtigt DSGVO, Zweckbindung und
> Datenminimierung. Das Konzept identifiziert datenschutzrechtliche
> Risiken. Es definiert notwendige Schutzmaßnahmen. Zudem ist es
> Voraussetzung für eine spätere Freigabe.
>
> **Zusammensetzung:** Datenschutzanalyse, Maßnahmen
>
> **Qualitätskriterien:** DSGVO-konform
>
> **Abnahmekriterien:** Freigabe Datenschutzbeauftragter
>
> **Verantwortlich:** Datenschutzbeauftragter (Hr. Sünkel)

2.  []{#_Toc256000027 .anchor}Datenschutz-Folgenabschätzung (Vorprüfung)

> **Zweck:** Diese Vorprüfung bewertet, ob eine formale
> Datenschutz-Folgenabschätzung erforderlich ist. Sie analysiert Art,
> Umfang und Risiko der Datenverarbeitung. Dadurch werden regulatorische
> Anforderungen frühzeitig erkannt. Die Vorprüfung reduziert rechtliche
> Unsicherheiten. Sie unterstützt eine rechtssichere Projektplanung.
>
> **Zusammensetzung:** Prüfdokument
>
> **Qualitätskriterien:** Vollständig
>
> **Abnahmekriterien:** Zustimmung Datenschutzbeauftragter
>
> **Verantwortlich:** Datenschutzbeauftragter (Hr. Sünkel)

3.  []{#_Toc256000028 .anchor}Informationssicherheitsbewertung

> **Zweck:** Die Informationssicherheitsbewertung analysiert
> Schutzbedarf und Risiken der geplanten Lösung. Sie betrachtet
> Verfügbarkeit, Vertraulichkeit und Integrität. Die Bewertung dient als
> Grundlage für Sicherheitsmaßnahmen. Sie stellt die Einhaltung interner
> Sicherheitsvorgaben sicher. Zudem unterstützt sie
> Managemententscheidungen.
>
> **Zusammensetzung:** Schutzbedarfsanalyse
>
> **Qualitätskriterien:** Nachvollziehbar
>
> **Abnahmekriterien:** Freigabe ISB
>
> **Verantwortlich:** Informationssicherheitsbeauftragter S.Krause

4.  []{#_Toc256000029 .anchor}Berechtigungskonzept

> **Zweck:** Das Berechtigungskonzept definiert, wer welche Daten über
> das LLM einsehen darf. Es berücksichtigt Rollen, Fachbereiche und
> Zugriffsszenarien. Das Konzept minimiert unberechtigte Zugriffe. Es
> ist zentral für Datenschutz und Sicherheit. Zudem dient es als
> Grundlage für technische Umsetzung.
>
> **Zusammensetzung:** Rollenmodell, Regeln
>
> **Qualitätskriterien:** Konsistent
>
> **Abnahmekriterien:** Freigabe IT & Datenschutz
>
> **Verantwortlich:** Martin Schmeißer, Fr. Stallmach, Fr.
> Schmidt-Morich

5.  []{#_Toc256000030 .anchor}SAP-Berechtigungsanalyse

> **Zweck:** Die SAP-Berechtigungsanalyse untersucht bestehende Rollen
> und Berechtigungen. Sie identifiziert relevante Ableitungen für
> EMRgpt. Dadurch werden Synergien genutzt und Redundanzen vermieden.
> Die Analyse unterstützt ein konsistentes Berechtigungsmodell. Sie
> reduziert Implementierungsaufwand.
>
> **Zusammensetzung:** Analysebericht
>
> **Qualitätskriterien:** Vollständig
>
> **Abnahmekriterien:** Zustimmung SAP-Verantwortliche
>
> **Verantwortlich:** Martin Schmeißer, Fr. Stallmach, Fr.
> Schmidt-Morich

6.  []{#_Toc256000031 .anchor}Logging- und Nachvollziehbarkeitskonzept

> **Zweck:** Dieses Produkt beschreibt, wie Zugriffe und LLM-Anfragen
> protokolliert werden. Es stellt die Nachvollziehbarkeit sicher. Das
> Konzept unterstützt Compliance- und Audit-Anforderungen. Es dient der
> Missbrauchserkennung. Zudem erhöht es das Vertrauen in die Lösung.
>
> **Zusammensetzung:** Logging-Konzept
>
> **Qualitätskriterien:** Revisionssicher
>
> **Abnahmekriterien:** Freigabe ISB
>
> **Verantwortlich:** IT-Sicherheit, Projektmanager

5.  []{#_Toc256000032 .anchor}Management Summary

    1.  []{#_Toc256000033 .anchor}Entscheidungsgrundlage Datenhaltung

> **Zweck:** Die Entscheidungsgrundlage bereitet die Auswahl der
> Datenhaltung strukturiert vor. Sie fasst technische, fachliche und
> rechtliche Aspekte zusammen. Entscheidungsoptionen werden klar
> dargestellt. Risiken und Auswirkungen werden transparent gemacht. Sie
> unterstützt eine belastbare Managemententscheidung.
>
> **Zusammensetzung:** Entscheidungsdokument
>
> **Qualitätskriterien:** Entscheidungsrelevant
>
> **Abnahmekriterien:** Entscheidung Management
>
> **Verantwortlich:** Projektmanager, Carina

2.  []{#_Toc256000034 .anchor}Entscheidungsgrundlage LLM-Anbindung

> **Zweck:** Dieses Produkt bewertet verschiedene Varianten der
> LLM-Anbindung. Es stellt Nutzen, Risiken und Aufwände gegenüber.
> Dadurch wird eine technologieoffene Entscheidung ermöglicht. Die
> Grundlage verhindert vorschnelle Festlegungen. Sie unterstützt eine
> nachhaltige Architekturentscheidung.
>
> **Zusammensetzung:** Variantenvergleich
>
> **Qualitätskriterien:** Vergleichbar
>
> **Abnahmekriterien:** Zustimmung Lenkungsausschuss
>
> **Verantwortlich:** IT-Architekt, Carina, Projektmanager

3.  []{#_Toc256000035 .anchor}Management-Entscheidungsvorlage

> **Zweck:** Die Management-Entscheidungsvorlage fasst alle relevanten
> Ergebnisse des Vorprojekts zusammen. Sie stellt Entscheidungsoptionen
> klar und verständlich dar. Vor- und Nachteile werden transparent
> gegenübergestellt. Die Vorlage ermöglicht eine fundierte Entscheidung
> über die Fortführung als Hauptprojekt. Sie bildet den formalen
> Abschluss des Vorprojekts.
>
> **Zusammensetzung:** Zusammenfassung, Optionen, Empfehlung
>
> **Qualitätskriterien:** Prägnant, entscheidungsrelevant
>
> **Abnahmekriterien:** Entscheidung des Managements
>
> **Verantwortlich:** Projektmanager

6.  []{#_Toc256000036 .anchor}Abschlussdokumentation

    1.  []{#_Toc256000037 .anchor}Empfehlung für Hauptprojekt

> **Zweck:** Die Empfehlung fasst alle Erkenntnisse des Vorprojekts
> zusammen. Sie leitet eine klare Handlungsempfehlung ab. Die Empfehlung
> berücksichtigt Strategie, Technik und Recht. Sie unterstützt die
> Entscheidung zur Projektfortsetzung. Zudem schafft sie
> Planungssicherheit.
>
> **Zusammensetzung:** Empfehlungstext
>
> **Qualitätskriterien:** Schlüssig
>
> **Abnahmekriterien:** Kenntnisnahme Management
>
> **Verantwortlich:** Projektmanager

2.  []{#_Toc256000038 .anchor}Grober Umsetzungsfahrplan

> **Zweck:** Der Umsetzungsfahrplan skizziert die nächsten Schritte für
> das Hauptprojekt. Er zeigt Phasen, Meilensteine und Abhängigkeiten.
> Dadurch entsteht ein realistischer Ausblick. Der Fahrplan unterstützt
> die Ressourcenplanung. Er erhöht die Entscheidungssicherheit.
>
> **Zusammensetzung:** Phasenplan
>
> **Qualitätskriterien:** Realistisch
>
> **Abnahmekriterien:** Zustimmung Auftraggeber
>
> **Verantwortlich:** Projektmanager

3.  []{#_Toc256000039 .anchor}Abnahmedokument Vorprojekt

> **Zweck:** Das Abnahmedokument bestätigt den erfolgreichen Abschluss
> des Vorprojekts. Es dokumentiert die gelieferten Produkte. Offene
> Punkte werden transparent festgehalten. Die Abnahme schafft formale
> Klarheit. Sie ist Voraussetzung für den Übergang ins Hauptprojekt.
>
> **Zusammensetzung:** Abnahmeprotokoll
>
> **Qualitätskriterien:** Vollständig
>
> **Abnahmekriterien:** Unterschrift Auftraggeber
>
> **Verantwortlich:** Auftraggeber
