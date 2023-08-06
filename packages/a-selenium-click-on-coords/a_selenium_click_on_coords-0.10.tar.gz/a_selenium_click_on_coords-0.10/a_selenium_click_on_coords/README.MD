# Selenium mouse clicks on x,y coordinates 

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-click-on-coords

from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from time import sleep
from a_selenium_click_on_coords import click_on_coordinates
if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = uc.Chrome(driver_executable_path=path)
    driver.get(r"https://github.com/hansalemaos/a_cv2_easy_resize")
    sleep(2)
    click_on_coordinates(driver,x=100,y=100, script_timeout=10)
    
```




