

from scrapy import Spider
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


class InstaSpider(Spider):
    name = 'instav1'

    chromedriver_path = '/Users/adamsahli/Desktop/Cushion/InstaBot/chromedriver' # Change this to your own chromedriver path!
    webdriver = webdriver.Chrome(executable_path=chromedriver_path)
    sleep(2)
    # Redirects to login page of Instagram
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)

    # Enters login information
    username = webdriver.find_element_by_name('username')
    username.send_keys('Enter username')
    sleep(3)
    password = webdriver.find_element_by_name('password')
    password.send_keys('Enter password')
    sleep(3)

    button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
    sleep(3)
    button_login.click()
    sleep(3)

# Steps that need to be done here:
# Instagram has enterred a security check, which involves sending a message code on your email address
# Some possible way to get the code from the code to the screen and paste it there will again make the bot functional ( Do speak to Ivan, he has done something similar)
#

    # Avoid the additional Not now button
    notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click()

# Goes into the suggestions page and follows a bunch of people ( 50 for now and stores it into an excel to make sure follow button isn't pressed multiple times for the same user)

    handle_httpstatus_list = [404,403]
    allowed_domains = ['instagram.com']
    start_urls = [webdriver.current_url+'explore/people/suggested/']
    custom_settings = {'DOWNLOAD_DELAY':0.5}

    webdriver.get(webdriver.current_url+'explore/people/suggested/')
    sleep(2)
#react-root > section > main > div > div.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm.HVWg4 > div > div > div:nth-child(1) > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button
#react-root > section > main > div > div.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm.HVWg4 > div > div > div:nth-child(1) > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button
    try:
        Data = pd.read_csv('Users_We_Follow.csv')
        usernames = list(Data['users'])
    except:
        usernames = []

    for i in range(1,50):
        user_name = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(i)+']/div[2]/div[1]').text

        if user_name not in usernames:
            button_click = webdriver.find_element_by_css_selector('#react-root > section > main > div > div.DPiy6.Igw0E.IwRSH.eGOV_._4EzTm.HVWg4 > div > div > div:nth-child('+str(i)+') > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button')
            button_click.click()
            sleep(2)
            usernames.append(user_name)




    Data = pd.DataFrame(usernames,columns=['users'])
    Data.to_csv('Users_We_Follow.csv')


    # def parse(self,response):
    #         apps = response.xpath('//*/div/')
    #         items = []
    #         for app in apps:
    #             item = {}
    #             item['User_name'] = app.xpath('./a/div/div/div').extract()
    #             items.append(item)
    #             #print(items)
    #         return items
