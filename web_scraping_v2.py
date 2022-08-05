import pandas as pd
import pyrebase
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="G:\chromedriver_win32 (1)\chromedriver.exe")
# driver.navigate().to("https://www.amazon.ca/")
products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2.")
# driver.get("https://www.amazon.ca")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
# soup = BeautifulSoup(content)#, features="html.parser")
# print(soup)
# import pdb
# pdb.set_trace()
# for a in soup.findAll('a', href=True, attrs={'class': '_3pLy-c row'}):
for a in soup.findAll('div', attrs={'class': '_3pLy-c row'}):
    # name = a.find('div', attrs={'class': '_3wU53n'})
    # print(name)
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    # rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
    # products.append(name.text)
    prices.append(price.text)
    # ratings.append(rating.text)
    
# print(prices)
pd.plot(sinx(prices))

firebaseConfig = {
  "apiKey": "AIzaSyD-RVdcxd_6dskD1W6DdFA0KrMEnxcJVd4",
  "authDomain": "fir-frompython.firebaseapp.com",
  "databaseURL": "https://fir-frompython-default-rtdb.firebaseio.com",
  "projectId": "fir-frompython",
  "storageBucket": "fir-frompython.appspot.com",
  "messagingSenderId": "529313000758",
  "appId": "1:529313000758:web:ec25dcd2311c359fa61797",
  "measurementId": "G-N4VQM7B0M6",
    "databaseURL" : "https://fir-frompython-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
database1 = firebase.database()
database1.child("laptop_prices").child("Prices").set(prices)