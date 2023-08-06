# Get the whole updated HTML source code from every frame (not driver.page_source)

#### https://stackoverflow.com/a/71763545/15096247

**To conclude where as the page source obtained from driver.page_source is more or less is an artist's impression of the DOM Tree, Element.outerHTML gets the serialized HTML fragment describing the element including its descendants.**

```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10

$pip a-selenium-get-source-from-all-frames

from time import sleep
from a_selenium_kill import add_kill_selenium
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc
from a_selenium_get_source_from_all_frames import get_sourcecode_from_all_frames


@add_kill_selenium  # https://github.com/hansalemaos/a_selenium_kill
def get_driver():
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )  # https://github.com/hansalemaos/auto_download_undetected_chromedriver
    driver = uc.Chrome(driver_executable_path=path)
    return driver


if __name__ == "__main__":
    folderchromedriver = "f:\\seleniumdriver3"
    path = download_undetected_chromedriver(
        folder_path_for_exe=folderchromedriver, undetected=True
    )
    driver = get_driver()
    driver.get(r"https://demo.guru99.com/test/guru99home/")
    sleep(4)
    source = get_sourcecode_from_all_frames(
        driver,
    )

    
	
```




