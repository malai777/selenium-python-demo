from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")

# Leave username and password empty - just click submit
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "flash"))
)

assert "Your username is invalid!" in driver.page_source
print("Empty fields test passed!")

driver.quit()