from selenium.webdriver.remote.errorhandler import ErrorHandler


class TolerantErrorHandler(ErrorHandler):
    def check_response(self, response):
        try:
            super(TolerantErrorHandler, self).check_response(response)
        except Exception as e:
            print(str(e).replace("\n", " ").replace("\r", " "))


def add_ignore_exception(driver):
    driver.error_handler = TolerantErrorHandler()
    return driver
