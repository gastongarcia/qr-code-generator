import qrcode
import os
import argparse
import re
import qrcode.image.svg

def sanitize_url(url):
    # Remove protocol and replace special characters
    sanitized = re.sub(r'^https?://', '', url)
    sanitized = re.sub(r'[/\\?%*:|"<>]+', '_', sanitized)
    return sanitized

def generate_qr_code(url):
    if not url:
        print("URL cannot be empty.")
        return

    try:
        # Generate PNG
        img_png = qrcode.make(url)
        filename_png = f"{sanitize_url(url)}.png"
        img_png.save(filename_png)
        print(f"QR code saved as {os.path.abspath(filename_png)}")

        # Generate SVG
        img_svg = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage)
        filename_svg = f"{sanitize_url(url)}.svg"
        img_svg.save(filename_svg)
        print(f"QR code saved as {os.path.abspath(filename_svg)}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a QR code from a URL.')
    parser.add_argument('url', type=str, help='The URL to generate a QR code for.')
    args = parser.parse_args()
    generate_qr_code(args.url)