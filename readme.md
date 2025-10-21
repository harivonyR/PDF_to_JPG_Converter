# PDF to JPG Converter

A simple, high-resolution PDF to JPG conversion utility built with Python and the `pdf2image` library. This script processes all pages of a given PDF and saves each page as a separate JPG image in a specified output directory.

## Prerequisites

This script requires **Python 3.x** and the following external library:

1.  **`pdf2image` (Python Library)**
2.  **`Poppler` (System Dependency)**: The `pdf2image` library requires the **Poppler** utility to be installed on your operating system.

### Installation

1.  **Install Python Dependencies:**
    ```bash
    pip install pdf2image
    ```

2.  **Install Poppler (System Dependency):**
    * **Windows:** Download the latest Poppler binaries and add the `bin` folder to your system's PATH.
    * **macOS (using Homebrew):**
        ```bash
        brew install poppler
        ```
    * **Linux (using apt):**
        ```bash
        sudo apt-get install poppler-utils
        ```

## Usage

The script is executed via the command line and requires the input PDF path and the desired output directory.

### Command Syntax

```bash
python pdf_converter.py <INPUT_PDF_PATH> <OUTPUT_DIRECTORY> [OPTIONS]
````

### Arguments

| Argument | Description | Example |
| :--- | :--- | :--- |
| `<INPUT_PDF_PATH>` | Path to the PDF file you want to convert. | `docs/report.pdf` |
| `<OUTPUT_DIRECTORY>` | Folder where the generated JPG images will be saved. | `output/report_images` |

### Options

| Option | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--dpi` | Integer | `300` | Sets the resolution (Dots Per Inch) of the output images. |

### Examples

**1. Basic Conversion (using default 300 DPI):**

```bash
python pdf_converter.py input/Q3_2025_bis.pdf images_Q3_bis_res_pdf
```

**2. High-Resolution Conversion (using 400 DPI):**

```bash
python pdf_converter.py input/project_plan.pdf output/plan_pages --dpi 400
```

## Output

The script will create the output folder (if it doesn't exist) and save each page with a filename structure like:

`[PDF_BASENAME]_page_[PAGE_NUMBER].jpg`

**Example Output Files:**

  * `images_Q3_bis_res_pdf/Q3_2025_bis_page_1.jpg`
  * `images_Q3_bis_res_pdf/Q3_2025_bis_page_2.jpg`
  * ...
