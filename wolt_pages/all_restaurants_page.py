from playwright.async_api import expect

from wolt_pages.base_page import BasePage
from wolt_pages.restaurant_page import RestaurantPage


class RestaurantsPage(BasePage):
    # All Restaurants locator list
    RESTAURANTS_OBJECTS_LIST_LOCATOR = "[data-test-id=\"VenueVerticalListGrid\"]"

    FIRST_RESTAURANT_LOCATOR = ".s47e3xb > a"
    DIV_RESTAURANT_NAME_LOCATOR = "div[class*='dllhz82']"
    RESTAURANT_NAME_LOCATOR = ".dllhz82"
    MAIN_RESTAURANTS_PAGE_BODY_LOCATOR = "main"

    def get_all_restaurant_names(self, return_text=True):
        """
        Capture all restaurant names within the page
        """
        restaurant_elements = self.locate(self.RESTAURANT_NAME_LOCATOR)
        # Extract name content from each restaurant card
        restaurant_names = [self.get_text(element).strip() for element in restaurant_elements.element_handles()]

        return restaurant_names

    def locate_restaurant_card_object_by_name(self, restaurant_name_input):
        """
        Dynamically locate a specific restaurant card by its name.
        Returns the restaurant card object while storing the display name for validation.
        """
        restaurant_cards = self.locate(self.RESTAURANTS_OBJECTS_LIST_LOCATOR).locator(self.RESTAURANT_NAME_LOCATOR)

        # Iterate through the restaurant cards
        for restaurant_card in restaurant_cards.element_handles():
            card_text = self.get_text(restaurant_card)
            print(card_text)
            if restaurant_name_input in card_text:
                # Store the display name for validation
                self.restaurant_display_name = card_text
                return restaurant_card

        self.logger.info(f"Restaurant '{restaurant_name_input}' not found.")
        self.restaurant_display_name = None
        return None

    def go_to_restaurant_page(self, restaurant_name):
        """
        Click on a specific restaurant card and navigate to the restaurant page.
        """
        restaurant_card = self.locate_restaurant_card_object_by_name(restaurant_name)
        if not restaurant_card:
            raise ValueError(f"Restaurant '{restaurant_name}' not found.")

        restaurant_card.click()
        return RestaurantPage(self.page)

    def get_restaurant_display_card_name_for_validation(self):
        """
        Retrieve the display name of the last located restaurant card.
        """
        if hasattr(self, "restaurant_display_name") and self.restaurant_display_name:
            return self.restaurant_display_name
        else:
            raise ValueError("No restaurant display name has been captured.")



    def wait_for_restaurants_list_to_load(self):
        self.wait_for(self.RESTAURANTS_OBJECTS_LIST_LOCATOR)
        self.locate(self.RESTAURANTS_OBJECTS_LIST_LOCATOR).is_visible()

    def wait_for_first_restaurant_to_load(self):
        self.wait_for(self.FIRST_RESTAURANT_LOCATOR)
        self.locate(self.FIRST_RESTAURANT_LOCATOR).is_visible()

    def interact_with_all_restaurants(self):
        """
        Iterate through all restaurant cards, enter to respecitve page and test if name is equal.
        """

        restaurant_cards = self.locate('[data-test-id^="venueCard."]')  # dynamic locator
        for i in range(restaurant_cards.count()):
            restaurant_card = restaurant_cards.nth(i)
            restaurant_card_name = restaurant_card.locator(self.RESTAURANT_NAME_LOCATOR).text_content()
            print(f"Restaurant name in Page: {restaurant_card_name}")

            restaurant_card.click()

            restaurant_page = RestaurantPage(self.page)
            restaurant_page.wait_for_restaurant_to_load()
            restaurant_page.verify_restaurant_name(restaurant_card_name)

            self.navigate_back()  # Navigate back after clicking
