from bs4 import BeautifulSoup
import requests
import pymysql

class Stock:
    def __init__(self, *stock_numbers):
        self.stock_numbers = stock_numbers
        print(self.stock_numbers)

    def scrape(self):
        result = list()
        for stock_number in self.stock_numbers:

            response = requests.get("https://tw.stock.yahoo.com/q/q?s=" + stock_number)
            soup = BeautifulSoup(response.text.replace("加到投資組合", ""), "lxml")
            stock_date = soup.find("font", {"class": "tt"}).getText().strip()[-9:]
            tables = soup.find_all("table")[2]
            tds = tables.find_all("td")[0:11]
            result.append((stock_date,) + tuple(td.getText().strip() for td in tds))

        return result

    def save(self, stocks):

        db_setting = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "kiwikiwi",
            "db": "stock",
            "charset": "utf8"
        }
        try:
            conn = pymysql.connect(**db_setting)

            with conn.cursor() as cursor:
                sql = """ INSERT INTO market(
                    market_date,
                    stock_name,
                    market_time,
                    final_price,
                    buy_price,
                    sell_price,
                    ups_and_downs,
                    lot,
                    yesterday_price,
                    opening_price,
                    highest_price,
                    lowest_price)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                for stock in stocks:
                    cursor.execute(sql, stock)
                conn.commit()

        except Exception as ex:
            print("Exception:", ex)




stock = Stock("2451", "2454")
stock.save(stock.scrape())
print(stock.scrape())

