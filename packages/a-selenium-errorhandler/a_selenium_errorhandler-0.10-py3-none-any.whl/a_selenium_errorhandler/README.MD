# Ignores all ChromeDriver Exceptions, returns the Exception(s) as string


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-errorhandler

from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from a_selenium_errorhandler import add_ignore_exception


if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    driver = add_ignore_exception(driver)

    # You can check if an executed command threw an Exception
    e1 = driver.find_element(By.CSS_SELECTOR, "not existing")
    if isinstance(e1, str):
        print("failed")
    else:
        print(e1)
        print("success")
    print("------------------")
    e1 = driver.find_element(By.CSS_SELECTOR, "*")
    if isinstance(e1, str):
        print("failed")
    else:
        print(e1)
        print("success")
```


