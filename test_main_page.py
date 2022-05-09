from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,link)
    login_page = LoginPage(browser,browser.current_url)

    page.open() 
    page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    basket_page = BasketPage(browser, link)

    page.open()
    page.go_to_basket()
    basket_page.shoud_not_be_items_in_basket()
    basket_page.should_be_empty_basket_message()
