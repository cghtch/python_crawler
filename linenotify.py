import requests
import scraper

stock = scraper.Stock("2330")
result = stock.scrape()
price = result[0][3]

headers = {"Authorization": "Bearer " + "fJYb5WObFDm8VGJr0LWAX7HGMfoQhkU5PuUR2SZLgQO",
           "Content-Type": "application/x-www-form-urlencoded"}
params = {"message": "2330台積電已降價至" + price + "元"}
if int(price) < 600:  # 將爬取的價格字串轉型為整數

    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  # 200
