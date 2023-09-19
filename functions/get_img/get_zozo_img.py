from selenium.webdriver import Chrome, ChromeOptions
import re

DEFAULT_IMAGE_PATH_PATTERN = r'"(http[^"]+)"'

def extract_image_url_from_html(html_content):
    for line in html_content.splitlines():
        if "DefaultImagePath" in line:
            url_match = re.search(DEFAULT_IMAGE_PATH_PATTERN, line)
            return url_match.group(1) if url_match else None
    return None

def get_zozo_img(target_url):
    options = ChromeOptions()
    
    with Chrome(options=options) as driver:
        driver.get(target_url)
        html_content = driver.page_source
        return extract_image_url_from_html(html_content) or False
