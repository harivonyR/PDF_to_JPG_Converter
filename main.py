# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 20:20:18 2025

@author: Lenovo
"""

import os
import argparse
from pdf2image import convert_from_path

def convert_pdf_to_jpg(pdf_path: str, output_folder: str, dpi: int = 300):
    """
    Converts a multi-page PDF document into individual JPG images (one per page).

    Args:
        pdf_path: The full path to the input PDF file.
        output_folder: The directory where the output JPG images will be saved.
        dpi: The Dots Per Inch resolution for the output images (default is 300).
    """
    try:
        # 1. Convert the PDF to a list of images (one per page)
        print(f" Starting conversion of: {pdf_path}...")
        pages = convert_from_path(pdf_path, dpi=dpi)

        # 2. Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        print(f" Output directory created: {output_folder}")

        # 3. Save each page as a JPG file
        for i, page in enumerate(pages):
            # Use os.path.basename to get the PDF filename without extension for better naming
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            image_path = os.path.join(output_folder, f'{base_name}_page_{i + 1}.jpg')
            
            page.save(image_path, 'JPEG')
            print(f'✅ Page {i + 1} saved successfully: {image_path}')
            
        print(f"\n Conversion complete! {len(pages)} pages processed.")

    except FileNotFoundError:
        print(f" Error: Input file not found at {pdf_path}")
    except Exception as e:
        print(f" An unexpected error occurred during conversion: {e}")

def main():
    """
    Parses command-line arguments and calls the conversion function.
    """
    parser = argparse.ArgumentParser(
        description="A Python script to convert PDF files into high-resolution JPG images."
    )
    
    parser.add_argument(
        "input_pdf", 
        type=str, 
        help="Path to the input PDF file (e.g., input/document.pdf)"
    )
    parser.add_argument(
        "output_dir", 
        type=str, 
        help="Path to the output folder where images will be saved (e.g., images/)"
    )
    parser.add_argument(
        "--dpi", 
        type=int, 
        default=300, 
        help="Resolution of the output images in DPI (Default: 300)"
    )
    
    args = parser.parse_args()
    
    convert_pdf_to_jpg(args.input_pdf, args.output_dir, args.dpi)

if __name__ == "__main__":
    # Example for internal testing (comment out when using command-line)
    # convert_pdf_to_jpg('input/Q3 2025 bis.pdf', 'images_Q3_bis_res_pdf')
    
    # Use the main function to handle command-line arguments
    main()