import requests
from bs4 import BeautifulSoup
import pprint
import lxml
import smtplib

response = requests.get("https://www.amazon.in/Dell-E2420HS-Backlit-Monitor-Speaker/dp/B084N8B9XB/ref=sr_1_5?dchild=1&keywords=monitor+24%2B+inch&qid=1632326718&sr=8-5",headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
})
soup=BeautifulSoup(response.content,"lxml")
# anchor=soup.find_all("a")
# print(anchor)
# for link in soup.find_all('a'):
    # print(link.get('href'))
	
price=soup.find("span", {"id": "priceblock_ourprice"}).string
price_amazon= price.split("₹")[1]
price_as_int=price_amazon.split(",")
t=0
for value in price_as_int:
	t=str(t)+str(value)
new_price=(float(t))

#email

title = soup.find(id="productTitle").get_text().strip()


Buy_price = 10000

if new_price < Buy_price:
    message = f"{title} is now available at {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login("acgritty@gmail.com", "*******")
        connection.sendmail(
            from_addr=acgritty@gmail,
            to_addrs=acgritty@gmail,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
