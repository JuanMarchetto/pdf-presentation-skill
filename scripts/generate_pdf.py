#!/usr/bin/env python3
"""Generate PDF from HTML using WeasyPrint.

Converts a self-contained HTML document into a professional PDF with
CSS Paged Media support (headers, footers, page numbers, margins).

Usage:
    python generate_pdf.py input.html
    python generate_pdf.py input.html -o output.pdf
    python generate_pdf.py input.html -o output.pdf --title "My Report"
"""

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Generate PDF from HTML using WeasyPrint"
    )
    parser.add_argument("input", help="Input HTML file path")
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output PDF file path (default: same name as input with .pdf extension)",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Document title (injected into <title> if not already set)",
    )
    args = parser.parse_args()

    # Resolve input path
    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if not input_path.suffix.lower() in (".html", ".htm"):
        print(
            f"Warning: Input file '{input_path.name}' does not have an HTML extension.",
            file=sys.stderr,
        )

    # Resolve output path
    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = input_path.with_suffix(".pdf")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Import WeasyPrint
    try:
        from weasyprint import HTML
    except ImportError:
        print(
            "Error: WeasyPrint is not installed.\n"
            "Install it with: pip install weasyprint\n"
            "See https://doc.courtbouillon.org/weasyprint/stable/first_steps.html",
            file=sys.stderr,
        )
        sys.exit(1)

    # Read and optionally modify HTML
    html_content = input_path.read_text(encoding="utf-8")

    if args.title and "<title>" not in html_content.lower():
        html_content = html_content.replace(
            "<head>", f"<head>\n<title>{args.title}</title>", 1
        )

    # Generate PDF
    try:
        doc = HTML(string=html_content, base_url=str(input_path.parent))
        doc.write_pdf(str(output_path))
    except Exception as e:
        print(f"Error generating PDF: {e}", file=sys.stderr)
        sys.exit(1)

    # Report success
    size_kb = output_path.stat().st_size / 1024
    print(f"PDF generated: {output_path}")
    print(f"Size: {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
