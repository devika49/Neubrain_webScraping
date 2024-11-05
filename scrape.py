from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up ChromeDriver path
driver_path = 'C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'  # Update this path if necessary
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL to the page with the table
url = "https://eprplastic.cpcb.gov.in/#/plastic/home/main_dashboard"
driver.get(url)

try:
    # Wait for the table container to load (adjust locator as needed)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "class=card-body px-0 py-1"))
    )
    
    # Optional: scroll down to load more content if necessary
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust if more time is needed for content to load

    # Locate the table and rows
    table = driver.find_element(By.CSS_SELECTOR, ".table-layer .custom-simple-table")
    rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Initialize an empty list to store data
    table_data = []

    # Loop through rows and extract data
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        table_data.append(row_data)

finally:
    # Close the driver
    driver.quit()

# Define column names based on the table structure
column_names = ["Date of Application", "Legal Name", "Trade Name", "App. No.", "Registration Number", "Type of PIBO", "Application Status"]

# Convert the data to a DataFrame
df = pd.DataFrame(table_data, columns=column_names)

# Display the DataFrame
print(df.head())
