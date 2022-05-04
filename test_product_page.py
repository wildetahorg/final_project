from .pages.product_page import ProductPage
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button
    page.add_item_to_basket
    time.sleep(20)
    # page.solve_quiz_and_get_code
    # page.check
