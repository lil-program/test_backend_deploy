import sys
sys.path.append("..")

from main import main


def test_get_img():
    test_urls = [
         "https://jp.shein.com/FriFul-Drop-Shoulder-Half-Zip-Placket-Tee-p-21904788-cat-1738.html?src_identifier=fc%3DWomen%60sc%3D%E3%83%88%E3%83%83%E3%83%97%E3%82%B9%60tc%3D0%60oc%3D0%60ps%3Dtab01navbar06%60jc%3Dreal_1766&src_module=topcat&src_tab_page_id=page_home1694871771572&mallCode=1"
        "https://jp.shein.com/Honeyspot-Solid-Ruched-Sleeve-Oversized-Shirt-p-11069315-cat-1733.html?mallCode=1&imgRatio=3-4"
        "https://shop-list.com/women/niceclaup/0822060840/",
        "https://shop-list.com/women/niceclaup/0832060330/",
        "https://zozo.jp/shop/adidas/goods/73131257/?did=120132956&rid=1006",
        "https://zozo.jp/shop/adidas/goods/73131266/?did=120080522&rid=1006",
        "hogehoge"
    ]

    for test_url in test_urls:
        print("---------------------------------------------------------------------------------")
        print(test_url)
        print(main(test_url))

if __name__ == '__main__':
    test_get_img()