from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

# Define your website link, username, and password`
website_link = "https://mrei.icloudems.com/corecampus/index.php"
username = "12104005N094"
password = "9560252503"

# Define the HTML element IDs for username, password, and submit button
element_for_username = "useriid"
element_for_password = "actlpass"
element_for_submit = "psslogin"

# Initialize the WebDriver using GeckoDriverManager (no need for executable_path)
browser = webdriver.Firefox()

# Open the website
browser.get(website_link)

try:
    # Find and fill the username field using the HTML element ID
    username_element = browser.find_element(By.ID, element_for_username)
    username_element.send_keys(username)

    # Find and fill the password field using the HTML element ID
    password_element = browser.find_element(By.ID, element_for_password)
    password_element.send_keys(password)

    # Introduce a delay (e.g., 3 seconds) before clicking the submit button
    time.sleep(3)

    # Find and click the submit button using the HTML element ID
    signInButton = browser.find_element(By.ID, element_for_submit)
    signInButton.click()

    # You can add further automation steps after successful login here.

except Exception as e:
    print("An error occurred:", e)

# Optionally, you can add code to wait for specific elements to load or perform further automation steps.

# To quit the browser, uncomment the following line:
# browser.quit()
