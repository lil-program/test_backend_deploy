import requests
import re

IMG_TAG_PATTERN = re.compile(r'<img[^>]+>')
SRC_PATTERN = re.compile(r'src=["\'](https?://[^"\']+)["\']')

def extract_image_url_from_html(html_content):
    img_tags = IMG_TAG_PATTERN.findall(html_content)
    
    for tag in img_tags:
        if "詳細画像1" in tag:
            match = SRC_PATTERN.search(tag)
            if match:
                return match.group(1)
    
    return None

def get_shop_list_img(target_url):
    try:
        res = requests.get(target_url)
        res.raise_for_status()

        html_content = res.content.decode('utf-8')
        return extract_image_url_from_html(html_content)
    
    except requests.RequestException:
        return False
