# Downloads are started automatically 


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-download-without-asking

from a_selenium_download_without_asking import enable_download_without_asking
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc


if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    enable_download_without_asking(driver, download_dir="f:\\testdownload")
    driver.get(
        r"https://github.com/hansalemaos/DigiDeutsch/raw/main/digi_deutsch_setup.exe"
    )
```


