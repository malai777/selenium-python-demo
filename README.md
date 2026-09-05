# Selenium Login Automation Test

A set of automated tests built with Selenium and Python that verify the login flow on a public practice site, covering both valid and invalid login scenarios.

## What it does

**test_login.py** — Positive test:
1. Opens the login page at `the-internet.herokuapp.com/login`
2. Enters a valid username and password
3. Clicks the login button
4. Waits for the page to respond
5. Asserts that the success message ("You logged into a secure area") appears

**test_login_negative.py** — Negative test (wrong password):
1. Enters a valid username with an incorrect password
2. Asserts the correct error message ("Your password is invalid!") appears

**test_login_empty.py** — Negative test (empty fields):
1. Submits the login form with both fields empty
2. Asserts the correct error message ("Your username is invalid!") appears

## Tech stack

- Python 3
- Selenium WebDriver
- webdriver-manager (auto-manages the Chrome driver, no manual downloads needed)

## How to run it

1. Clone this repo
2. Install dependencies:
pip3 install selenium webdriver-manager pytest

3. Run any test:

python3 test_login.py
python3 test_login_negative.py
python3 test_login_empty.py


Each script opens a Chrome window automatically, performs the actions, and closes it.

## Sample output
Login test passed!
Wrong password test passed!
Empty fields test passed!


## What I learned building this

- Locating elements with Selenium (`find_element` by ID and CSS selector)
- Handling page load timing issues using explicit waits (`WebDriverWait` + `expected_conditions`) instead of assuming the page is ready immediately
- Writing both positive and negative test cases to verify expected and error behavior
- Debugging real issues: environment setup (pip/PATH on macOS), script formatting, and assertion failures caused by timing

## Next steps

- Structure all three tests using pytest for cleaner test reporting
- Add screenshot capture on failure
- Set up GitHub Actions to run tests automatically on every push