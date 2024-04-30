from browser_setup import setup_browser, reset_browser
from game_functions import perform_algorithm
import time

def main():
    driver = setup_browser()

    try:
        perform_algorithm(driver)
    finally:
        input("Press Enter to close the browser...")
        driver.quit()

if __name__ == "__main__":
    main()
