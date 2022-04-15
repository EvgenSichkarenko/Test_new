import pytest

@pytest.mark.login
def test_login(app):
	app.login.login(text1="testatt@inboxbear.com", text2="1234Qwer")