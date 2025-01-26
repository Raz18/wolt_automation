import os
from dotenv import load_dotenv


class AppSettings:
    """
    Application settings for the Wolt Discovery Page automation framework.
    These settings are used for configuring test runs and global parameters.
    """
    load_dotenv()

    BASE_URL = os.getenv("BASE_URL")
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    USER_EMAIL = os.getenv("USER_EMAIL")
    BROWSER_ARGS = os.getenv("BROWSER_ARGS", "").split(",")

    @staticmethod
    def get_base_url():
        """Returns the base URL for the application."""
        return AppSettings.BASE_URL

    @staticmethod
    def is_headless():
        """Returns whether the browser should run in headless mode."""

        return bool(AppSettings.HEADLESS)

    @staticmethod
    def get_user_email():
        """Returns the user email for the application."""
        return AppSettings.USER_EMAIL

    @staticmethod
    def get_browser_args():
        """Returns the browser arguments for the application."""
        return AppSettings.BROWSER_ARGS
