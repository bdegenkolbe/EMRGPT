# 02-27 Besprechung: Integration des Archivsystems und Datenschutz

### Maßnahmen
- @Speaker 8 - Nach interner Freigabe die AVVs an Speaker 6 und Team weiterleiten. - Vor dem Termin am Mittwoch.
- @Speaker 3 - Fordert eine Architekturskizze an, um dem Datenschützer den technischen Ablauf verständlich zu machen. - Speaker 1 hat die Bereitstellung zugesagt.
- @[Speaker 6] - Die spezifische Datenschutzlage in Sachsen am kommenden Mittwoch klären. - [Mittwoch].
- @[Unbekannt, wahrscheinlich das anbietende Team] - Entsprechende Datenschutzdokumente an die Gegenseite zusenden. - [Unspezifisch].
- @Unbestimmt - Eine detaillierte Prüfung der Datenqualität und Festlegung des Vorgehens zur Dokumentenmigration ist erforderlich, um eine genaue Preisindikation zu erstellen.
- @Frau Krass & Herr Vasipki (intern) - Die unterschiedlichen Positionen zum Zeitplan werden intern mit Herrn Dr. Vasipki besprochen.
- @Projektteam - Das Thema wird gegebenenfalls in den Lenkungsausschuss eingebracht, um eine finale Entscheidung herbeizuführen.
- @Projektteam (im Gespräch mit "Sie") - Das Projektteam wird sich bezüglich der Dokumente melden.
- @Anbieter (im Gespräch mit "wir") - Der Anbieter wartet auf Rückmeldung vom Projektteam.
### Wichtige Entscheidungen
- Der vorgeschlagene Ansatz für die Altdatenintegration ist ein ereignisbasierter Abruf aus Hype Media bei der Aufnahme eines neuen Patientenfalls, anstatt eines initialen Massenimports aller Dokumente.
- Der effizienteste Weg zur Klärung der Datenschutzbedenken ist, dem Datenschützer vorab die AVVs zur Prüfung vorzulegen, damit dieser spezifische Bedenken zurückmelden kann. - Dies soll einen proaktiven Austausch ermöglichen und einen unproduktiven Termin verhindern.
- Für die Anbindung des Archivsystems (hypeMedia) zur Nutzung historischer Daten wird ein Aufwand von 10 bis 20 Personentagen geschätzt. - Basierend auf Erfahrung mit ähnlichen Systemen.
- Der geschätzte Aufwand von 10-20 Tagen deckt auch die technischen Feinheiten ab, die sich aus der Verarbeitung der OCR-erkannten PDF-Dokumente ergeben. - Einschätzung von Speaker 2.
- Die Entscheidung über den Zeitplan liegt außerhalb der Kompetenz des Projektteams und muss auf höherer Ebene geklärt werden.
### Detailliertes Protokoll
[01:09-03:53] **Eine Vorstellungsrunde der anwesenden Parteien und ihrer jeweiligen Rollen im Projekt wird durchgeführt.**
- Die Vorstellung beginnt mit den Teilnehmern von 4K Analytics, die sich als unterstützende Berater für Carina bei der M-KIS-Umsetzung vorstellen.
  - 4K Analytics hat seit 7-8 Jahren Erfahrung mit Projekten im UKL, einschließlich des Aufbaus eines Data Warehouse.
  - Ihr aktueller Auftrag ist es, die M-KIS-Implementierung zu unterstützen, insbesondere die Daten zu analysieren und eine Entscheidungsvorlage zu erstellen.
  - Anwesend sind der Chef des Unternehmens und der Projektleiter für das Warehouse-Projekt seitens 4K, der regelmäßig mit Frau Dr. Kundi im Austausch steht.
- Es folgen die Vertreter von Mayerhofer und deren Partner.
  - Samira Graß stellt sich als Account Managerin für das UKL bei Mayerhofer vor, zuständig für zukünftige Projekte und vertragliche Themen.
  - Martin Wetzel (Mayerhofer) ist Produktmanager für medizinische Dokumentation und verantwortlich für die Integration des Averbes-Produkts "Medical Dialogue" (bei Mayerhofer "Gesprächsdokumentation" genannt) in M-KIS.
  - Basil Ostermann (Mayerhofer) ist für die Arztbriefschreibung und die Integration von "Medical Peak Krise" zuständig.
- Abschließend stellen sich die Vertreter von Averbes vor.
  - Silvia Klappern ist Partnermanagerin bei Averbes, managt die Produkte und steht in intensivem Austausch mit Mayerhofer. Sie ist primär für die kaufmännischen Aspekte zuständig.
  - Marc Sander ist der technische Ansprechpartner für die Integration von Averbes-Produkten in das M-KIS.
[04:02-06:23] **Die zentrale Anforderung des UKL ist die Integration eines externen Dokumentenarchivs (Hype Media) in die neue Lösung, um die Patientenhistorie umfassend analysieren zu können.**
- Das UKL betont, dass die Anbindung ihres externen Dokumenten-Repositorys, Hype Media, von entscheidender Bedeutung ist.
  - Hype Media enthält über 20 Millionen Dokumente und stellt den wertvollsten Datenschatz für die Analyse der Patientenhistorie dar.
  - Nach der M-KIS-Umstellung im Oktober wird die Datenbasis im neuen System anfangs gering sein, was die Altdaten in Hype Media umso wichtiger macht.
- Die Hauptfrage ist, ob und wie eine Anbindung eines zweiten, externen Repositorys (Hype Media) neben der M-KIS-Integration technisch realisierbar ist.
  - Es wird um ein tieferes technisches Verständnis gebeten, da sich das UKL mit 4K Analytics in der Konzeptionsphase für die Umsetzung befindet.
  - Neben der technischen Machbarkeit sind auch die resultierenden Entwicklungsaufwände seitens Averbes/Mayerhofer und ein möglicher Zeitplan von Interesse, insbesondere im Kontext der Konzentration auf die M-KIS-Gesamteinführung.
  - Das Ziel ist es, Einblick in die technische Architektur einer solchen Lösung zu erhalten, um eine fundierte Bewertung durchführen zu können.
[06:25-09:30] **Die technische Herausforderung der Integration von Altdaten aus SAP, die als PDFs in Hype Media archiviert werden, wird detailliert erläutert.**
- Es wird bestätigt, dass Mayerhofer Kenntnis von der UKL-Infrastruktur und dem Hype Media Dokumenten-Repository hat.
- Die M-KIS-Einführung folgt einem Brownfield-Ansatz, bei dem nicht alle Altdaten aus SAP in das neue System migriert werden.
  - Ein Satz von Altdaten verbleibt in SAP und wird in Hype Media archiviert.
  - Hype Media wurde gewählt, da es als zertifiziertes System die Verfügbarkeit medizinischer Dokumente für über 100 Jahre sicherstellt.
- Der Prozess der Archivierung in Hype Media wird beschrieben: Strukturierte Daten aus SAP werden in PDFs umgewandelt und in Hype Media gespeichert. Der Zugriff erfolgt dann über einen "Rack-Ansatz" auf diese PDFs. Dieser Weg wird als "etwas doof", aber rechtssicher bezeichnet.
- Neben den SAP-Kerndaten (ISH Med) müssen auch Daten aus diversen Randsystemen (z.B. Register) berücksichtigt werden, die ebenfalls in Hype Media landen.
- Die Herausforderung besteht darin, dass die Averbes-Lösung standardmäßig nur auf die M-KIS-Instanz zugreift, während die Mitarbeiter, besonders zu Beginn nach dem Go-Live im Oktober, einen hohen Bedarf am Zugriff auf die Altdaten in Hype Media haben werden.
[09:37-11:21] **Die Funktionsweise der Datenverarbeitung in der Cloud und die lokale Speicherung von Vektordatenbanken werden geklärt.**
- Eine Frage betrifft das Hosting von Averbes in Schweden und die Verarbeitung der ca. 30 Millionen zu erwartenden Dokumente. Es wird geklärt, wie die Daten zwischen der On-Premise-Installation und der Cloud ausgetauscht werden.
- Klarstellung durch Averbes:
  - Dokumente werden nur temporär zur Verarbeitung im Rahmen des RAG-Ansatzes in die Cloud (Schweden) geschickt.
  - Die eigentliche Speicherung aller Daten ("on prem") erfolgt lokal.
  - Die Vektordatenbank wird ebenfalls lokal gespeichert. Die Embeddings (Vektoren) werden zwar in der Cloud berechnet, aber dann in der lokalen Datenbank abgelegt.
- Diese Klärung wird als Vereinfachung des Sachverhalts positiv aufgenommen.
- Averbes schlägt vor, eine Architekturskizze zu präsentieren, um zu zeigen, wie Hype Media angebunden werden könnte und weitere technische Fragen zu beantworten.
[11:23-14:41] **Averbes präsentiert eine technische Architekturskizze zur Integration von M-KIS und externen Dokumentensystemen wie Hype Media.**
- Die präsentierte Architektur zeigt, wie das Averbes-Produkt (Medical Summary) mit M-KIS und einem Large Language Model (LLM) interagiert und wie ein externes Content Management System (CMS) wie Hype Media angebunden werden kann.
- Der Standard-Datenfluss von M-KIS zu Averbes erfolgt über eine HL7-Schnittstelle. Alle Daten (strukturierte Daten, Dokumente) werden im Medical Summary Backend lokal (on-prem) persistiert.
- Für die Anbindung historischer Daten aus Hype Media wird ein ereignisbasierter Ansatz vorgeschlagen:
  - Eine REST-API (idealerweise FHIR-basiert) von Hype Media würde genutzt, um Daten abzurufen.
  - Wenn ein neuer Fall für einen Patienten in M-KIS angelegt wird (z.B. via ADT-Nachricht), löst dieses Ereignis eine Abfrage aus.
  - Basierend auf der Patienten-ID werden dann alle historischen Dokumente zu diesem Patienten aus Hype Media in die Medical Summary geladen.
  - Ein vollständiger initialer Import aller 20+ Millionen Dokumente wird als "too much" angesehen.
- Eine weitere Möglichkeit wäre die Anbindung an einen HL7-Verteiler, um neue Dokumente, die nicht über M-KIS laufen, direkt in das Averbes-System zu pushen.
- **Wichtige Entscheidung:** Der vorgeschlagene Ansatz für die Altdatenintegration ist ein ereignisbasierter Abruf aus Hype Media bei der Aufnahme eines neuen Patientenfalls, anstatt eines initialen Massenimports aller Dokumente.
[14:44-15:10] **Die Komponenten der Averbes-Lösung werden den jeweiligen Umgebungen (On-Premise vs. Cloud) zugeordnet.**
- Auf Nachfrage wird die Verteilung der Systemkomponenten bestätigt:
  - **On-Premise:** Das Medical Summary Backend und die Health Discovery NLP Engine sind Produkte von Averbes und werden lokal installiert.
  - **Cloud:** Das genutzte Large Language Model (LLM) wird bei Azure in der EU-GA-Zone in Schweden gehostet.
[15:16-16:15] **Die Qualität und Art der verfügbaren Schnittstellen von Hype Media sind noch in Klärung, Averbes zeigt sich jedoch flexibel.**
- Es wird angemerkt, dass die Qualität der Hype-Media-Schnittstellen davon abhängt, was das UKL eingekauft hat.
- Das UKL bestätigt, dass dies noch in Diskussion mit Hype Media ist. Während Hype Media eine FHIR-Schnittstelle vorschlägt, bevorzugt das UKL den direkten Zugriff über eine REST-API, da FHIR in diesem Kontext keinen Mehrwert biete.
- Averbes erklärt, dass sie Erfahrung mit verschiedenen Schnittstellentypen haben (FHIR, proprietäre REST-APIs) und eine Anbindung grundsätzlich möglich ist.
[16:20-18:04] **Die exklusive Partnerschaft zwischen Mayerhofer und Averbes wird bestätigt; es gibt Verzögerungen bei geplanten Teststellungen.**
- Es wird geklärt, dass Mayerhofer im Bereich der Gesprächsdokumentation exklusiv mit Averbes zusammenarbeitet.
- Üblicherweise wird eine bis zu dreimonatige Testphase durchgeführt, in der Anwender die Möglichkeit haben, die Software auszuprobieren, bevor eine Lizenzierung erforderlich ist.
- In der Testphase fallen vertrieblich gesehen nur Kosten für Dienstleistungen wie Schulungen und Einrichtung an.
- Die Asklepios Kliniken sind derzeit pilotiert und befinden sich nach aktuellem Kenntnisstand noch in der Testphase, bevor sie in den Live-Betrieb übergehen.
- Für Greifswald (UMG) ist geplant, ebenfalls eine Testphase durchzuführen, die in die Lizenzierung und den Live-Betrieb münden soll. Dieser Prozess hat sich jedoch aufgrund eines internen IT-Leiterwechsels verzögert.
[18:07-21:01] **Es bestehen Bedenken hinsichtlich des Datenschutzes bei der Nutzung von Azure OpenAI, insbesondere im Hinblick auf die strengen Vorschriften in Sachsen, die Cloud-Lösungen generell einschränken.**
- Die Schnittstelle zu Azure OpenAI wird als potenzielles Diskussionsthema mit Datenschützern wahrgenommen. Es wird die Notwendigkeit betont, ein umfassendes Datenschutzkonzept ("100 Seiten Papier") vorlegen zu können, das die Datensicherheit garantiert, inklusive eines Auftragsverarbeitungsvertrags (AVV) mit Microsoft und OpenAI.
- Als Alternative zu Azure wird der Anbieter Stackit vorgestellt, der innerhalb Deutschlands agiert.
  - Die Wahl zwischen Azure und Stackit hängt oft von der Haltung des jeweiligen Datenschützers ab; einige lehnen Microsoft grundsätzlich ab.
  - Stackit ist in der Regel mit höheren Kosten für den Kunden verbunden.
- Es wird klargestellt, dass die genutzten Modelle von OpenAI über Azure gehostet werden. Es muss vertraglich sichergestellt sein, dass die Daten nicht zum Training der Modelle verwendet werden.
- Ein Verweis auf das Klinikum Rheine (ein Tausend-Betten-Haus), das Azure nutzt, wird als nicht direkt vergleichbar für Sachsen erachtet, da in Sachsen landesweit keine Freigabe für Cloud-Lösungen bestehe.
- Es wird die Sorge geäußert, dass möglicherweise ein teures Datenschutzgutachten (z.B. von KPMG) erforderlich sein könnte, um die rechtliche Absicherung zu gewährleisten, was zusätzliche Kosten von ca. 100.000 € verursachen könnte.
[21:02-23:50] **Zur Vorbereitung auf ein anstehendes Gespräch mit dem Datenschützer werden konkrete Unterlagen angefordert und deren Bereitstellung zugesagt.**
- Es ist ein Termin mit dem Datenschützer für den kommenden Mittwochvormittag angesetzt.
- Speaker 8 schlägt vor, die standardmäßigen Auftragsverarbeitungsverträge (AVVs), die die Unterauftragnehmer und Prozesse detaillieren, für den Termin zur Verfügung zu stellen.
  - **Wichtige Entscheidung:** Der effizienteste Weg zur Klärung der Datenschutzbedenken ist, dem Datenschützer vorab die AVVs zur Prüfung vorzulegen, damit dieser spezifische Bedenken zurückmelden kann. - Dies soll einen proaktiven Austausch ermöglichen und einen unproduktiven Termin verhindern.
  - **Maßnahme:** @Speaker 8 - Nach interner Freigabe die AVVs an Speaker 6 und Team weiterleiten. - Vor dem Termin am Mittwoch.
- Zusätzlich wird angeregt, die Dokumente zu prüfen, die Patrick bereits in Greifswald eingereicht hatte.
- **Maßnahme:** @Speaker 3 - Fordert eine Architekturskizze an, um dem Datenschützer den technischen Ablauf verständlich zu machen. - Speaker 1 hat die Bereitstellung zugesagt.
[23:53-24:49] **Es wird erörtert, ob die Einschränkung der Cloud-Nutzung in Sachsen absolut ist und ob es Verhandlungsspielraum gibt, wobei ein Update zum aktuellen Stand erforderlich ist.**
- Die Information, dass Azure in Sachsen ausgeschlossen sei ("föderales Wissen"), war einigen Teilnehmern neu.
- Es bleibt zu klären, ob dies eine unumstößliche Vorgabe ist, die zwangsläufig zu einer Lösung wie Stackit führt, oder ob es im Prozess, z.B. durch Nachweise und Verhandlungen, Gestaltungsmöglichkeiten gibt.
- Als Referenz wird eine aktuelle Ausschreibung für "Langdoc" vom Staatsministerium Sachsen erwähnt, um den Sachverhalt weiter zu prüfen. Der letzte Stand des Sprechers basierte auf früheren Erfahrungen mit SAP-Lösungen, bei denen das Thema Cloud schnell abgelehnt wurde.
- Es wird anerkannt, dass man sich auf den aktuellen Stand bringen muss, was die Regelungen betrifft.
[24:53-25:37] **Es besteht Unsicherheit bezüglich einer landesspezifischen Datenschutzregelung in Sachsen, die möglicherweise den Einsatz von Cloud-Technologien bei Universitätskliniken einschränkt.**
- Speaker 5 und Speaker 6 sind von der Information überrascht, dass es in Sachsen eine spezielle Regelung geben könnte, die sich gegen Cloud-Nutzung ausspricht.
- Speaker 6 vermutet, dass es sich dabei nicht zwingend um eine Landesverordnung handelt, sondern möglicherweise um eine Vereinbarung der Universitätskliniken mit dem Landesdatenschützer, die aus einer fehlenden Cloud-Strategie resultierte.
- Es wird eingeräumt, dass diese Information veraltet sein könnte, falls inzwischen eine Cloud-Strategie entwickelt wurde.
- **Maßnahme:** @[Speaker 6] - Die spezifische Datenschutzlage in Sachsen am kommenden Mittwoch klären. - [Mittwoch].
[25:40-28:10] **Es wird diskutiert, wie mit dem Widerstand von Datenschützern in Sachsen umgegangen werden kann, insbesondere im Hinblick auf US-amerikanische Hyperscaler.**
- Speaker 8 schlägt vor, Referenzprojekte aus anderen Bundesländern zu dokumentieren und zu übermitteln, um zu zeigen, dass die Technologie deutschlandweit bereits im Einsatz ist.
- Speaker 8 bietet an, bei Gesprächen mit den Datenschützern unterstützend mitzuwirken.
- Speaker 6 vergleicht die unterschiedlichen Haltungen der Datenschützer in den Bundesländern mit der langwierigen Entwicklung der elektronischen Patientenakte.
- Das Kernproblem, warum Datenschützer Bedenken haben könnten, ist das Zugriffsrecht von US-Behörden auf Daten, die bei amerikanischen Hyperscalern (wie Azure) gehostet werden (z. B. durch den CLOUD Act).
- Speaker 6 merkt an, dass es alternative deutsche Anbieter wie Arvato (Health Care RZ) oder Telekom gibt, die ebenfalls Hyperscaling ermöglichen und diese Abhängigkeit vermeiden würden.
- Es wird festgehalten, dass Averbes selbst keine lokal gehosteten Open-Source-Modelle anbietet, da dies nicht gut skaliert. Averbes setzt auf Hyperscaler.
[28:14-29:26] **Die technische Umsetzbarkeit und der nächste Schritt im Datenschutzprozess werden geklärt.**
- Speaker 2 bestätigt, dass die LLM-APIs auf offenen Standards basieren, weshalb es technisch unerheblich ist, ob die Lösung on-premise oder in der Cloud betrieben wird.
- Speaker 6 stellt fest, dass für das Erstellen von Arztbriefen Patientendaten zwangsläufig in der Azure-Cloud durch die LLMs verarbeitet werden müssen.
- **Maßnahme:** @[Unbekannt, wahrscheinlich das anbietende Team] - Entsprechende Datenschutzdokumente an die Gegenseite zusenden. - [Unspezifisch].
- Als nächster Schritt wird definiert, dass nach Zusendung der Dokumente geprüft wird, ob der Datenschützer weitere Unterlagen anfordert oder wie seine Entscheidung ausfällt.
[29:26-30:22] **Die Funktionsweise der Berechtigungssteuerung wird erläutert.**
- Es wird bestätigt, dass das Berechtigungskonzept des KIS (Klinikinformationssystem, MKIS) übernommen wird. Ein Benutzer, der im KIS Zugriffsrechte auf einen Patienten hat, erhält diese auch in der neuen Anwendung.
- Die technische Umsetzung erfolgt über Single Sign-On (SSO) und einen Identity Provider, der das OIDC-Protokoll nutzt. Die Berechtigungen werden so durchgeschleust.
- Speaker 5 bestätigt, dass der Identity Provider Teil der NEXT-Betriebsumgebung ist und zum relevanten Zeitpunkt (1.10.) mit der Averbes-Lösung kommunizieren kann.
[30:23-33:22] **Die Kosten und Aufwände für die Integration zusätzlicher Systeme werden geschätzt.**
- Speaker 6 fragt nach den Projektkosten für die Anbindung des Archivs (hypeMedia) und die Anpassungen, insbesondere im Hinblick auf den Stichtag 1.10.
- **Wichtige Entscheidung:** Für die Anbindung des Archivsystems (hypeMedia) zur Nutzung historischer Daten wird ein Aufwand von 10 bis 20 Personentagen geschätzt. - [Basierend auf Erfahrung mit ähnlichen Systemen].
- Die Anbindung an das Identity Management wird als Standardfunktion des Produkts bestätigt und verursacht keine zusätzlichen Kosten.
- Speaker 5 präzisiert, dass die Identity-Management-Funktion zwar existiert, aber zum Stichtag 1.10. erst vollständig ausgerollt sein wird. Es entstehen dadurch keine Zusatzkosten.
- Der geschätzte Entwicklungsaufwand von 10-20 Tagen für die hypeMedia-Anbindung käme zu den Kosten einer Teststellung hinzu, die bereits angeboten wurde.
[33:29-36:08] **Die technische Integration von hypeMedia und die Verarbeitung der darin enthaltenen PDF-Daten werden detailliert besprochen.**
- Die Anbindung von hypeMedia erfordert keine Änderung an der Benutzeroberfläche. Die Software holt sich im Hintergrund automatisch die Dokumente, sobald eine neue Patienten-ID vom MKIS gemeldet wird. Die Daten werden in die bestehende Ansicht (Medical Summary) integriert.
- Ein technisches Problem wird identifiziert: Die Daten in hypeMedia liegen als PDFs vor und sind nicht maschinenlesbar.
- Seit letzter Woche ist eine OCR-Funktion in hypeMedia implementiert. Es ist unklar, ob diese auch für die Millionen von Bestandsdokumenten rückwirkend angewendet wird.
- Speaker 6 merkt an, dass man prüft, ob die strukturierten FHIR-Daten direkt genutzt werden können, um den ineffizienten Prozess (Struktur -&gt; PDF -&gt; OCR -&gt; Struktur) zu vermeiden.
- **Wichtige Entscheidung:** Der geschätzte Aufwand von 10-20 Tagen deckt auch die technischen Feinheiten ab, die sich aus der Verarbeitung der OCR-erkannten PDF-Dokumente ergeben. - [Einschätzung von Speaker 2].
[36:10-37:37] **Die Modelle können in der Regel mit Dokumenten unterschiedlicher Qualitätsstufen umgehen, obwohl sehr schlechte Qualität eine Verarbeitung verhindern kann.**
- Es wurde die Sorge geäußert, dass Dokumente in den Archivsystemen uneinheitlich sind, z.B. durch mehrfache Scans mit unterschiedlichen Zeitstempeln oder durch Handyfotos.
- Es wurde gefragt, ob die Modelle bis zum 1. Oktober in der Lage sein werden, mit dieser variablen Qualität umzugehen, um ein qualitativ hochwertiges Ergebnis zu gewährleisten.
- Die Erfahrung aus Referenzprojekten zeigt, dass die Verarbeitung von Dokumenten verschiedener Qualitätsstufen in der Regel gut funktioniert und fast immer eine Lösung gefunden wird.
[37:39-42:31] **Die Qualität der Dokumentenklassifikation (KDL-Klassifizierung) ist ein kritischer Faktor für die Medical Summary und könnte den Dienstleistungsaufwand erheblich beeinflussen.**
- Die KDL-Klassifizierung ist entscheidend für die Filterfunktion der Medical Summary, um Dokumententypen wie Arztbriefe oder Laborbefunde unterscheiden zu können.
- Es besteht Unsicherheit über die Qualität der bestehenden Klassifizierung im Archiv. Die Hypothese wurde aufgestellt, dass das Archiv einer "Müllhalde" gleicht, in die unsortiert PDF-Dateien und Bilder abgelegt werden.
- Eine systematische KDL-Klassifizierung durch den Scandienstleister erfolgt erst seit zwei Jahren und wurde vermutlich nicht rückwirkend für ältere Dokumente angewendet.
- Dieser Mangel an durchgehender Klassifizierung könnte den Dienstleistungsaufwand über die veranschlagten 20 Tage hinaus erhöhen.
- Es wurden verschiedene Lösungsansätze für den Umgang mit unklassifizierten oder alten Dokumenten diskutiert:
  - Ein gestaffeltes Vorgehen, bei dem zunächst nur Dokumente der letzten Jahre importiert werden, um eine Überlastung zu vermeiden.
  - Ein ADT-basierter Ansatz: Dokumente werden erst dann verarbeitet ("Embedding"), wenn ein neuer Patient durch eine ADT-Meldung registriert wird. Dies vermeidet die Massenverarbeitung von Millionen historischer Dokumente auf einmal.
  - Der Einsatz eines vorgelagerten "Erkennungsprompts", um den Dokumententyp (z. B. Arztbrief, OP-Bericht) automatisch zu identifizieren.
  - Die Implementierung einer Korrekturfunktion in der Anwendung, die es Nutzern ermöglicht, falsch klassifizierte Dokumente manuell richtig zuzuordnen.
- Es wurde festgestellt, dass eine genaue Aufwandsschätzung für die weitere Konzeption schwierig ist, solange der genaue Grad der schlechten Dokumentenqualität unbekannt ist.
- **Aktionspunkt:** @Unbestimmt - Eine detaillierte Prüfung der Datenqualität und Festlegung des Vorgehens zur Dokumentenmigration ist erforderlich, um eine genaue Preisindikation zu erstellen.
[42:35-44:28] **Es besteht ein strategischer Konflikt bezüglich des Zeitplans für die Einführung des neuen Systems zum 1. Oktober.**
- Das Kernprojektteam in Leipzig präferiert eine Verschiebung des Projekts, um den Fokus zunächst auf die laufende KIS-Einführung zu legen.
- Als Gründe werden die bevorstehenden Teststellungen, laufende Anwenderschulungen und die generelle Unvertrautheit der Nutzer mit dem neuen KIS genannt.
- Demgegenüber steht eine hochpriorisierte Forderung der Vorstandsebene, am 1. Oktober eine funktionierende Dokumentenübersicht bereitzustellen.
- Die Befürchtung ist, dass es zu erheblichem Widerstand unter den Ärzten führen würde, wenn sie sich durch unstrukturierte Dokumente arbeiten müssten.
- **Wichtige Entscheidung:** Die Entscheidung über den Zeitplan liegt außerhalb der Kompetenz des Projektteams und muss auf höherer Ebene geklärt werden.
- **Aktionspunkt:** @Frau Krass & Herr Vasipki (intern) - Die unterschiedlichen Positionen zum Zeitplan werden intern mit Herrn Dr. Vasipki besprochen.
- **Aktionspunkt:** @Projektteam - Das Thema wird gegebenenfalls in den Lenkungsausschuss eingebracht, um eine finale Entscheidung herbeizuführen.
[44:28-44:54] **Die nächsten Schritte und der Abschluss des Gesprächs wurden vereinbart.**
- **Aktionspunkt:** @Projektteam (im Gespräch mit "Sie") - Das Projektteam wird sich bezüglich der Dokumente melden.
- **Aktionspunkt:** @Anbieter (im Gespräch mit "wir") - Der Anbieter wartet auf Rückmeldung vom Projektteam.