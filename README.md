# Wolt Automation Infrastructure

End-to-end robust test automation infrastructure on wolt deliveries website
## **Table of Contents**
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Key Design Philosophy](#key-design-philosophy)
- [Running the Tests](#running-the-tests)
- [Environment Variables](#environment-variables)
- [Writing New Tests](#writing-new-tests)
- [Troubleshooting](#troubleshooting)

# Overview

This repository contains a robust automation framework for testing the core functionality of the Wolt site, including sign in and search. 

It leverages Pytest and Playwright under the Page Object Model architecture, providing an easily maintainable, scalable, and developer-friendly setup.

**Key Features:**

1) Pytest + Playwright

Utilizes Playwright for reliable end-to-end browser automation.
Works seamlessly with Pytest’s rich ecosystem (fixtures, parametrization, etc.).

2)Page Object Model (POM)
Each page and his dedicated locators are represented by a dedicated class under wolt_pages/.

3) Command-Line Browser Selection

Choose your browser with a simple CLI option, e.g. --browser_type=chromium, --browser_type=firefox, or --browser_type=webkit.
Enables easy cross-browser testing without code changes.

4) Screenshot on Failure

Automatically captures and saves screenshots in the screenshots/ directory whenever a test fails.
Increases visibility into failures and simplifies debugging.

5) Logging Setup

Centralized logging configuration via logging.ini.
Logs are captured throughout test execution, making it easier to trace issues.

## Project Structure


```bash
wolt-automation/
│
├── config/
│   ├── __init__.py
│   ├── settings.py              # AppSettings class (reads .env file for configs like BASE_URL, headless mode)
│
├── pages/                       # Page Object Model (POM) classes
│ 
│   ├── base_page.py             # BasePage class with reusable methods for all pages
│   ├── discovery_page.py        # DiscoveryPage class for home/discovery page actions
│   ├── login_card.py            # LoginCard class for login functionality
│   ├── restaurants_page.py      # RestaurantsPage class for actions inside the page 
│   ├── all_restaurants_page.py  # AllRestaurantsPage class for listing and interacting with restaurants, in all restaurants page
│   ├── checkout_page.py         # CheckoutPage class to mock and simulate the checkout process
│
├── tests/                       # Test scripts for various features
│   ├── __init__.py
│   ├── test_e2e_wolt.py         # End-to-end test for Wolt restaurant
│   ├── test_search.py           # Tests for search functionality
│   ├── test_sign_in.py          # Tests for login functionality
│   ├── test_checkout.py         # Tests for the checkout process
│
├── utils/                       # Utility functions and helpers
│   ├── __init__.py
│   ├── logger.py                # Custom logger configuration
│
├── screenshots/                 # Screenshots directory (dedicated)
│   ├── <screenshot files>.png   # Screenshots saved during test execution
│
├── reports/                     # Reports generated after test runs
│
├── .env                         # Environment variables for sensitive configs
├── requirements.txt             # Python dependencies for the project
├── pytest.ini                   # Pytest configuration (e.g., markers, options)
├── .gitignore                   # Git ignore file for unwanted files (e.g., __pycache__)
├── README.md                    # Project documentation and setup instructions


```

**Key Design Philosophy**

The Wolt Automation Framework is designed with a focus on **reusability**, **readability**, and **scalability**. Here's how these principles are embedded throughout the framework:

---

### **1. Reusability**
To minimize duplication and ensure a modular structure, all commonly used methods are encapsulated in classes and designed to be shared across different test cases and page objects.

#### **Example: BasePage**
- The `BasePage` class provides generic methods for interacting with web elements, such as:
- `locate`: Find elements dynamically.
- `click_element`: Perform click actions with retries.
- `write_on_element`: Enter text into input fields.
- `wait_for`: Wait for elements to become visible or interactable.
- `take_screenshot`: Capture a screenshot for debugging.
- These methods are inherited by all other page classes, making the implementation consistent and reusable.

### **2. Readability**
The framework is designed to ensure clarity and ease of understanding, making it easier to debug, maintain, and extend. This is achieved through structured code, descriptive methods, and integrated logging and reporting.

---

#### **Structured Locators**
Locators are declared as constants at the top of each page class. This ensures:
- Easy reference and updates when locators change.
- Better readability by avoiding hardcoded locators scattered throughout the code.

Example:
```python
class DiscoveryPage(BasePage):
    SEARCH_BAR = "input[placeholder='Search in Wolt...']"
    DISCOVERY_TAB = "Discovery"
    RESTAURANTS_TAB = "Restaurants"

```
### **3. Scalability**
The framework is designed to support growth, allowing new tests, pages, and features to be added seamlessly.

#### **Page Object Model (POM)**
Each page or feature of the Wolt platform is represented by a dedicated class. This ensures that:
- New features can be added as separate classes without interfering with existing ones.
- Code is modular and easy to maintain.
- Interactions with the application are logically grouped by functionality.

For example:
- `DiscoveryPage`: Handles actions like searching and navigating tabs.
- `LoginCard`: Manages login functionality.
- `RestaurantPage`: Manages interactions specific to individual restaurants.

#### **Environment Configuration**
Key settings such as `BASE_URL`, `BROWSER`, and `HEADLESS` mode are stored in a `.env` file. This makes it easy to:
- Switch between different environments (e.g., staging, production).
- Update configurations without modifying the code.

### **Environment Variables**
The framework uses a `.env` file to store configurable settings. These variables allow you to easily switch between environments and customize the framework without modifying the codebase.

---

#### **Example `.env` File**
Below is an example of the `.env` file that you should create in the root directory of the project:
```env
BASE_URL=https://wolt.com/discovery           # Base URL of the Wolt platform
HEADLESS=True                                 # Run tests in headless mode (True or False)       
USER_EMAIL=your_test_email@example.com        # Email for login functionality
USER_LOCATION=Rishon LeTsiyon                 # Default location for search functionality
```

## **Running the Tests**

The Wolt Automation Framework includes various test scripts to validate functionality across the Wolt platform. Below are the instructions for running these tests.

Follow these steps to clone the repository, navigate to the directory, and run the tests.

### Clone the Repository

```bash
git clone https://github.com/Raz18/wolt_automation.git 
cd wolt-automation
```

### Create and activate a virtual environment 
python -m venv venv

source venv/bin/activate

### Install the project dependencies
pip install -r requirements.txt


### **Run All Tests**
To execute all test cases one by one, use the following command:
```bash
pytest tests/
```
**Available Browser Options**
- `chromium` (default)
- `firefox`
- `webkit`

#### **Command to Run Tests**
To specify a browser type, use the following syntax:

```bash
pytest --browser_type=<browser_name>
```
