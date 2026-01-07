# PDF Splitter

A simple desktop web application to extract a single page from a PDF file, built with Python, Flask, PyQt5, and PyPDF2.

<p align="center">
   <img src="Icon.png">
</p>

## Features

- Extract a specific page from any PDF file.
- User-friendly web interface embedded in a desktop window.
- Cross-platform (Windows recommended).
- Fast and secure file handling.

## Requirements

- Python 3.8+
- See [requirments.txt](requirments.txt) for all dependencies.

## Installation

You can use either of the following methods to install and run PDF Splitter:

### 1. Run from Source

1. **Clone or Download** this repository.
2. **Install dependencies** (preferably in a virtual environment):

    ```sh
    pip install -r requirments.txt
    ```

3. **Run the application**:

    ```sh
    python app.py
    ```

### 2. Use the Executable (Windows)

1. Download the pre-built `.exe` file from the [Releases](#) section (or build it yourself using the Inno Setup script).
2. Double-click the executable to launch the application—no Python installation required.

## Usage

1. The application window will open automatically.
2. Select a PDF file and enter the page number you want to extract.
3. Click "Submit" to download the extracted page as a new PDF.
4. Use the "Quit" button to exit the application.

## Project Structure

- `app.py` - PyQt5 desktop wrapper for the Flask web app.
- `pdfsplitter.py` - Flask server and PDF splitting logic.
- `templates/index.html` - Web interface template.
- `requirments.txt` - Python dependencies.
- `setup creation script for inno.iss` - Inno Setup script for creating a Windows installer.

## Building an Executable

You can use PyInstaller or the provided Inno Setup script to create a standalone executable for Windows.
