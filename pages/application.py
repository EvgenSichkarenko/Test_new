from selenium import webdriver
from pages.login import Login


class Application:
	def	__init__(self):
		#self.wd = webdriver.Chrome(executable_path="C:\\Python_project\\Test_Sotka\\drivers\\chromedriver.exe")
		self.wd = webdriver.Chrome(executable_path="/home/ubuntu/drivers/chromedriver")
		self.login = Login(self)


	def destroy(self):
		self.wd.quit()