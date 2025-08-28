# QR Code Generator

This is a simple Python script to generate QR codes from URLs. It's a command-line tool that takes a URL as an argument and saves the corresponding QR code as both PNG and SVG files.

## Features

- Generates QR codes from any URL.
- Saves QR codes in both PNG and SVG formats.
- Sanitizes the URL to create a clean filename.

## Installation

1. **Clone the repository or download the script.**

2. **Create a virtual environment.** It is recommended to use a virtual environment to manage the dependencies.

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment.**

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install the required packages.**

   ```bash
   pip install qrcode[pil]
   ```

## Usage

**IMPORTANT:** Before running the script, you **MUST** activate the virtual environment in your terminal session. This is to avoid a `ModuleNotFoundError` because the required `qrcode` library is installed in the virtual environment.

Run the script from your terminal and pass the URL as an argument:

```bash
python qr_generator.py "your_url_here"
```

Replace `"your_url_here"` with the actual URL you want to encode.

### Example

```bash
python qr_generator.py "https://www.google.com"
```

This will create two files in the same directory:

- `www.google.com.png`
- `www.google.com.svg`