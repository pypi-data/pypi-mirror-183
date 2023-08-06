# No more getting stuck with not reacting URLs


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10

$pip install a-selenium-get-with-timeout


from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc

from a_selenium_get_with_timeout import get_site_with_timeout

if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(folder_path_for_exe=folderchromedriver, undetected=True)
    driver = uc.Chrome(driver_executable_path=path)
    url=r"https://www.whitehouse.gov/"
    get_site_with_timeout(driver, url, timeout=5, ready_state=True)

```

