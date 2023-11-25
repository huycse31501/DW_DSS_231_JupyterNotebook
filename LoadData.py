from Grade import *
from CollegeID import * 
import pandas as pd
import json

# CollegeAndGrade = CrawlGradeByCollege()


def LoadToCSV():


    GradeList = CrawlGradeByCollege()



    CollegeListDF = pd.DataFrame(CollegeList)
    GradeListDF = pd.DataFrame(GradeList)


    CollegeListDF.to_csv('College.csv', index=False, encoding='utf-8')
    GradeListDF.to_csv('Grade.csv', index=False, encoding='utf-8')



LoadToCSV()