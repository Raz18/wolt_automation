from wolt_pages.discovery_page import DiscoveryPage


def test_location_integration(browser_session):
    # Arrange
    discovery_page = DiscoveryPage(browser_session)
    # Act
    discovery_page.click_on_location_input()
    # Assert

