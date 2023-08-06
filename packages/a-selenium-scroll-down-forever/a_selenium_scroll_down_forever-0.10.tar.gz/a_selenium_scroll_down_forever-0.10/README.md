# Scrolls down on a page

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-scroll-down-forever

from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from time import sleep
from a_selenium_scroll_down_forever import scroll_down_forever


if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    driver.get(r"https://github.com/hansalemaos/a_cv2_easy_resize")
    sleep(2)
    scroll_down_forever(
        driver,
        pause_between_scrolls=(0.5, 0.1),
        max_scrolls=10,
        timeout=3,
        script_timeout=1,
    )
    
```




