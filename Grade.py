from CollegeID import *
from bs4 import BeautifulSoup
import requests


collegeList = CrawlCollegeID()

def CrawlGradeByCollege():
    CollegeGrade = []
    for college in collegeList:
        for year in range(2016,2023):
            url = college[1].replace("year",f"{year}")
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            if not soup.find("table"):
                continue
            else:
                GradeTableInfo = soup.find("div", {"class": "dataTable__main"}).find("table").find("tbody").findAll("tr")
            for Grade in GradeTableInfo:
                dataList = []
                dataList.append(college[3])
                for data in Grade:
                    if data == '\n':
                        continue
                    if data.find("a"):
                        data = data.getText()
                        dataList.append(data[:len(data) - 6])
                    else:
                        data = data.getText()
                        dataList.append(data)
                dataList.append(year)
                CollegeGrade.append(dataList)

    return CollegeGrade

CrawlGradeByCollege()

