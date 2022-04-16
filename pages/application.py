from selenium import webdriver
from pages.login import Login
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Application:
	def	__init__(self):
		#self.wd = webdriver.Chrome(executable_path="C:\\Python_project\\Test_Sotka\\drivers\\chromedriver.exe")
		#self.wd = webdriver.Chrome(executable_path="/home/ubuntu/drivers/chromedriver")
		self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		self.login = Login(self)


	def destroy(self):
		self.wd.quit()