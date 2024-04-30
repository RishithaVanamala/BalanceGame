from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time
from browser_setup import reset_browser

def input_number(driver, bowl, cell_index, number):
    # Insert number in the specified cell of the bowl's grid
    input_id = f"{bowl}_{cell_index}"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, input_id))).clear()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, input_id))).send_keys(str(number))

def click_weigh_button(driver):
    # Press the "Weigh" button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "weigh"))).click()

def get_result(driver):
    # Get the result of weighing from the list within 'game-info'
    weighings = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".game-info ol li"))
    )
    return weighings[-1].text.strip() if weighings else ""

def get_result_second(driver):
    # Get the second weighing result
    game_info = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'game-info'))
    )
    ol_element = game_info.find_element(By.TAG_NAME, 'ol')
    second_li = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.game-info ol li:nth-child(2)'))
    )
    return second_li.text

def click_gold_bar_number(driver, number):
    # Click on the suspected fake bar
    try:
        suspected_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, f"coin_{number}"))
        )
        suspected_button.click()

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert: {alert_text}")

            # Manual review before dismissal
            input("Press Enter to dismiss the alert...")

            alert.accept()

            assert "Yay!" in alert_text, "Failed to find the fake bar"
        except NoAlertPresentException:
            print(f"No alert after clicking bar {number}")
    except Exception as e:
        print(f"Error clicking bar {number}: {e}")

def perform_algorithm(driver):
    groups = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]

    # Weigh the first two groups
    for i in range(3):
        input_number(driver, 'left', i, groups[0][i])
        input_number(driver, 'right', i, groups[1][i])
    click_weigh_button(driver)
    
    result = get_result(driver)
    print(f"First Weighing Result: {result}")
    reset_browser(driver)

    if "=" not in result:
        fake_group = groups[0] if "<" in result else groups[1]
    else:
        fake_group = groups[2]
    
    # Weigh two bars from the fake group
    input_number(driver, 'left', 0, fake_group[0])
    input_number(driver, 'right', 0, fake_group[1])
    click_weigh_button(driver)
    
    second_result = get_result_second(driver)
    print(f"Second Weighing Result: {second_result}")
    reset_browser(driver)

    if "=" in second_result:
        fake_bar = fake_group[2]
    else:
        fake_bar = fake_group[0] if "<" in second_result else fake_group[1]

    # Click on the fake bar and handle the alert
    click_gold_bar_number(driver, fake_bar)
