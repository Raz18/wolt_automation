from time import sleep

from wolt_pages.base_page import BasePage
from wolt_pages.all_restaurants_page import RestaurantsPage
from wolt_pages.login_card import LoginCard


class DiscoveryPage(BasePage):
    SEARCH_BAR = "input[placeholder='Search in Wolt...']"
    DISCOVERY_TAB = "Discovery"
    RESTAURANTS_TAB = "Restaurants"
    ALL_LINKS_LOCATOR= "Restaurants Groceries Pharmacies Alcohol Pet Supply Health&Beauty Electronics"
    LOCATION_INPUT_LOCATOR="[data-test-id='header.address-select-button.address-text']"


    def click_link_via_name(self, name):
        """Click on a link by its name."""
        self.click_element(self.get_by_role("link", name))


    def search_on_wolt(self, query):
        """Search for a specific query on Wolt via the search field."""
        self.logger.debug(f'searching {query}...')
        self.write_on_element(self.SEARCH_BAR, query)
        self.page.press(self.SEARCH_BAR, "Enter")



    def go_to_restaurants(self):
        """Navigate to the Restaurants page."""
        restaurants_tab=self.get_by_role("tab", self.RESTAURANTS_TAB)
        self.click_element(restaurants_tab)
        return RestaurantsPage(self.page)

    def click_on_login(self):
        """Click on the login link and navigate to the login card."""
        login_link=self.get_by_role("button", "Log in")
        self.click_element(login_link)
        return LoginCard(self.page)

    def click_on_location_input(self):
        """Click on the location input field."""
        self.locate(self.click_element(self.LOCATION_INPUT_LOCATOR))
        sleep(3)


