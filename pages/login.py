from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Login:
	def __init__(self, app):
		self.app = app


	def login(self, text1, text2):
		wd = self.app.wd
		wd.get("https://trialbase.com/login")
		login = WebDriverWait(wd, 10).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
		login.send_keys(Keys.CONTROL + "a")
		login.send_keys(Keys.BACK_SPACE)
		login.send_keys(text1)

		password = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		password.send_keys(Keys.CONTROL + "a")
		password.send_keys(Keys.BACK_SPACE)
		password.send_keys(text2)
		wd.find_element(By.CSS_SELECTOR, "button[name='registrationSignInBtn']").click()