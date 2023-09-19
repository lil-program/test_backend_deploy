from functions.get_img.get_default_img import get_default_img
from functions.get_img.get_zozo_img import get_zozo_img
from functions.get_img.get_shop_list_img import get_shop_list_img
from functions.get_img.get_shein_img import get_shein_img

URL_TO_FUNCTION_MAPPING = {
    'zozo.jp': get_zozo_img,
    'shop-list.com': get_shop_list_img,
    'shein.com': get_shein_img
}

def get_img_path(target_url: str = None) -> str:
    """URLから画像パスを取得する

    Args:
        target_url (str, optional): ショップURL. Defaults to None.

    Returns:
        img_url: 画像パス
    """
    if not target_url:
        return get_default_img()

    for domain, func in URL_TO_FUNCTION_MAPPING.items():
        if domain in target_url:
            return func(target_url) or get_default_img()

    return get_default_img()

if __name__ == '__main__':
    get_img_path()