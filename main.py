from bs4 import BeautifulSoup
import requests
import smtplib

email = ""
password = ""

url = "https://www.amazon.in/Sony-WH-1000XM5-Wireless-Cancelling-Headphones/dp/B09XS7JWHH/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

price = None
selectors = [
    "span.a-price-whole",
    "span.a-price.a-text-price span.a-offscreen",
]

for selector in selectors:
    price_tag = soup.select_one(selector)
    if price_tag:
        price = price_tag.get_text(strip=True)
        break

title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
price = float(price.replace(",", "").replace("₹", ""))



BUY_PRICE = 26990

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
