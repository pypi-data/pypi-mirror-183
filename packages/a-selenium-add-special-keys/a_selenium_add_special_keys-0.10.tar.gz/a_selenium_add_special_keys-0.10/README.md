# Adds some useful keys from the chrome.debugger library to Selenium


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-add-special-keys

from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from a_selenium_add_special_keys import add_special_keys

if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(folder_path_for_exe=folderchromedriver, undetected=True)
    driver = uc.Chrome(driver_executable_path=path)
    driver = add_special_keys(driver)
```



<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/seleniumkeys.png"/>
