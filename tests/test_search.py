import pytest

from wolt_pages.discovery_page import DiscoveryPage


@pytest.mark.parametrize("restaurant_name, expected_found", [
    ("nono", True),  # Valid restaurant name
    ("Red Sun Sushi", True),  # Another valid restaurant name
    ("InvalidName", False),  # A non-existent restaurant name
    ("", False),  # Empty search input
    ("   ", False),  # Whitespace input
])
def test_search_functionality(browser_session, restaurant_name, expected_found):
    """
    Test the search functionality on Wolt with multiple restaurant names.

    Args:
        browser_session: Browser instance provided by the fixture.
        restaurant_name: The name of the restaurant to search for.
        expected_found: Whether the restaurant is expected to be found.
    """
    discovery_page = DiscoveryPage(browser_session)

    # Perform the search
    discovery_page.search_on_wolt(restaurant_name)
