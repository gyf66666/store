'''
    python自动化刷抖音
'''

from appium  import  webdriver
import  time

server = "http://localhost:4723/wd/hub"
param = {
			  "deviceName": "b897ce07",
			  "platformName": "Android",
			  "platformVersion": "10",
			  "appPackage": "com.ss.android.ugc.aweme",
			  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
			  "noReset":True
}
# 启动这个软件
driver = webdriver.Remote(server,param)


# 自己写刷抖音

while True:
	time.sleep(5)
	start_x = 500
	start_y = 1300
	distance = 1000
	driver.swipe(start_x,start_y,start_x,
				 start_y - distance)























