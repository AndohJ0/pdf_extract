#!/usr/bin/env python3
"""
PDF Extract - A pilot PDF utility tool

This tool provides basic PDF operations including:
- Text extraction
- Metadata extraction
- Page information
"""

import argparse
import sys
import os
from PyPDF2 import PdfReader
from PyPDF2.errors import PyPdfError


def extract_text(pdf_path, page_num=None):
    """Extract text from PDF file."""
    try:
        reader = PdfReader(pdf_path)
        
        if page_num is not None:
            if page_num < 1 or page_num > len(reader.pages):
                print(f"Error: Page {page_num} is out of range. PDF has {len(reader.pages)} pages.", file=sys.stderr)
                return False
            
            page = reader.pages[page_num - 1]  # Convert to 0-based index
            text = page.extract_text()
            print(f"--- Page {page_num} ---")
            print(text)
        else:
            # Extract text from all pages
            for i, page in enumerate(reader.pages, 1):
                text = page.extract_text()
                print(f"--- Page {i} ---")
                print(text)
                print()  # Add blank line between pages
        
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.", file=sys.stderr)
        return False
    except PyPdfError as e:
        print(f"Error: Failed to process PDF file. {str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: Unexpected error occurred. {str(e)}", file=sys.stderr)
        return False


def extract_metadata(pdf_path):
    """Extract metadata from PDF file."""
    try:
        reader = PdfReader(pdf_path)
        
        print("=== PDF Metadata ===")
        print(f"Number of pages: {len(reader.pages)}")
        
        metadata = reader.metadata
        if metadata:
            if metadata.title:
                print(f"Title: {metadata.title}")
            if metadata.author:
                print(f"Author: {metadata.author}")
            if metadata.subject:
                print(f"Subject: {metadata.subject}")
            if metadata.creator:
                print(f"Creator: {metadata.creator}")
            if metadata.producer:
                print(f"Producer: {metadata.producer}")
            if metadata.creation_date:
                print(f"Creation Date: {metadata.creation_date}")
            if metadata.modification_date:
                print(f"Modification Date: {metadata.modification_date}")
        else:
            print("No metadata found in PDF.")
            
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.", file=sys.stderr)
        return False
    except PyPdfError as e:
        print(f"Error: Failed to process PDF file. {str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: Unexpected error occurred. {str(e)}", file=sys.stderr)
        return False


def list_pages(pdf_path):
    """List page information from PDF file."""
    try:
        reader = PdfReader(pdf_path)
        
        print("=== PDF Pages ===")
        print(f"Total pages: {len(reader.pages)}")
        
        for i, page in enumerate(reader.pages, 1):
            print(f"Page {i}:")
            if hasattr(page, 'mediabox'):
                width = float(page.mediabox.width)
                height = float(page.mediabox.height)
                print(f"  Size: {width:.1f} x {height:.1f} points")
            
            # Count approximate text length
            text = page.extract_text()
            print(f"  Text length: ~{len(text)} characters")
            print()
            
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.", file=sys.stderr)
        return False
    except PyPdfError as e:
        print(f"Error: Failed to process PDF file. {str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: Unexpected error occurred. {str(e)}", file=sys.stderr)
        return False


def main():
    """Main entry point for the PDF utility."""
    parser = argparse.ArgumentParser(
        description='PDF Extract - A pilot PDF utility tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s extract sample.pdf              # Extract all text
  %(prog)s extract sample.pdf --page 1     # Extract text from page 1
  %(prog)s metadata sample.pdf             # Show PDF metadata
  %(prog)s pages sample.pdf                # List page information
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Extract text command
    extract_parser = subparsers.add_parser('extract', help='Extract text from PDF')
    extract_parser.add_argument('pdf_file', help='Path to PDF file')
    extract_parser.add_argument('--page', '-p', type=int, help='Extract text from specific page number')
    
    # Metadata command
    metadata_parser = subparsers.add_parser('metadata', help='Show PDF metadata')
    metadata_parser.add_argument('pdf_file', help='Path to PDF file')
    
    # Pages command
    pages_parser = subparsers.add_parser('pages', help='List page information')
    pages_parser.add_argument('pdf_file', help='Path to PDF file')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Validate file exists
    if not os.path.isfile(args.pdf_file):
        print(f"Error: File '{args.pdf_file}' does not exist.", file=sys.stderr)
        return 1
    
    # Execute the requested command
    success = False
    if args.command == 'extract':
        success = extract_text(args.pdf_file, args.page)
    elif args.command == 'metadata':
        success = extract_metadata(args.pdf_file)
    elif args.command == 'pages':
        success = list_pages(args.pdf_file)
    
    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())