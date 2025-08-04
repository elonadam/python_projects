import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from datetime import datetime
import logging
import sys

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('price_monitor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)


class AmazonPriceMonitor:
    def __init__(self, email_config):
        self.email_config = email_config
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-GB,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    def get_price(self, url):
        """Extract price from Amazon product page"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Try multiple price selectors because Amazon changes these frequently
            price_selectors = [
                '.a-price-whole',
                '.a-price .a-offscreen',
                '#price_inside_buybox',
                '.a-price-range .a-price .a-offscreen',
                '#apex_desktop .a-price .a-offscreen',
                '.a-price.a-text-price.a-size-medium.apexPriceToPay .a-offscreen'
            ]

            price = None
            for selector in price_selectors:
                price_element = soup.select_one(selector)
                if price_element:
                    price_text = price_element.get_text().strip()
                    # extract numeric value from price text
                    price_match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
                    if price_match:
                        price = float(price_match.group())
                        break

            if price is None:
                logging.warning("Could not find price on page")
                return None

            return price

        except requests.RequestException as e:
            logging.error(f"Error fetching page: {e}")
            return None
        except Exception as e:
            logging.error(f"Error parsing price: {e}")
            return None

    def send_email(self, subject, body, current_price, url, product_name):
        """Send email notification"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender_email']
            msg['To'] = self.email_config['recipient_email']
            msg['Subject'] = subject

            # create HTML body
            html_body = f"""
            <html>
                <body style="font-family: Arial, sans-serif; color: #333;">
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                        <h2 style="margin: 0;"> Amazon Price Alert!</h2>
                    </div>

                    <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                        <h3 style="color: #28a745; margin-top: 0;">Product: {product_name}</h3>
                        <p style="font-size: 16px;">{body}</p>

                        <div style="background: white; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
                            <p style="margin: 0; font-size: 18px;"><strong> Current Price: £{current_price:.2f}</strong></p>
                        </div>
                    </div>

                    <div style="text-align: center; margin: 20px 0;">
                        <a href="{url}" style="background: #007bff; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold;">🛒 View Product on Amazon</a>
                    </div>

                    <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
                    <p style="color: #666; font-size: 12px; text-align: center;">
                        Alert triggered on {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}
                    </p>
                </body>
            </html>
            """

            msg.attach(MIMEText(html_body, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_config['sender_email'], self.email_config['password'])

            text = msg.as_string()
            server.sendmail(self.email_config['sender_email'],
                            self.email_config['recipient_email'], text)
            server.quit()

            logging.info(f" V Email sent successfully for {product_name}")

        except Exception as e:
            logging.error(f" X Error sending email for {product_name}: {e}")

    def check_price(self, url, target_price=310, product_name="Amazon Product"):
        """Check price and send alert if below target"""
        logging.info(f"Checking price for: {product_name}")
        logging.info(f"Target price: £{target_price}")

        current_price = self.get_price(url)

        if current_price is None:
            logging.error(f" X Failed to get current price for {product_name} - skipping")
            return False

        logging.info(f"Current price for {product_name}: £{current_price:.2f}")

        if current_price < target_price:
            subject = f" Price Drop Alert: {product_name} now £{current_price:.2f}!"
            body = f"Great news! The price for <strong>{product_name}</strong> has dropped to £{current_price:.2f}, which is £{target_price - current_price:.2f} below your target of £{target_price}."
            self.send_email(subject, body, current_price, url, product_name)
            logging.info(f"ALERT: {product_name} price below target - email sent!")
            return True
        else:
            logging.info(f"{product_name} price £{current_price:.2f} is still above target £{target_price}")
            return False


def main():
    # Configuration - UPDATE THESE VALUES!
    EMAIL_CONFIG = {
        'sender_email': 'sender@gmail.com',  # YOUR Gmail address
        'password': 'gmailAppPassewordHere',  # YOUR Gmail app password
        'recipient_email': 'reciver@gmail.com'  # Where you want alerts
    }

    # Product URLs and target price - ADD/MODIFY PRODUCTS HERE
    products = [
        {
            'name': 'Bambino Plus Stainless Steel',
            'url': 'https://www.amazon.co.uk/dp/B07GB2JVD7?tag=sakura0f2-21&linkCode=ogi&th=1',
            'target_price': 305
        },
        {
            'name': 'Bambino Plus Black',
            'url': 'https://www.amazon.co.uk/dp/B07Q2LS4XK?tag=sakura0f2-21&linkCode=ogi&th=1',
            'target_price': 305
        }
    ]

    # Initialize monitor
    monitor = AmazonPriceMonitor(EMAIL_CONFIG)

    logging.info("=" * 60)
    logging.info(f"Starting Amazon Price Monitor - {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}")
    logging.info("=" * 60)

    alerts_sent = 0

    try:
        for product in products:
            result = monitor.check_price(
                url=product['url'],
                target_price=product['target_price'],
                product_name=product['name']
            )
            if result:
                alerts_sent += 1
            logging.info("-" * 40) 

        # Summary
        logging.info("=" * 60)
        if alerts_sent > 0:
            logging.info(f"V Price monitor completed - {alerts_sent} alert(s) sent!")
        else:
            logging.info("V Price monitor completed - no alerts needed")
        logging.info("=" * 60)

    except Exception as e:
        logging.error(f" X Error during price check: {e}")


if __name__ == "__main__":
    main()
