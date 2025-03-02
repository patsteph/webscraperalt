import os
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import Tk, filedialog

# Function to fetch website content
def fetch_content(url):
    headers = {
        "User-Agent": UserAgent().random  # Generate a random user-agent
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the website: {e}")
        return None

# Function to clean extracted text
def clean_text(text):
    keywords_to_remove = ["Python", "JavaScript", "C++", "HTML/CSS"]  # Example keywords
    for keyword in keywords_to_remove:
        safe_keyword = re.escape(keyword)  # Escape special characters
        text = re.sub(rf'\b{safe_keyword}\b', '', text, flags=re.IGNORECASE)
    return text

# Function to extract relevant text from webpage
def extract_text(html):
    soup = BeautifulSoup(html, "lxml")

    # Remove unwanted elements
    for tag in soup(["script", "style", "noscript", "iframe", "code", "pre"]):
        tag.extract()

    text = soup.get_text(separator=" ")
    return clean_text(text)

# Function to check and create ScrapeOutputs directory on Desktop
def get_output_directory():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_dir = os.path.join(desktop_path, "ScrapeOutputs")
    
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"✅ Created output folder: {output_dir}")
        except PermissionError:
            print("❌ Error: No permission to create a folder on Desktop.")
            return None
    return output_dir

# Function to ensure a valid filename
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename).strip()

# Function to save as DOCX
def save_as_docx(content, output_dir, filename):
    doc = Document()
    doc.add_paragraph(content)
    output_path = os.path.join(output_dir, filename + ".docx")
    doc.save(output_path)
    print(f"📄 Saved as DOCX: {output_path}")

# Function to save as PDF
def save_as_pdf(content, output_dir, filename):
    output_path = os.path.join(output_dir, filename + ".pdf")
    pdf = canvas.Canvas(output_path, pagesize=letter)
    pdf.setFont("Helvetica", 12)

    # Split text into multiple lines for proper formatting
    lines = content.split(" ")
    y_position = 750
    max_chars_per_line = 90
    line_buffer = ""

    for word in lines:
        if len(line_buffer) + len(word) + 1 < max_chars_per_line:
            line_buffer += word + " "
        else:
            pdf.drawString(50, y_position, line_buffer.strip())
            y_position -= 20
            line_buffer = word + " "
            if y_position < 50:  # Start new page if needed
                pdf.showPage()
                pdf.setFont("Helvetica", 12)
                y_position = 750

    if line_buffer:
        pdf.drawString(50, y_position, line_buffer.strip())

    pdf.save()
    print(f"📄 Saved as PDF: {output_path}")

# Main script execution
if __name__ == "__main__":
    url = input("🔗 Enter the website URL to scrape: ").strip()
    
    html_content = fetch_content(url)
    if not html_content:
        exit()

    extracted_text = extract_text(html_content)
    
    # Check for output directory
    output_dir = get_output_directory()
    if not output_dir:
        exit()

    # Ask user where to save file
    print("\n💾 Choose file format:\n1. DOCX\n2. PDF")
    file_choice = input("Enter your choice (1 or 2): ").strip()

    # Prompt for filename
    filename = input("\n✏️ Enter a name for the saved file (without extension): ").strip()
    filename = sanitize_filename(filename)

    if file_choice == "1":
        save_as_docx(extracted_text, output_dir, filename)
    elif file_choice == "2":
        save_as_pdf(extracted_text, output_dir, filename)
    else:
        print("❌ Invalid choice. Exiting.")

    # Prompt user for saving location
    save_prompt = input("\nWould you like to choose a different save location? (yes/no): ").strip().lower()
    if save_prompt == "yes":
        Tk().withdraw()  # Hide root window
        save_path = filedialog.askdirectory(title="Select Save Location")
        if save_path:
            if file_choice == "1":
                save_as_docx(extracted_text, save_path, filename)
            else:
                save_as_pdf(extracted_text, save_path, filename)
