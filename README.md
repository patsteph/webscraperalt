# WebScraperAlt

A simple yet powerful Python web scraper that extracts content from websites and saves it as DOCX or PDF files.

## Features

- 🌐 Scrapes text content from any website
- 🧹 Cleans and processes text (removes specified keywords)
- 📂 Automatically creates an output folder on your desktop
- 📄 Saves content in DOCX or PDF format
- 🔄 Uses random user agents to avoid being blocked
- 📁 Custom save location option

## Requirements

- Python 3.6+
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `fake-useragent`
  - `python-docx`
  - `reportlab`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/webscraperalt.git
   cd webscraperalt
   ```

2. Install the required packages:
   ```
   pip install requests beautifulsoup4 lxml fake-useragent python-docx reportlab
   ```

## Usage

1. Run the script:
   ```
   python webscraperalt.py
   ```

2. Enter the website URL when prompted.

3. Choose the output format (DOCX or PDF).

4. Enter a filename for the saved file.

5. Choose whether to save in the default location (Desktop/ScrapeOutputs) or select a custom location.

## Customization

You can customize the script by modifying:

- The `keywords_to_remove` list in the `clean_text` function to filter out specific words
- The HTML tags to exclude in the `extract_text` function
- The formatting options in the `save_as_pdf` function

## Example

```
🔗 Enter the website URL to scrape: https://example.com

💾 Choose file format:
1. DOCX
2. PDF
Enter your choice (1 or 2): 1

✏️ Enter a name for the saved file (without extension): example_site

📄 Saved as DOCX: C:\Users\username\Desktop\ScrapeOutputs\example_site.docx

Would you like to choose a different save location? (yes/no): no
```

## Notes

- This script respects website terms of service by using proper headers.
- Be mindful of copyright restrictions when scraping and using website content.
- Some websites may block scraping attempts. Use responsibly.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
