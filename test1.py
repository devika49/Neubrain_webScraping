from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up the Selenium driver (ensure you have the correct chromedriver installed)
driver = webdriver.Chrome()

url = "https://eprplastic.cpcb.gov.in/#/plastic/home/main_dashboard"
driver.get(url)

try:
    # Wait until the dropdown for entries per page is clickable
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//ng-select[@name='example_length']"))  # Corrected to use ng-select
    )

    # Use Select class to select "100" entries per page
    dropdown = Select(driver.find_element(By.XPATH, "//ng-select[@name='example_length']"))
    dropdown.select_by_visible_text("100")  # Selects "100" from the dropdown

    # Wait for the table to refresh after selecting entries
    time.sleep(3)

    # Click the "Table" button in the button group
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-group')]//button[text()='Table']"))  # Adjusted XPath to target the correct button
    ).click()

    # Wait for the table to load
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-view.pt-3"))
    )

    # Locate the table with the correct CSS selector
    table = driver.find_element(By.CSS_SELECTOR, ".table-view.pt-3")
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip the header row

    # Extract data
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) == 7:
            data.append({
                "Date of Application": cols[0].text,
                "Legal Name": cols[1].text,
                "Trade Name": cols[2].text,
                "App. No.": cols[3].text,
                "Registration Number": cols[4].text,
                "Type of PIBO": cols[5].text,
                "Application Status": cols[6].text
            })

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to Excel
    df.to_excel("pibo_registration_status.xlsx", index=False)
    print("Data has been saved to pibo_registration_status.xlsx")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()
