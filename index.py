from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import time
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("EMAIL"))


# def currentPrice():
#     url = 'https://www.amazon.com/Toilet-Smooth-Birthday-Bathroom-Accessories/dp/B085WQY15M/ref=sr_1_4?dchild=1&keywords=toilet+paper&qid=1584989842&sr=8-4'

#     headers = {
#         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
#     }
#     page = requests.get(url, headers=headers)
#     soup = BeautifulSoup(page.content, 'lxml')
#     price = soup.find('span', id='price_inside_buybox').get_text().strip()
#     converted_price = int(price[1:3])
#     return converted_price


# def checkPrice():
#     if(currentPrice() < 9):
#         sendMail()
#     else:
#         print('price is too high, wait a little longer')


# def sendMail():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login(os.getenv("EMAIL"), os.getenv('PASSWORD'))

#     subject = 'Price is below desired price!'
#     body = 'check it out here: https://www.amazon.com/Toilet-Smooth-Birthday-Bathroom-Accessories/dp/B085WQY15M/ref=sr_1_4?dchild=1&keywords=toilet+paper&qid=1584989842&sr=8-4'
#     msg = f'subject: {subject}\n\n{body}'

#     server.sendmail(
#         os.getenv("EMAIL"),
#         os.getenv("EMAIL"),
#         msg
#     )

#     print('email has been sent')

#     server.quit()


# while(True):
#     checkPrice()
#     time.sleep(60 * 60 * 60 * 24)
