from .pages.product_page import ProductPage
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.item_correctly_added_to_basket()
    time.sleep(15)
