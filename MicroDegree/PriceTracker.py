import requests
from bs4 import BeautifulSoup
import time

products_to_track = [
    {
        "product_url": "https://www.amazon.in/gp/aw/d/9355434146/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=849ecfe90124266010408c111e92d5a7&hsa_cr_id=0&qid=1776760475&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=PnM7RbFYu0&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=D0F2d&content-id=amzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05%3Aamzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_p=9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_r=MERFNF8V3419EYW47JFS&pd_rd_wg=YqFx7&pd_rd_r=c1609025-ffd4-4e99-9a64-227402190206",
        "name": "The Mountain Is You",
        "target_price": 500
    },
    {
        "product_url": "https://www.amazon.in/dp/178633089X/?bestFormat=true&k=ikigai%20book%20in%20english&ref_=nb_sb_ss_w_scx-ent-bk-ww_k0_1_6_de&crid=1H4T9VELALMXI&sprefix=ikigai",
        "name": "Ikigai",
        "target_price": 500
    },
    {
        "product_url": "https://www.amazon.in/That-Night-Friends-Haunting-Secret/dp/0143451871/ref=sr_1_2_sspa?crid=2YVA3SYISFNIU&dib=eyJ2IjoiMSJ9.J6et6_V0OeZvnB6jk-pg9nDP4fwhKc0zI_bvdWSRorg2shoYveCya3Xw3NUvEA2W0ZULfsBQuwZRmQoSv7IFAB_fmzblu3SHQrWsBY8OUKjA7VTwVRBOnxo-3XTgBoLTqCC5m__eUPQ5rmI96D7bmQeU0832r4i78hh-nRMZQc4ayLi9pelQzMSfV-vGwYpQigGbAIsNUWifu2UbiOPp4IXn5-zNb4kYKM88d9GU8mI.uiztg2M3bJ5z-t1skqgJbiWlink2UpvDTM00-jGqUCM&dib_tag=se&keywords=novel+books&qid=1776760475&sprefix=novel%2Caps%2C454&sr=8-2-spons&aref=m79IJDlEnH&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "name": "That Night",
        "target_price":500
    },
    {
        "product_url": "https://www.amazon.in/Touch-Eternity-Datta-Durjoy/dp/014344834X/ref=sr_1_8?crid=2YVA3SYISFNIU&dib=eyJ2IjoiMSJ9.J6et6_V0OeZvnB6jk-pg9nDP4fwhKc0zI_bvdWSRorg2shoYveCya3Xw3NUvEA2W0ZULfsBQuwZRmQoSv7IFAB_fmzblu3SHQrWsBY8OUKjA7VTwVRBOnxo-3XTgBoLTqCC5m__eUPQ5rmI96D7bmQeU0832r4i78hh-nRMZQc4ayLi9pelQzMSfV-vGwYpQigGbAIsNUWifu2UbiOPp4IXn5-zNb4kYKM88d9GU8mI.uiztg2M3bJ5z-t1skqgJbiWlink2UpvDTM00-jGqUCM&dib_tag=se&keywords=novel+books&qid=1776760475&sprefix=novel%2Caps%2C454&sr=8-8",
        "name": "Touch-Eternity",
        "target_price":500
    },
    {
        "product_url": "https://www.amazon.in/When-Am-You-Durjoy-Datta/dp/0143448358/ref=pd_sbs_d_sccl_1_1/522-2556794-9306220?pd_rd_w=V2Dlj&content-id=amzn1.sym.d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_p=d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_r=41E0J7KR2B8V1D66DK3D&pd_rd_wg=Y3l5L&pd_rd_r=c615d2cb-b3fe-4fbd-8b72-39f9df46f981&pd_rd_i=0143448358&psc=1",
        "name": "When I Am With You",
        "target_price":500
    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    price3 = soup.find("span", class_="a-price-whole")
    if price3 is None:
        price3 = soup.find(id="priceblock_ourprice")
    
    # Changed: Added check for None and empty string
    if price3 and price3.string and price3.string.strip():
        print(price3.string)
        return price3.string
    
    return None

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        
        if product_price_returned is None:
            continue
        
        my_product_price = int(product_price_returned.replace(',', ''))
        
        print(f"{every_product.get('name')} - {my_product_price}")
        
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("name") + ' - Available at Target Price - Current Price: ' + str(my_product_price) + '\n')
        else:
            print("Still at current price")
            result_file.write(every_product.get("name") + ' - Still at current price - Current Price: ' + str(my_product_price) + '\n')
        
        print("-" * 50)
        time.sleep(2)

finally:
    result_file.close()