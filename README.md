# Fake Gold Bar Finder

This project automates the process of identifying a fake gold bar using a balance scale and a set of 9 bars, where one is fake and weighs less.

## How to Run

1. **Setup:**

   Ensure you have Python and the necessary packages installed:

   ```bash
   pip install selenium webdriver_manager

2. **Run** **The** **Script:**
   python3 main.py
3. **Observing** **the** **Results:**
  Weighs groups of bars to identify the fake one.
  Clicks on the suspected fake bar and checks for an alert.
  Outputs the alert message and results to the console.
  After the final alert, the browser will stay open for review, requiring manual dismissal by pressing "Enter".


## Code Structure:

The project consists of three main files:
main.py: Runs the program, initializing the browser and calling necessary functions.
browser_setup.py: Contains functions for setting up and managing the browser.
game_functions.py: Contains functions for weighing bars, retrieving results, and selecting the fake bar.
