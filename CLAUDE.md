# CLAUDE.md – Projektanweisungen für EMRGPT

## Projekt

**EMRGPT** (ehem. UKLGPT / hAIppokrates) – KI-gestützter klinischer Informationsassistent für das Universitätsklinikum Leipzig (UKL). RAG-basierter Zugriff auf ~21 Mio. archivierte Patientendokumente nach SAP IS-H-Abschaltung (Oktober 2026).

- **Methodik:** PRINCE2 / Agil (Hybrid)
- **Sprache:** Alle Dokumente und Commit-Messages auf **Deutsch**
- **Markdown-Dialekt:** GitHub-Flavored Markdown (GFM)

## Repository-Struktur

```
EMRGPT/
├── Konzept_EMRGPT.md          # Hauptkonzept – Zielarchitektur (führendes Dokument)
├── PSP_EMRGPT.md              # Produktstrukturplan (PRINCE2)
├── Projektplan.md             # YouTrack-Tickets aller Phasen
├── Projektplan_Gantt.csv      # Gantt-Daten (CSV, Semikolon-getrennt)
├── Praesentation_EMRGPT.md    # Präsentation Hauptprojekt
├── Praesentation_Vorprojekt.md# Präsentation Vorprojekt
├── QUALITAETSANALYSE.md       # QA-Befunde und Risiko-Register
├── Fachablage/                # Quelldokumente (DOCX, PDF, PNG)
├── Codebeispiele/             # SNOMED, FHIR, Europe PMC API-Beispiele
├── Code-Beispiele/            # Weitere Code-Artefakte
└── CLAUDE.md                  # Diese Datei
```

## Leitdokumente und Abhängigkeiten

- **Konzept_EMRGPT.md** ist das führende Dokument. PSP und Projektplan referenzieren es.
- **PSP_EMRGPT.md** definiert die verbindliche Produktstruktur (mit dem Kunden abgestimmt).
- **Projektplan.md** enthält die YouTrack-Tickets und Meilensteine.
- **Projektplan_Gantt.csv** ist die tabellarische Gantt-Darstellung (Semikolon-Trennzeichen, UTF-8).
- Änderungen am Konzept erfordern ggf. Nachführung in PSP und Projektplan (Querverweise prüfen).

## Qualitätsregeln

1. **Versionierung:** Jede inhaltliche Änderung an Konzept, PSP oder Projektplan erhöht die Versionsnummer im Dokumentkopf und ergänzt den Änderungsvermerk.
2. **PSP-Konsistenz:** Jedes Ergebnis im Konzept muss einem PSP-Produkt zuordenbar sein.
3. **Querverweise:** Kapitelverweise (z.B. "Kap. 7.2.1") müssen nach Strukturänderungen geprüft werden.
4. **Terminologie:** Kanonischer Projektname ist **EMRGPT**. UKLGPT darf als Synonym im Konzept verwendet werden (Versionskonsistenz). Neue Dokumente verwenden ausschließlich EMRGPT.
5. **Gantt-CSV:** Semikolon-getrennt, Datumsformat `YYYY-MM-DD`, Spaltenreihenfolge wie in Projektplan_Gantt.csv definiert.

## Distributionsregeln (Pflicht-Exporte)

**WICHTIG:** Nach jeder inhaltlichen Änderung an den folgenden Quelldateien müssen die zugehörigen Exporte erzeugt und committet werden.

### Konzept_EMRGPT.md
| Export-Format | Zieldatei | Werkzeug |
|---------------|-----------|----------|
| **PDF** | `Konzept_EMRGPT.pdf` | Python (markdown + weasyprint) |
| **DOCX** | `Konzept_EMRGPT.docx` | Python (python-docx + markdown) |

### Projektplan.md
| Export-Format | Zieldatei | Werkzeug |
|---------------|-----------|----------|
| **PDF** | `Projektplan.pdf` | Python (markdown + weasyprint) |
| **DOCX** | `Projektplan.docx` | Python (python-docx + markdown) |

### PSP_EMRGPT.md
| Export-Format | Zieldatei | Werkzeug |
|---------------|-----------|----------|
| **PDF** | `PSP_EMRGPT.pdf` | Python (markdown + weasyprint) |
| **DOCX** | `PSP_EMRGPT.docx` | Python (python-docx + markdown) |
| **XML** | `PSP_EMRGPT.xml` | Python (lxml) – MindManager-kompatibles Format |

### Projektplan_Gantt.csv
| Export-Format | Zieldatei | Werkzeug |
|---------------|-----------|----------|
| **XLSX** | `Projektplan_Gantt.xlsx` | Python (openpyxl) |

### Export-Befehle (Referenz)

```bash
# PDF-Export (Markdown → HTML → PDF)
python3 -c "
import markdown, weasyprint
with open('DATEI.md') as f:
    html = markdown.markdown(f.read(), extensions=['tables','toc'])
html_doc = f'<html><head><meta charset=\"utf-8\"><style>body{{font-family:Arial,sans-serif;margin:2cm}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ccc;padding:6px 10px;text-align:left}}th{{background:#f0f0f0}}</style></head><body>{html}</body></html>'
weasyprint.HTML(string=html_doc).write_pdf('DATEI.pdf')
"

# DOCX-Export (Markdown → DOCX via python-docx)
python3 -c "
import markdown, re
from docx import Document
from docx.shared import Pt, Inches
from xml.etree import ElementTree as ET

with open('DATEI.md') as f:
    html = markdown.markdown(f.read(), extensions=['tables','toc'])

doc = Document()
style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(11)

root = ET.fromstring(f'<div>{html}</div>')
for elem in root.iter():
    if elem.tag in ('h1','h2','h3'):
        level = int(elem.tag[1])
        doc.add_heading(elem.text or '', level=level)
    elif elem.tag == 'p':
        doc.add_paragraph(elem.text or '')
doc.save('DATEI.docx')
"

# Excel-Export (CSV → XLSX)
python3 -c "
import csv, openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Gantt'
with open('Projektplan_Gantt.csv', encoding='utf-8') as f:
    for row in csv.reader(f, delimiter=';'):
        ws.append(row)
wb.save('Projektplan_Gantt.xlsx')
"

# MindManager-XML-Export (PSP → XML)
python3 -c "
from lxml import etree
import re

with open('PSP_EMRGPT.md') as f:
    lines = f.readlines()

root = etree.Element('map', version='1.0')
doc_node = etree.SubElement(root, 'node', TEXT='PSP EMRGPT')

current_h2 = None
current_h3 = None

for line in lines:
    line = line.strip()
    if line.startswith('## ') and not line.startswith('## Inhaltsverzeichnis'):
        h2_text = re.sub(r'^##\s+', '', line)
        current_h2 = etree.SubElement(doc_node, 'node', TEXT=h2_text)
        current_h3 = None
    elif line.startswith('### '):
        h3_text = re.sub(r'^###\s+', '', line)
        parent = current_h2 if current_h2 is not None else doc_node
        current_h3 = etree.SubElement(parent, 'node', TEXT=h3_text)
    elif line.startswith('| ') and '|' in line[1:]:
        cols = [c.strip() for c in line.split('|')[1:-1]]
        if cols and not all(c.startswith('-') for c in cols):
            if cols[0] and not cols[0].startswith('PSP-Nr') and not cols[0].startswith('---'):
                label = f'{cols[0]}: {cols[1]}' if len(cols) > 1 else cols[0]
                parent = current_h3 if current_h3 is not None else (current_h2 if current_h2 is not None else doc_node)
                etree.SubElement(parent, 'node', TEXT=label)

tree = etree.ElementTree(root)
tree.write('PSP_EMRGPT.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')
"
```

### Ablauf bei Dokumentänderungen

1. Markdown-Quelldatei bearbeiten
2. Versionsnummer und Änderungsvermerk aktualisieren
3. **Alle zugehörigen Exporte erzeugen** (siehe Tabellen oben)
4. Quelldatei UND Exportdateien gemeinsam committen

## Commit-Konventionen

- **Sprache:** Deutsch
- **Format:** Kurze Zusammenfassung (max. 72 Zeichen), gefolgt von optionaler Detailbeschreibung
- **Beispiele:**
  - `Konzept v2.1: FHIR-Konformität Kap. 3.2 ergänzt`
  - `PSP: Produkt 3.10 (API-Gateway) hinzugefügt`
  - `Projektplan: Phase-2-Tickets aktualisiert`
  - `Export: PDF/DOCX/XLSX nach Konzept-Update regeneriert`

## Hinweise für Claude

- Vor Änderungen an Konzept, PSP oder Projektplan immer die **aktuelle Version** lesen.
- Nach inhaltlichen Änderungen die **Distributionsregeln** befolgen (Exporte erzeugen).
- Bei Strukturänderungen (Kapitel verschoben/hinzugefügt) alle **Querverweise** in allen drei Dokumenten prüfen.
- **Projektplan_Gantt.csv** bei Ticket-Änderungen synchron halten.
- Die **QUALITAETSANALYSE.md** bei größeren Änderungen konsultieren und ggf. aktualisieren.
