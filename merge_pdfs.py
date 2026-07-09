"""Merge the exercise report PDFs into a single document.

Usage: uv run merge_pdfs.py OUTPUT.pdf INPUT.pdf [INPUT.pdf ...]

Each input becomes a top-level bookmark in the output, named after the
exercise directory it came from (e.g. ex1/report/report.pdf -> "ex1").
"""

import sys
from pathlib import Path

from pypdf import PdfWriter


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(f"usage: {Path(sys.argv[0]).name} OUTPUT.pdf INPUT.pdf [INPUT.pdf ...]")

    output, *inputs = sys.argv[1:]

    writer = PdfWriter()
    for pdf in inputs:
        label = Path(pdf).parts[0]
        before = len(writer.pages)
        writer.append(pdf, outline_item=label)
        print(f"  + {pdf}  ({len(writer.pages) - before} pages)")

    writer.write(output)
    print(f"wrote {output}  ({len(writer.pages)} pages total)")


if __name__ == "__main__":
    main()
