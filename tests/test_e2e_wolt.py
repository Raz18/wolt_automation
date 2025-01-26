from time import sleep

from wolt_pages.discovery_page import DiscoveryPage
from wolt_pages.all_restaurants_page import RestaurantsPage
from wolt_pages.restaurant_page import RestaurantPage


def test_restaurants_load_and_click(browser_session):
    discovery_page = DiscoveryPage(browser_session)
    all_restaurants_page = discovery_page.go_to_restaurants()

    # Act: Wait for restaurants list to load
    all_restaurants_page.wait_for_restaurants_list_to_load()

    # Navigate to a specific restaurant,name or first restaurant in the list of all restaurants

    restaurant_page = all_restaurants_page.go_to_restaurant_page("Garage Burger | Rishon LeZion")
    print(f"Navigating to restaurant: 'Abdalla'")

   # get the restaurant name displayed in all restaurants page
    restaurant_display_name_in_all_restaurants_page = all_restaurants_page.get_restaurant_display_card_name_for_validation()

    # Verify restaurant name is the same is in card title
    restaurant_page.wait_for_restaurant_page_to_load()
    assert restaurant_page.verify_restaurant_name(restaurant_display_name_in_all_restaurants_page) is True, \
        f"Restaurant name mismatch: Expected {restaurant_display_name_in_all_restaurants_page}, but was not found."

    # Add food items and calculate total price
    restaurant_page.add_food_items_on_specified_sections(2)

    order_price = restaurant_page.total_price_value()

    #  transition to mocked checkout
    checkout_page = restaurant_page.proceed_to_checkout()

    # Simulate the payment process
    order_status = checkout_page.pay(order_price, restaurant_display_name_in_all_restaurants_page)
    print(f"Order Status: {order_status}")

    # Validate payment success
    assert order_status["status"] == "SUCCESS", f"Payment failed: {order_status['message']}"
