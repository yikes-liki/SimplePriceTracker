import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/gp/aw/d/9355434146/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=849ecfe90124266010408c111e92d5a7&hsa_cr_id=0&qid=1776760475&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=PnM7RbFYu0&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=D0F2d&content-id=amzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05%3Aamzn1.sym.9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_p=9269eab1-ae85-443b-9ec2-b2fa4ebaad05&pf_rd_r=MERFNF8V3419EYW47JFS&pd_rd_wg=YqFx7&pd_rd_r=c1609025-ffd4-4e99-9a64-227402190206"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

print(page)


price3 = soup.find("span", class_="a-price-whole")
print (price3)
print(price3.string)














