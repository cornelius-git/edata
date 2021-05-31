import logging
import time

from selenium.webdriver import ChromeOptions
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#输出日志的
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
TIME_OUT = 30
TOTAL_PAGE = 12
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

#主程序
def spiderData(url):
    browser = webdriver.Chrome(options=option, executable_path='../../chromedriver.exe')
    print("数据自动化程序即将执行，请不要关闭自动打开的浏览器")
    #爬取数据
    browser.get(url)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js)
    js = "window.scrollBy(0,900);"
    browser.execute_script(js)
    # js="var q=document.documentElement.scrollTop=900"
    # browser.execute_script(js)
    i=1
    # element = WebDriverWait(browser, 30).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="highlights"]/div')))
    sum_inner = None
    try:
        sum_inner = browser.find_element_by_xpath('//*[@id="highlights"]/div/div[3]/div/div').text
    except Exception as e:
        print("未发现信息")
        pass
    commodity_name = "no exist"
    oe_num = ""
    while True:
        # 循环提取每页内容

        try :
            commodity_name = browser.find_element_by_xpath('//*[@id="highlights"]/div/div[3]/div/div/div[{}]'.format(i)).text
            i+=1
            if 'NUM' in str(commodity_name).upper():
               oe_num = str(oe_num)+','+str(commodity_name.split(':')[1]).replace("\n",'')
               print(oe_num)
        except Exception as y:
            print("第一页内容提取完毕")
            break
    # print(oe_num)
    browser.quit()
    return sum_inner,oe_num


if __name__ == "__main__":
    lh = ['https://www.carparts.com/control-arm/truedrive/rl28150005'
    ,'https://www.carparts.com/control-arm/truedrive/rl28150006'
    ,'https://www.carparts.com/control-arm/truedrive/rl28150007'
    ,'https://www.carparts.com/control-arm/truedrive/rl28150009'
    ,'https://www.carparts.com/control-arm/truedrive/set-rl28150005'
    ,'https://www.carparts.com/control-arm/truedrive/rl28150008'
    ,'https://www.carparts.com/control-arm/truedrive/rl28150010'
    ,'https://www.carparts.com/control-arm/truedrive/rl28150011']
    for fg in lh:
        spiderData(url=fg)