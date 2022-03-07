import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(r'/usr/local/bin/chromedriver', options=options)

    URL = 'https://comic.naver.com/webtoon/detail?titleId=769209&no=46'

    driver.get(URL)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'), S('Height'))
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

    driver.quit()