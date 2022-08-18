from tqdm import tqdm
import time
import requests
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import pyautogui
import time

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
name_list = []
for i in tqdm(range(1,1234),desc="Whole Progress"):
    num=1
    url = "https://www.namechart.kr/chart/all?gender=t&page={}".format(i)
    req = requests.get(url)
    html = req.text
    html = BeautifulSoup(html,'html.parser')
    for list_data in html.select("div.MuiPaper-root.MuiPaper-elevation.MuiPaper-rounded.MuiPaper-elevation1.MuiCard-root.css-14comn4"):
        for tr in list_data.select("table.MuiTable-root.css-1mzcbh3 tbody.MuiTableBody-root.css-1xnox0e tr"):
            #print(tr)
            for td in tr.select("td.MuiTableCell-root.MuiTableCell-body.MuiTableCell-alignLeft.MuiTableCell-sizeMedium.css-1w1brnc span"):
                name_list.append(td.get_text())
    num+=1
