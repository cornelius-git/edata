import logging

from selenium.webdriver import ChromeOptions
from selenium import webdriver
# import Excleoperate as eo
#输出日志的
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
TIME_OUT = 30
TOTAL_PAGE = 12
from helpInput import connectmysql as cm

#操作浏览器的基础配置
option = ChromeOptions()
#隐藏自动化程序
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
#限制图片加载
prefs={
    'profile.default_content_setting_values': {
        'images': 2}
}
option.add_experimental_option('prefs',prefs)

#开启无界面模式
# option.add_argument("--headless")
# option.add_argument("--disable-gpu")
# wait = WebDriverWait(browser, TIME_OUT)
result = '//*[@id="mainContent"]//h1[@class="srp-controls__count-heading"]/span[@class = "BOLD"]'
# 区分市场
# 'https://www.ebay.de':77,
market_dict = {'https://www.ebay.com':1,'https://www.ebay.co.uk':3,'https://www.ebay.com.au':15}

#主程序
def spiderData(url):
    print("数据自动化程序即将执行，请不要关闭自动打开的浏览器")
    browser = webdriver.Chrome(options=option, executable_path='../../chromedriver.exe')
    #爬取数据
    browser.get(url=url)
    # time.sleep(50)
    f = 1
    while True:
        i = 1
        while True:
            # 循环提取每页内容
            look_count = "no data"
            try :
                commodity_name = browser.find_element_by_xpath('//*[@id="ResultSetItems"]/ul/li[{}]/h3'.format(i)).text
                commodity_link = browser.find_element_by_xpath('//*[@id="ResultSetItems"]/ul/li[{}]/h3/a'.format(i)).get_attribute("href")
                image_link = browser.find_element_by_xpath('//*[@id="ResultSetItems"]/ul/li[{}]/div[1]/div/a/img'.format(i)).get_attribute("src")
                try:
                    # 尝试抓取销售数据
                    look_count = browser.find_element_by_xpath('//*[@id="ResultSetItems"]/ul/li[{}]/ul[1]//div[contains(@class,"hotness-signal")]' .format(i)).text
                    # if look_count:
                    #     look_count_result = ""
                    #     for gh in look_count:
                    #         look_count_result = str(look_count_result) + ";" + gh.text
                except Exception as e:
                    # print(e)
                    pass
                # print(i)
                i+=1
                # print(name,look_count,look_url)
                itemid = commodity_link.split("/")[-1].split('?')[0]
                commodity_name = str(commodity_name)
                cm.shopDataInsert(storename="detroitaxle", produce_type="control arm", itemid=itemid,title=commodity_name,picture=image_link,market="us",sold=look_count)
            except Exception as y:
                # browser.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(inner)
                # browser.find_element_by_xpath('//*[@id="gh-btn"]').click()
                print(y)
                print("第一页内容提取完毕")
                break
        try:
            # 页面class值是唯一值
            browser.find_element_by_xpath('//*[@id="Pagination"]/tbody/tr/td[3]/a').click()
            # print(next_page)
            print("第{}页采集完成，即将采集下一页".format(str(f)))
        except Exception as q:
            print(q)
            print('无翻页')
            break
# print("执行完毕")
    browser.quit()

if __name__ == "__main__":
    # base_url = "https://www.ebay.de/sch/Querlenker-Teile/33583/m.html?_nkw=&_armrs=1&_from=&_clu=2&_fcid=77&_localstpos=&_stpos=&gbr=1&_ssn=atp-autoteile&_ipg=200&rt=nc"
    #base_url = '
    base_url = 'https://www.ebay.com/sch/Control-Arms-Parts/33583/m.html?_nkw=&_armrs=1&_from=&_ssn=detroitaxle&_fcid=1&_ipg=200&rt=nc'
    spiderData(url=base_url)