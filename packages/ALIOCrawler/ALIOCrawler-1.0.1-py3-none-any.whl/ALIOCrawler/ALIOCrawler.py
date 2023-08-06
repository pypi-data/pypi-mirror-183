#!/usr/bin/env python

# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import time
import datetime
import os
import sys
import json
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException
import argparse
from pyfiglet import Figlet

def main():
    f = Figlet(font='big')
    print(f.renderText('ALIOCrawler'))
    print('------------------------')
    print('\n')
    print('If you have any questions, please send your questions to my email.')
    print('\nOr, please suggest errors and areas that need updating.')
    print('\n 📨 woo_go@yahoo.com')
    print('\n')
    print('\nVisit https://github.com/wjgoarxiv/ALIOCrawler for more information.')
    print('\n')
    print('------------------------')
    print('\n')

    # Setting driver options.
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Start argument parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-s', '--search', type=str, help='검색하고자 하는 공고기관의 이름을 입력해주세요 (예시: 울산과학기술원).', default='울산과학기술원')
    parser.add_argument('-o', '--output', type=str, help='검색 결과를 저장할 파일명을 입력해주세요 (예시: ALIO_output). Output 파일은 CSV 파일 형태로 저장됩니다.', default = 'ALIO_output')

    args = parser.parse_args()

    # Assign arguments to variables
    search = args.search # 무엇을 검색할 것인가
    output_file = args.output # 파일 아웃풋 이름은 무엇으로 할 것인가? 

    # Automatically install the matching chromedriver version
    chromedriver_autoinstaller.install()

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome('chromedriver', options=options)

    # Go to the ALIO website 
    driver.get("https://www.alio.go.kr/main.do")

    # 검색란의 XPath는 "//*[@id="content"]/div[1]/div/div/div[1]/div/input" 입니다.
    driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/div[1]/div/input").send_keys(search)
    driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/div[1]/div/input").send_keys(Keys.ENTER)

    # implicit wait 4 sec
    driver.implicitly_wait(4)
    time.sleep(1.5)

    # "//*[@id="content"]/div/div[3]/div/div/button[6]" 버튼을 눌러 "채용정보" 탭으로 진입합니다. 
    driver.find_element(By.XPATH, "//*[@id='content']/div/div[3]/div/div/button[6]").click() 

    driver.implicitly_wait(4)
    time.sleep(1.5)

    print("INFO 입력하신 검색어는 '{}' 입니다.".format(search))
    print("INFO output 파일 이름은 '{}' 입니다.".format(output_file))
    print("INFO 혹시 원하는 인풋 값이 아닌가요? `$ aliocrawler -h` 를 입력해 인풋 값을 변경해보세요!")
    time.sleep(1.2) 

    # Page number identification
    page_num = 1
    while True:
        try:
            driver.find_element(By.XPATH, "//*[@id='content']/div/div[4]/div/dl/dd/div/div[2]/ul/li[{}]/a".format(page_num))
            page_num += 1
        except NoSuchElementException:
            break

    print("INFO 총 페이지 수는 {}개가 있네요. 이제 크롤링을 시작합니다!".format(page_num-1))

    # 페이지 별로 루프를 진행하되, 페이지가 없다면 NoSuchElementException을 발생시킵니다.
    for i in range(1, page_num):
      time.sleep (1)

      try:
        driver.find_element(By.XPATH, "//*[@id='content']/div/div[4]/div/dl/dd/div/div[2]/ul/li[{}]/a".format(i)).click()
      except NoSuchElementException as e:
        pass

      recruit_name = []
      recruit_date = []
      recruit_link = []

      time.sleep(1)

      #한 페이지 내에 있는 공고의 수를 파악합니다.
      recruit_num = 1
      while True:
        try:
          driver.find_element(By.XPATH, "//*[@id='content']/div/div[4]/div/dl/dd/div/div[1]/div/ul/li[{}]".format(recruit_num))
          recruit_num += 1
        except NoSuchElementException:
          break

      print("INFO 현재 페이지에는 {}개의 공고가 있습니다. 공고 정보를 추출하는 데에는 시간이 다소 소요될 수 있습니다.".format(recruit_num-1))
      # 한 페이지 내에 있는 공고의 수만큼 반복문을 돌립니다.
      try:
        for i in range(1, recruit_num):
          recruit_name.append(driver.find_element(By.XPATH, "//*[@id='content']/div/div[4]/div/dl/dd/div/div[1]/div/ul/li[{}]/p[1]/span[3]/a".format(i)).text)
      except NoSuchElementException:
        pass

      try:
        for i in range(1, recruit_num):
          recruit_date.append(driver.find_element(By.XPATH, "//*[@id='content']/div/div[4]/div/dl/dd/div/div[1]/div/ul/li[{}]/p[2]/span[2]".format(i)).text)
      except NoSuchElementException:
        pass

      try:
        for i in range(1, recruit_num):
          # 공고 정보 팝업창을 띄우기 위해 "//*[@id="content"]/div/div[4]/div/dl/dd/div/div[1]/div/ul/li[1]/p[1]/span[3]/a" 버튼을 누릅니다.
          driver.find_element(By.XPATH, "//*[@id='content']/div/div[4]/div/dl/dd/div/div[1]/div/ul/li[{}]/p[1]/span[3]/a".format(i)).send_keys(Keys.ENTER)
          # 새로 팝업된 창을 닫습니다. 기존 창이 닫히지 않도록 주의합니다. 
          driver.switch_to.window(driver.window_handles[1])
          # 팝업창의 URL을 불러옵니다.
          recruit_link.append(driver.current_url)
          driver.close()
          driver.switch_to.window(driver.window_handles[0])

          # 프로그레스 바를 위한 print문입니다. 출력 시 "1/20"과 같이 출력됩니다.
          print("INFO 현재 처리 진행중인 항목 번호:", i, "/", recruit_num-1, end='\r')

      except NoSuchElementException:
        pass 
      
      # 루프를 돌 때마다 데이터프레임을 생성합니다. 내용이 계속해서 추가될 수 있도록 합니다. 헤더는 한 번만 생성하도록 합니다.
      df = pd.DataFrame({"공고명":recruit_name, "공고일":recruit_date, "공고링크":recruit_link})
      # Use output_file as the file name of the output file ('csv')
      df.to_csv(output_file+'.csv', mode='a', encoding='utf-8-sig', index=False, header=False)
      print("INFO 현재 페이지의 크롤링이 완료되었습니다.")

    print("INFO 모든 크롤링이 완료되었습니다. 프로세스를 종료합니다. ")
    print("INFO 현재 디렉토리에 저장된 CSV 파일을 확인해보세요.")
    # driver quit
    driver.quit()
    time.sleep(1)

# entry point
if __name__ == "__main__":
  main()