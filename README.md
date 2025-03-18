# Amazon-Price-Tracker

This Python script tracks the price of a product on Amazon and sends an email alert when the price drops below a specified amount.

## Features
- Scrapes product details (title and price) from Amazon using `BeautifulSoup`
- Sends an email alert when the price drops below the target price
- Uses `requests` for web scraping and `smtplib` for email notifications

## Prerequisites
Make sure you have Python installed and the required libraries:

```bash
pip install beautifulsoup4 requests
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. Update your Amazon **product URL** in the `url` variable inside the script.

3. Set your email and password in the `email` and `password` variables:
   ```python
   email = "your-email@example.com"
   password = "your-email-password"
   ```
   **Note:** It is recommended to use **App Passwords** for security instead of your real password.

4. Set the `BUY_PRICE` to your target price:
   ```python
   BUY_PRICE = 26990
   ```

## Usage
Run the script:
```bash
python price_tracker.py
```

If the price falls below your `BUY_PRICE`, you will receive an email notification.

## Troubleshooting
- If the script doesn't find the price, Amazon may have changed the website structure. Try updating the `selectors` in the script.
- Make sure you have enabled **Less Secure Apps** (or use App Passwords) in your email provider.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open an issue or submit a pull request if you want to improve this script!

---
### Author
**Abhinav Kumar**  


