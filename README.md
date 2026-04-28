# LinkedIn Automation using Selenium

##  Project Overview
This project automates LinkedIn using Selenium WebDriver in Python.

It performs:
- Opens LinkedIn
- Logs into account
- Navigates to feed
- Scrolls the page
- Extracts top posts

---

##  Tech Stack
- Python
- Selenium WebDriver
- ChromeDriver

---

##  Requirements

Install dependencies:
```bash
pip install selenium

Download ChromeDriver matching your Chrome version:
https://googlechromelabs.github.io/chrome-for-testing/

 Project Structure
LinkedIn_Automation/
│── script.py
│── chromedriver.exe
│── error.png (if any error occurs)
 How to Run
Open terminal in project folder
Run:
python script.py
Script will:
Open Chrome
Login to LinkedIn
Fetch posts
Print posts in terminal
 Sample Code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup ChromeDriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open LinkedIn
driver.get("https://www.linkedin.com/login")

# Wait for login (manual or automated)
time.sleep(20)

# Go to feed
driver.get("https://www.linkedin.com/feed/")
time.sleep(5)

# Scroll
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Get posts
posts = driver.find_elements(By.XPATH, "//div[contains(@class,'feed-shared-update-v2')]")

# Print posts
for i in range(min(5, len(posts))):
    print(f"\n--- Post {i+1} ---")
    print(posts[i].text[:300])

input("Press Enter to close...")
driver.quit()
