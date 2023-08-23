import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_addition_item_to_the_cart():
    # disable-notifications
    options = Options()
    options.add_argument("--disable-notifications")

    # initialize webdriver
    driver = webdriver.Chrome(
        service=Service(r"C:\\Users\\HP\\Kod-rep" + "chromedriver.exe"),
        options=options,
    )

    # Open URL and maximize window
    driver.get("https://rozetka.com.ua/ua/")
    driver.maximize_window()

    # press the button "Смартфони, ТВ і електроніка"
    phones = driver.find_element(
        By.XPATH,
        "//a[@class='menu-categories__link'][contains(@href, 'telefony-tv-i-ehlektronika/c4627949/')]",
    )
    phones.click()
    time.sleep(1)

    # press the button "Мобільні телефони"
    mobile_phones = driver.find_element(By.XPATH, "//a[text()=' Мобільні телефони ']")
    mobile_phones.click()

    # press the button "Apple iPhone 13 128GB Midnight (MLPF3HU/A)"
    iphone_13 = driver.find_element(
        By.XPATH,
        "//span[text()=' Мобільний телефон Apple iPhone 13 128GB Midnight (MLPF3HU/A) ']",
    )
    iphone_13.click()
    time.sleep(2)

    # press the button "Купити"
    buy = driver.find_element(By.XPATH, "//span[text()=' Купити ']")
    buy.click()
    time.sleep(1)

    # input quantity of Apple iPhone 13 128GB Midnight
    quantity = driver.find_element(
        By.XPATH,
        "//input[@class='cart-counter__input ng-untouched ng-pristine ng-valid']",
    )
    quantity.clear()
    quantity.send_keys(2)

    # press the button "Продовжити покупки"
    continue_shopping = driver.find_element(
        By.XPATH, "//button[text()=' Продовжити покупки ']"
    )
    continue_shopping.click()

    # close browser
    driver.close()
