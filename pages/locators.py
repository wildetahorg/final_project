from selenium.webdriver.common.by import By

class  BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
# class MainPageLocators():
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    RGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_COMFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_ITEM_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) .alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")

class BasketPageLocators():
    SOME_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
