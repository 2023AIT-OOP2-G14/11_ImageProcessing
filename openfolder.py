from flask import Flask, request, render_template
import os
import sys
import datetime
from datetime import datetime
def create_html_with_images(folder_path):
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    html_content = "<html>\n<head>\n<title>PNG Images</title>\n</head>\n<body>\n"

    for file in png_files:
        img_path = os.path.join(folder_path, file)
        html_content += f"<img src='{img_path}' alt='{file}'><br>\n"

    html_content += "</body>\n</html>"

    with open('images.html', 'w') as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)
    folder_path =request.form.get("fo")
    create_html_with_images(folder_path)
