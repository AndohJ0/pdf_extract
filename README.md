# PDF Extract - Pilot PDF Utility Tool

A simple command-line utility for working with PDF files. This tool provides basic PDF operations including text extraction, metadata reading, and page information.

## Features

- **Text Extraction**: Extract text from all pages or specific pages
- **Metadata Reading**: Display PDF metadata including title, author, creation date, etc.
- **Page Information**: List page count, dimensions, and text statistics
- **Error Handling**: Robust error handling for common issues

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd pdf_extract
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The tool provides three main commands:

### Extract Text

Extract text from all pages:
```bash
python3 pdf_extract.py extract document.pdf
```

Extract text from a specific page:
```bash
python3 pdf_extract.py extract document.pdf --page 2
```

### Show Metadata

Display PDF metadata:
```bash
python3 pdf_extract.py metadata document.pdf
```

### List Pages

Show page information:
```bash
python3 pdf_extract.py pages document.pdf
```

### Help

Get help for any command:
```bash
python3 pdf_extract.py --help
python3 pdf_extract.py extract --help
```

## Example Output

### Metadata
```
=== PDF Metadata ===
Number of pages: 3
Title: Test PDF Document
Author: PDF Extract Tool
Subject: Test document for PDF utility
Creator: ReportLab PDF Library - www.reportlab.com
Producer: ReportLab PDF Library - www.reportlab.com
Creation Date: 2025-09-09 15:18:40+00:00
Modification Date: 2025-09-09 15:18:40+00:00
```

### Page Information
```
=== PDF Pages ===
Total pages: 3
Page 1:
  Size: 612.0 x 792.0 points
  Text length: ~255 characters

Page 2:
  Size: 612.0 x 792.0 points
  Text length: ~261 characters
```

### Text Extraction
```
--- Page 1 ---
PDF Extract Tool - Test Document
This is page 1 of the test document.
This PDF contains sample text to test extraction capabilities.
```

## Error Handling

The tool includes comprehensive error handling:
- File not found errors
- Invalid page numbers
- Corrupted PDF files
- Permission issues

## Dependencies

- Python 3.6+
- PyPDF2 3.0.1

## License

This is a pilot/proof-of-concept tool for PDF processing.