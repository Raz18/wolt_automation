import pytest

from wolt_pages.discovery_page import DiscoveryPage


@pytest.mark.parametrize("restaurant_name, expected_visible", [
    ("NonoMimi", True),             # Valid restaurant name
    ("Japanika", True),             # Another valid restaurant name,
    ("nonexistent", False)            # Non-existent restaurant name
])

def test_search_functionality(browser_session, restaurant_name, expected_visible):
    """
    Test the search functionality on Wolt with multiple restaurant names.
    """
    # Arrange
    discovery_page = DiscoveryPage(browser_session)

    # Perform the search
    result_visible = discovery_page.search_on_wolt(restaurant_name)
    # Assert
    assert result_visible == expected_visible, f"Expected restaurant '{restaurant_name}' to be {'visible' if expected_visible else 'not visible'}"

