import requests
import json
import time
#from pyhive import hive
#from selenium.webdriver import Chrome,ChromeOptions
import traceback
import sys
#from selenium import webdriver
from lxml import etree
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
url1 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
r1 = requests.get(url1, headers)
r1 = json.loads(r1.text)
data_all1 = json.loads(r1["data"])

from pyhive import hive
conn = hive.Connection(host='47.115.24.135', port=10000, username='hht', database='default')
cursor = conn.cursor()
cursor.execute('show tables')

for result in cursor.fetchall():
    print(result)