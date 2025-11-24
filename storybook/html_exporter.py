from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def export_story_to_html(chapters, image_files):
    html = "<html><body>"

    for i, chapter in enumerate(chapters):
        html += f"<h2>Chapter {i+1}<h2>"
        html += f"<p>{chapter}</p>"
        if i < len(image_files):
            html += f'<img src="{image_files[i]}" width="400"><br><br>'

    html += "</body></html>"

    html_filename = "storybook.html"
    try:
        with open(html_filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Successfully created {html_filename}")
    except IOError as e:
        print(f"Error writing HTML file: {e}")
        return

    # Selenium to open webpage and screenshot it
    opts = Options()
    opts.add_argument("--headless")
    driver = webdriver.Chrome(options=opts)

    driver.get("file://" + os.path.abspath("storybook.html"))
    time.sleep(1)
    driver.save_screenshot("storybook_preview.png")
    driver.quit()
