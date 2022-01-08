import requests
from bs4 import BeautifulSoup
import html5lib
import cv2
import numpy as np
from PIL import Image


url = "https://www.moneycontrol.com/"

html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
print(soup.prettify())

ad_img=[]
ads=soup.find_all('img',class_="img-ad")

for ad in ads:
    ad_img.append(ad['src'])

print(ad_img)
    
    
    
