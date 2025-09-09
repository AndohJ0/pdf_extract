import PyPDF2
import re
import sys
import os

def extract_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except:
        return None

def extract_numbers(text):
    numbers = []
    # Find all numbers with commas and decimals
    matches = re.findall(r'[\d,]+\.?\d*', text)
    for match in matches:
        # Remove commas and convert to float
        clean_num = match.replace(',', '')
        try:
            num = float(clean_num)
            if num > 0:  # Only positive numbers
                numbers.append(num)
        except:
            pass
    return sorted(set(numbers))

def compare_pdfs(pdf1, pdf2):
    text1 = extract_text(pdf1)
    text2 = extract_text(pdf2)
    
    if not text1 or not text2:
        print("Error: Could not read PDF files")
        return
    
    nums1 = extract_numbers(text1)
    nums2 = extract_numbers(text2)
    
    # Find common numbers
    common = set(nums1) & set(nums2)
    total_unique = len(set(nums1) | set(nums2))
    
    match_pct = len(common) / total_unique * 100 if total_unique > 0 else 0
    
    print(f"PDF 1: {pdf1}")
    print(f"PDF 2: {pdf2}")
    print(f"Numbers in PDF 1: {len(nums1)}")
    print(f"Numbers in PDF 2: {len(nums2)}")
    print(f"Common numbers: {len(common)}")
    print(f"Match percentage: {match_pct:.1f}%")
    
    if common:
        print(f"Common values: {sorted(list(common))[:10]}")  # Show first 10
    
    if match_pct >= 70:
        print("Result: Documents have similar numbers")
    else:
        print("Result: Documents have different numbers")

def find_pdfs_in_directory(directory="."):
    """Find all PDF files in the specified directory"""
    pdf_files = []
    try:
        for file in os.listdir(directory):
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(directory, file))
    except:
        pass
    return pdf_files

def compare_all_pdfs_in_directory(directory="."):
    """Compare all PDF files found in the specified directory"""
    pdf_files = find_pdfs_in_directory(directory)
    
    if len(pdf_files) < 2:
        print(f"Found {len(pdf_files)} PDF file(s) in directory: {directory}")
        print("Need at least 2 PDF files to compare")
        return
    
    print(f"Found {len(pdf_files)} PDF files:")
    for i, pdf in enumerate(pdf_files, 1):
        print(f"  {i}. {os.path.basename(pdf)}")
    
    print("\nComparing all PDF pairs:")
    print("=" * 50)
    
    for i in range(len(pdf_files)):
        for j in range(i + 1, len(pdf_files)):
            print(f"\nComparing: {os.path.basename(pdf_files[i])} vs {os.path.basename(pdf_files[j])}")
            compare_pdfs(pdf_files[i], pdf_files[j])
            print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments - compare all PDFs in current directory
        compare_all_pdfs_in_directory()
    elif len(sys.argv) == 2:
        # One argument - treat as directory path
        directory = sys.argv[1]
        if os.path.isdir(directory):
            compare_all_pdfs_in_directory(directory)
        else:
            print(f"Error: '{directory}' is not a valid directory")
            sys.exit(1)
    elif len(sys.argv) == 3:
        # Two specific files provided
        compare_pdfs(sys.argv[1], sys.argv[2])
    else:
        print("Usage:")
        print("  python script.py                           # Compare all PDFs in current directory")
        print("  python script.py /path/to/pdf/directory    # Compare all PDFs in specified directory")
        print("  python script.py file1.pdf file2.pdf       # Compare specific files")
        sys.exit(1)
