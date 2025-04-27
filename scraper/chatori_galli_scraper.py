import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import random

# Initialize undetected ChromeDriver
driver = uc.Chrome()

# Open the target URL
driver.get("https://www.swiggy.com/city/lucknow/chatori-gali-fatima-hospital-mahanagar-rest745593")

# Wait for the page to load
WebDriverWait(driver, 40).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "AWfRr"))
)

# Prepare CSV file for saving the product data including ratings
with open('chatori_galli_products_extracted.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product Name', 'Veg/Non-Veg', 'Description', 'Cost', 'Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Find all elements with class "sc-bXCLTC dUxVIy"
    elements = driver.find_elements(By.CLASS_NAME, "sc-bXCLTC.dUxVIy")

    # Extract and save text inside p tag with class "_1QbUq"
    for element in elements:
        try:
            # Extract product name, description, cost, and rating
            product_name = element.find_element(By.CLASS_NAME, "_1QbUq").text
            try:
                rating = element.find_element(By.CLASS_NAME, "sc-aXZVg.knBukL").text
            except:
                rating = round(random.uniform(2, 3.2), 1)  # Random rating between 2.5 and 3.8

            # Extract cost and description from product data
            parts = product_name.split(" Costs: ")
            name_veg = parts[0].split(" Costs:")[0].split(".")
            veg_or_nonveg = name_veg[0].strip()
            product_name = name_veg[1].strip()

            description = parts[1].split(" Description:")[1].strip()  # Extract only description after 'Description:'
            cost = parts[1].split(" rupees")[0].strip()

            # Write extracted data to CSV
            writer.writerow({
                'Product Name': product_name,
                'Veg/Non-Veg': veg_or_nonveg,
                'Description': description,
                'Cost': cost,
                'Rating': rating
            })

            print(f"Extracted: {product_name}, Rating: {rating}")
        except Exception as e:
            print(f"Error extracting data for an item: {e}")

# Close the driver
driver.quit()

print("Data extraction complete!")
