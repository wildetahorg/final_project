from .base_page import BasePage as BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def item_correctly_added_to_basket(self):
        self.should_be_add_button()
        self.add_item_to_basket()
        self.check_message_about_item()
        self.check_basket_price()
    
    def item_correctly_added_to_basket_with_promo(self):
        self.should_be_add_button()
        self.add_item_to_basket()
        self.solve_quiz_and_get_code()
        self.check_message_about_item()
        self.check_basket_price()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"
    
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_basket_button.click()

    def check_message_about_item(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_ITEM_MESSAGE), "There is no message about siccessfull item adding"
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME)
        item_name_text = item_name.text
        added_name_text = added_name.text
        assert added_name_text == item_name_text, "Incorrect name of item"

    def check_basket_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        item_price_number = item_price.text
        basket_price_number = basket_price.text
        assert item_price_number == basket_price_number, "Incorrect price in the basket"

    def there_is_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_ITEM_MESSAGE), "There is message about successfull item adding when it shoudn't disappear"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_ITEM_MESSAGE), "Success message don't disappear when it should"