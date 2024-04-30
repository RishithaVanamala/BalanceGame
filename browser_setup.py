from selenium import webdriver

def setup_browser():
    # Initialize the ChromeDriver
    driver = webdriver.Chrome()

    # Open the website and maximize the window
    driver.get("http://sdetchallenge.fetch.com/")
    driver.maximize_window()

    return driver

def reset_browser(driver):
    try:
        # Execute JavaScript to get the second reset button element
        reset_button = driver.execute_script("return document.querySelectorAll('button#reset')[1];")
        # Simulate a click event
        driver.execute_script("arguments[0].click();", reset_button)
        print("Second reset button clicked successfully")
    except Exception as e:
        print(f"An error occurred while clicking the reset button: {e}")
