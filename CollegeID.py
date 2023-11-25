from bs4 import BeautifulSoup
import requests

def CrawlCollegeID():
    numberOfPage = 16
    CollegeID = []
    baseURL = "https://vietnamnet.vn/"
    for i in range(numberOfPage):
        page = requests.get(f"{baseURL}giao-duc/diem-thi/tra-cuu-diem-chuan-cd-dh-2023-page{i}")
        soup = BeautifulSoup(page.text, 'html.parser')
        CollegeIDTableInfo = soup.find("div", {"class": "dataTable__main"}).find("table").find("tbody").findAll("tr")
        for College in CollegeIDTableInfo:
            dataList = []
            for data in College:
                if data == '\n':
                    continue
                if data.find("a"):
                    shortURL = data.find("a").get("href")
                    dataList.append(f"{baseURL}{shortURL}".replace("2023","year"))
                    data = data.getText()
                    dataList.append(data[:len(data) - 6])
                else:
                    data = data.getText()
                    dataList.append(data)
            CollegeID.append(dataList)
    return CollegeID

  