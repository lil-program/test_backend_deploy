import requests
import re

IMG_PATTERN = re.compile(r'data-src="//(img.*\.jpg)')

def extract_image_url_from_html(html_content):
    img_tags = IMG_PATTERN.findall(html_content)
    return img_tags[0] if img_tags else False

def get_shein_img(target_url):
    try:
        res = requests.get(target_url)
        res.raise_for_status()
        
        html_content = res.content.decode('utf-8')
        return extract_image_url_from_html(html_content)

    except requests.RequestException:
        return False