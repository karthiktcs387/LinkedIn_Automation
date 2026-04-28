from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# open browser in incognito
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/login")

wait = WebDriverWait(driver, 20)

try:
    # enter username
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.clear()
    username.send_keys("your_email_here")

    # enter password
    password = driver.find_element(By.ID, "password")
    password.clear()
    password.send_keys("your_password_here")

    # click login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # wait for feed page
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'feed')]")))
    print("Login Successful")

    # scroll down to load posts
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # wait for posts to load
    time.sleep(3)

    # get posts
    posts = driver.find_elements(By.XPATH, "//div[contains(@class,'feed-shared-update-v2')]")

    # print top 5 posts
    for i in range(min(5, len(posts))):
        print(f"\n--- Post {i+1} ---")
        print(posts[i].text[:300])

except Exception as e:
    print("Error:", e)
    driver.save_screenshot("error.png")

# keep browser open
input("Press Enter to close...")
driver.quit()