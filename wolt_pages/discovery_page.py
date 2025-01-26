from wolt_pages.base_page import BasePage
from wolt_pages.all_restaurants_page import RestaurantsPage
from wolt_pages.login_card import LoginCard

class DiscoveryPage(BasePage):
    SEARCH_BAR_LOCATOR = "input[placeholder='Search in Wolt...']"
    RESTAURANTS_TAB_LOCATOR = "Restaurants"
    LOCATION_INPUT_LOCATOR="[data-test-id='header.address-select-button.address-text']"
    WOLT_LOGO_LOCATOR="[data-test-id=\"HeaderWoltLogoLink\"]"
    SEARCH_RESULTS_LOCATOR="h1:has-text('Search results')"
    ADDRESS_NAME_LOCATOR="[data-test-id='address-query-input']"
    ADDRESS_CONTINUE_BUTTON_LOCATOR="[data-test-id='continue-button']"
    ADDRESS_SUGGESSTIONS_LIST_LOCATOR="[data-test-id='SuggestionsList']"


    def click_link_via_name(self, name):
        """Click on a link by its name."""
        self.click_element(self.get_by_role("link", name))


    def search_on_wolt(self, search_query):
        """Search for a specific query on Wolt via the search field and check if the text exist after search."""
        self.logger.debug(f"Searching for '{search_query}'...")
        self.write_on_element(self.SEARCH_BAR_LOCATOR, search_query)
        self.page.press(self.SEARCH_BAR_LOCATOR, "Enter")

        #using my restaurant page class to find the names and search for the query
        restaurants_page = RestaurantsPage(self.page)
        restaurants_page.wait_for_restaurants_list_to_load()
        restaurants_names=restaurants_page.get_all_restaurant_names()

        return any(search_query in name for name in restaurants_names)

    def go_to_discovery(self):
        """Navigate back to the Discovery page."""
        wolt_logo=self.locate(self.WOLT_LOGO_LOCATOR)
        self.click_element(wolt_logo)
        return DiscoveryPage(self.page)


    def go_to_restaurants(self):
        """Navigate to the Restaurants page."""
        restaurants_tab=self.get_by_role("tab", self.RESTAURANTS_TAB_LOCATOR)
        self.click_element(restaurants_tab)
        return RestaurantsPage(self.page)

    def click_on_login(self):
        """Click on the login link and navigate to the login card."""
        login_link=self.get_by_role("button", "Log in")
        self.click_element(login_link)
        return LoginCard(self.page)

    def set_location(self, location="Rishon LeTsiyon"):
        """Click on the location input field."""
        self.locate(self.click_element(self.LOCATION_INPUT_LOCATOR))
        self.wait_for(self.ADDRESS_NAME_LOCATOR)
        self.write_on_element(self.ADDRESS_NAME_LOCATOR, location)
        #self.page.press(self.ADDRESS_NAME_LOCATOR, "Enter")
        #self.wait_for(self.ADDRESS_SUGGESSTIONS_LIST_LOCATOR)
        self.click_element(self.get_by_role("option", location).first)

        self.click_element(self.ADDRESS_CONTINUE_BUTTON_LOCATOR)







