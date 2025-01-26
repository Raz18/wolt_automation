import re

from wolt_pages.base_page import BasePage
from wolt_pages.checkout_page import CheckoutPage


class RestaurantPage(BasePage):
    # main restaurant card locators
    RESTAURANT_CARD = "[data-test-id='venue-page-content-layout']"
    RESTAURANT_CARD_NAME = "[data-test-id='venue-hero\\.venue-title']"
    RESTAURANT_INFO_CARD_BUTTON_LOCATOR = "[data-test-id=\"venue-more-info-button\"]"
    RESTAURANT_INFO_CARD_LOCATOR = "[data-test-id=\"VenueInformationModal\"]"
    RESTAURANT_MINIMUM_ORDER_LOCATOR = "p:has-text('Small order surcharge limit') span.d1whud0i"

    # food sections locators inside restaurant page
    FOOD_SECTIONS_TEMPLATE = "div:nth-child({}) > .ra524sa > .ij4681s"
    FOOD_SECTIONS_PARENT = ".ra524sa"

    # SPECIFIC food items locators inside food sections
    FOOD_OPTIONS_PAGE_MAIN_LOCATOR = "[data-test-id=\"product-options-form\"]"
    FOOD_ITEMS_WITHIN_SECTION = ":scope > div"
    FIRST_FOOD_ITEM = ":scope > div:first-child"
    FOOD_ITEMS_BASED_ON_SECTION_LOCATOR="[data-capture-id=\"section\"]"
    FOOD_ITEMS_CHECKBOX_LOCATOR='input[type="checkbox"]'


    # add to cart locators
    ADD_TO_CART_BUTTON_LOCATOR = "[data-test-id=\"product-modal\\.submit\"]"
    CLICK_TO_CHECKOUT_BUTTON_LOCATOR = "[data-test-id=\"CartViewNextStepButton\"]"
    TOTAL_PRICE_LOCATOR = "[data-test-id=\"CartViewTotalPrice\"]"
    CART_VIEW_LOCATOR = "[data-test-id=\"cart-view-button\"]"

    def wait_for_restaurant_page_to_load(self):
        """Wait for the specific restaurant page to load."""
        self.wait_for(self.RESTAURANT_CARD)

    def verify_restaurant_name(self, restaurant_name):
        """Verify the restaurant name on the card is same as in the card title in all restaurants page,
        for validation."""
        actual_name_in_card = self.locate(self.RESTAURANT_CARD_NAME).text_content()
        print(f"Restaurant name in Card: {actual_name_in_card}")
        if restaurant_name not in actual_name_in_card:
            raise ValueError \
                (f"Expected restaurant name '{restaurant_name} on card', but found '{actual_name_in_card}, probably not the same restaurant.")
        return True

    def food_section_locator(self, section_index):
        """Generate locator for a specific food section."""
        return self.FOOD_SECTIONS_TEMPLATE.format(section_index)

    def click_on_add_to_cart_button(self):
        """Click on the 'Add to cart' button."""
        self.locate(self.click_element(self.ADD_TO_CART_BUTTON_LOCATOR))


    def click_on_show_cart_button(self):
        """Click on the 'Show cart' button."""
        self.locate(self.click_element(self.CART_VIEW_LOCATOR))


    def proceed_to_checkout(self):
        """
        Click on the 'Show cart' button, simulating the checkout process.
        """
        print("Clicking on checkout button.")
        return CheckoutPage()

    def restaurant_minimum_order_value(self):
        """Extract the minimum order value of the restaurant."""
        self.locate(self.RESTAURANT_INFO_CARD_BUTTON_LOCATOR).click()
        minimum_order = self.get_text(self.locate(self.RESTAURANT_MINIMUM_ORDER_LOCATOR)).strip('₪')
        self.navigate_back()
        return float(minimum_order)


    def total_price_value(self):
        """Return the total price of the cart."""
        self.locate(self.click_element(self.CART_VIEW_LOCATOR))
        total_price = self.get_text(self.locate(self.TOTAL_PRICE_LOCATOR)).strip('₪')
        return float(total_price)


    def add_food_items_on_specified_sections(self, start=2, end=3):
        """
        Add first food item in any given range of food sections.

        Iterates through selected food sections, replacing `n` in the template,
        and clicks the first food item in each section, adding it to the cart.
        """

        # Template for dynamically locating sections
        self.logger.info(f"Adding food items from sections {start} to {start + end - 1}.")

        for section_number in range(start, start + end):
            # Replace `n` in the template to locate the section
            food_section_locator = self.FOOD_SECTIONS_TEMPLATE.format(section_number)
            self.logger.info(f"Locating section #{section_number}: {food_section_locator}")

            # Locate the section
            section = self.locate(food_section_locator)

            # Check if the section is visible
            if section.is_visible():
                self.logger.info(f"Section #{section_number} is visible. Adding the first food item.")

                try:
                    # Click the first food item in the section
                    first_food_item = section.locator(self.FIRST_FOOD_ITEM)
                    first_food_item.click()

                    # Wait for the "Add to Cart" button to appear
                    self.wait_for(self.ADD_TO_CART_BUTTON_LOCATOR)

                    # Click the "Add to Cart" button
                    self.click_on_add_to_cart_button()
                    self.logger.info(f"Successfully added food item from section #{section_number} to the cart.")

                except Exception as e:
                    self.logger.error(f"Failed to add food item from section #{section_number}: {e}")

            else:
                self.logger.warning(f"Section #{section_number} is not visible or does not exist. Skipping.")

        self.logger.info("Completed adding food items from specified sections.")
