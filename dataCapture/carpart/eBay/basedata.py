import logging
import time

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
def spiderData(url,inner):
    print("数据自动化程序即将执行，请不要关闭自动打开的浏览器")
    browser = webdriver.Chrome(options=option, executable_path='../../chromedriver.exe')
    #爬取数据
    search_name = str(inner).replace(" ","+")
    market = []
    for mark_url,mark_id in market_dict.items():
        area = mark_url.split('.')[-1]
        if area == "com":
            area = "us"
        else:
            pass
        for page in range(0,10):
            #页面内容提取
            print(page)
            browser.get(url.format(mark_url,search_name,mark_id,page+1))
            time.sleep(1)
            i = 1
            while True:
                # 循环提取每页内容
                look_count_result = "no data"
                try :
                    commodity_name = browser.find_element_by_xpath('//*[@id="srp-river-results"]/ul/li[{}]/div/div[2]/a/h3'.format(i)).text
                    commodity_link = browser.find_element_by_xpath('//*[@id="srp-river-results"]/ul/li[{}]/div/div[2]/a'.format(i)).get_attribute("href")
                    image_link = browser.find_element_by_xpath('//*[@id="srp-river-results"]/ul/li[{}]/div/div[1]/div/a/div/img'.format(i)).get_attribute("src")
                    try:
                        # 尝试抓取销售数据
                        look_count = browser.find_elements_by_xpath('//*[@id="srp-river-results"]/ul/li[{}]/div/div[2]//span[contains(@class,"BOLD")]' .format(i))
                        if look_count:
                            look_count_result = ""
                            for gh in look_count:
                                look_count_result += gh.text
                    except Exception as e:
                        pass
                    # print(i)
                    i+=1
                    # print(name,look_count,look_url)
                    judege = "no"
                    itemid = commodity_link.split("/")[-1].split('?')[0]
                    if "control arm".upper() in str(commodity_name).upper():
                        judege = 'yse'
                    commodity_name = str(commodity_name) +"@"+"carparts"
                    cm.dataSql(itemid=itemid,title=commodity_name,picture=image_link,oe=inner,market=area,judege=judege,sold=look_count_result)
                except Exception as y:
                    # browser.find_element_by_xpath('//*[@id="gh-ac"]').send_keys(inner)
                    # browser.find_element_by_xpath('//*[@id="gh-btn"]').click()
                    print("第一页内容提取完毕")
                    break
            try:
                # 页面class值是唯一值
                next_page = browser.find_element_by_xpath('//*[contains(@class,"pagination__next")]')
                # print(next_page)
                next_page_judge = next_page.get_attribute('aria-disabled')
                print(next_page_judge)
                if next_page_judge:
                    break
                else:
                    continue
            except Exception as q:
                print(str(inner)+'采集完毕'+'\t'+'无下一页')
                break
        # print("执行完毕")
    browser.quit()

if __name__ == "__main__":
    base_url = "{}/sch/i.html?_from=R40&_nkw={}&_sacat=0&LH_TitleDesc=0&_ipg=200&_fcid={}&_pgn={}"
    spiderData(url=base_url,inner="68029903AC")