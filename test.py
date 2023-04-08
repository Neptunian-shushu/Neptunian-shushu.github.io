from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://neptunian-shushu.github.io/')

links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    href = link.get_attribute('href')
    if href:
        link.click()
        try:
            WebDriverWait(driver, 10).until(EC.title_contains(""))
            title = driver.title
            print(title)
        except NoSuchElementException:
            print(f"Link {href} does not lead to any page yet or leads to a 404 page.")
            exit(1)

driver.quit()
