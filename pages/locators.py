from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    RGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_ITEM_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
