from wolt_pages.discovery_page import DiscoveryPage
from config.app_settings import AppSettings

def test_successful_sign_in(browser_session):
    # Arrange
    discovery_page = DiscoveryPage(browser_session)
    login_flow=discovery_page.click_on_login()
    #login_flow.wait_for_login_card()
    # Act
    login_flow.enter_email(AppSettings.get_user_email())
    login_success_message=login_flow.sign_in_mail_sent_successful()
    # Assert
    assert login_success_message.is_visible(), "Login mail sent message is not visible."

def test_unsuccessful_sign_in(browser_session):
    # Arrange
    discovery_page = DiscoveryPage(browser_session)
    login_flow=discovery_page.click_on_login()
    #login_flow.wait_for_login_card()
    # Act
    login_flow.enter_email("invalid_email")
    invalid_email_message=login_flow.invalid_email_message()
    # Assert
    assert invalid_email_message.is_visible(), "Invalid email message is not visible."






