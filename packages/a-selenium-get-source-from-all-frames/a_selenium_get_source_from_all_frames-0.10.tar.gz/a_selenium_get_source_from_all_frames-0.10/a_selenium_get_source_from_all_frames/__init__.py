import re
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from selenium.webdriver.common.by import By


def get_sourcecode_from_all_frames(
    driver,
):
    driver.switch_to.default_content()
    sleep(.5)
    df = get_df(driver, By, WebDriverWait, expected_conditions, queryselector="*", with_methods=False, )
    alltext=df.loc[df.aa_localName.str.contains('html', na=False,flags=re.I)].aa_outerHTML.to_list()
    driver.switch_to.default_content()
    return alltext
