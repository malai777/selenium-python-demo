from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "flash"))
)

assert "Your password is invalid!" in driver.page_source
print("Wrong password test passed!")

driver.quit()