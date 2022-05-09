from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def shoud_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SOME_ITEM), "There is some element in the basket when it shouldn't"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no message about empty basket"
