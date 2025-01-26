from wolt_pages.base_page import BasePage


class LoginCard(BasePage):
    NEXT_BUTTON_LOCATOR = "[data-test-id=\"StepMethodSelect\\.NextButton\"]"
    MAIL_SUCCESS_MESSAGE_LOCATOR = "Great, check your inbox!"
    INVALID_EMAIL_MESSAGE_LOCATOR = "[data-test-id='MethodSelect.EmailInputError']"

    def wait_for_login_card(self):
        """Wait for the login card to appear."""
        self.wait_for(self.get_by_role("input", "email"))

    def enter_email(self, email):
        """Enter the email and submit the form."""
        self.write_on_element("input[name='email']", email)
        self.click_element(self.NEXT_BUTTON_LOCATOR)

    def sign_in_mail_sent_successful(self):
        """Check if the sign-in mail sent success message is visible."""
        email_sent_message = self.get_by_role("heading", self.MAIL_SUCCESS_MESSAGE_LOCATOR)
        self.wait_for(email_sent_message)
        email_sent_message.is_visible()
        return email_sent_message

    def invalid_email_message(self):
        """Check if the invalid email message is visible."""
        email_invalid_message = self.locate (self.INVALID_EMAIL_MESSAGE_LOCATOR)
        self.wait_for(email_invalid_message)
        email_invalid_message.is_visible()
        return email_invalid_message
