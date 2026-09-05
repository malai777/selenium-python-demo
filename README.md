# selenium-python-demo

# Selenium Login Automation Test

A basic automated test built with Selenium and Python that verifies the login flow on a public practice site.

## What it does

This script automates the following steps:
1. Opens the login page at `the-internet.herokuapp.com/login`
2. Enters a username and password
3. Clicks the login button
4. Waits for the page to respond
5. Asserts that the success message ("You logged into a secure area") appears

If the assertion passes, the script prints `Login test passed!` to the terminal.

## Tech stack

- Python 3
- Selenium WebDriver
- webdriver-manager (auto-manages the Chrome driver, no manual downloads needed)

## How to run it

1. Clone this repo
2. Install dependencies:
3. Run the test:


A Chrome window will open automatically, perform the login, and close. Check your terminal for `Login test passed!`.

## What I learned building this

- Locating elements with Selenium (`find_element` by ID and CSS selector)
- Handling page load timing issues using explicit waits (`WebDriverWait` + `expected_conditions`) instead of assuming the page is ready immediately
- Writing basic assertions to verify expected behavior

## Next steps

- Add negative test cases (wrong password, empty fields)
- Structure tests using pytest for cleaner test reporting
- Add screenshot capture on failure

