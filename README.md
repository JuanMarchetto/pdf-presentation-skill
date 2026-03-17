# PDF Presentation Skill for Claude Code

Generate professional PDF reports and presentations from structured content. Converts evaluations, proposals, and assessments into polished documents with score visualizations, styled tables, and print-optimized layouts.

## What It Does

When you ask Claude Code to "generate a PDF", "export this evaluation", or "create a report", this skill:

1. Analyzes the content to present (evaluation results, proposals, reports)
2. Generates a self-contained HTML document with inline CSS and SVG graphics
3. Converts it to PDF using WeasyPrint with CSS Paged Media support
4. Outputs a professional document with page numbers, headers, and proper typography

### Supported Content Types

- **Architect evaluations** -- Value Matrix, Opportunity Score, risk assessments
- **Project proposals** -- problem statements, solutions, timelines, budgets
- **Comparison analyses** -- side-by-side option evaluation with scores
- **General reports** -- any structured document with sections and findings
- **Meeting notes** -- agendas, decisions, action items

## Requirements

- Python 3.8+
- [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)

### System Dependencies (for WeasyPrint)

WeasyPrint requires some system libraries. On Ubuntu/Debian:

```bash
sudo apt install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0
```

On macOS:

```bash
brew install pango
```

## Installation

### Method 1: Clone directly

```bash
git clone https://github.com/juanmarchetto/pdf-presentation-skill.git
```

Add the skill directory to your Claude Code project configuration.

### Method 2: As a git submodule

```bash
cd your-project/
git submodule add https://github.com/juanmarchetto/pdf-presentation-skill.git skills/pdf-presentation
```

### Method 3: Manual download

Download the repository contents and place them in a directory accessible to Claude Code. Ensure `SKILL.md` is at the root of the skill directory.

## Installing WeasyPrint

```bash
pip install weasyprint
```

Verify the installation:

```bash
python -c "from weasyprint import HTML; print('WeasyPrint is ready')"
```

## Usage

Once installed, ask Claude Code to generate PDFs naturally:

```
Generate a PDF report of this evaluation
```

```
Export the architect assessment to PDF
```

```
Create a professional PDF proposal for the project we just discussed
```

```
Make a PDF presentation comparing these three options
```

The skill will produce a PDF in the current working directory (or a path you specify) and report the output location.

## Template

The included HTML template (`assets/templates/report.html`) provides:

- Professional cover page with gradient background
- Executive summary with recommendation badges (Go / Caution / No-Go)
- Score gauge and bar chart visualizations (inline SVG)
- Value Matrix tables with alternating row colors
- Risk assessment matrix with color-coded severity
- Numbered recommendation lists
- Timeline/next-steps layout
- CSS Paged Media: page numbers, running headers, proper margins

The template uses Jinja2-compatible placeholders (`{{ variable }}`), but Claude Code generates the full HTML directly -- no template engine is required at runtime.

## Project Structure

```
pdf-presentation-skill/
├── SKILL.md                      # Skill definition and instructions
├── .claude-plugin/plugin.json    # Plugin metadata
├── README.md                     # This file
├── LICENSE                       # MIT License
├── .gitignore
├── scripts/
│   └── generate_pdf.py           # HTML-to-PDF conversion script
└── assets/
    └── templates/
        └── report.html           # Reference HTML template
```

## License

MIT License. Copyright (c) 2026 Juan Marchetto.
