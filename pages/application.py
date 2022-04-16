from selenium import webdriver
from pages.login import Login
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Application:

	def	__init__(self):
		#self.wd = webdriver.Chrome(executable_path="C:\\Python_project\\Test_Sotka\\drivers\\chromedriver.exe")
		#self.wd = webdriver.Chrome(executable_path="/home/ubuntu/drivers/chromedriver")
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument('--no-sandbox')
		self.chrome_options.add_argument('--window-size=1420,1080')
		self.chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('--disable-gpu')
		self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.chrome_options)
		self.login = Login(self)


	def destroy(self):
		self.wd.quit()