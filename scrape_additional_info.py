from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Function to scrape additional product information
def scrape_additional_info(product_urls):
    product_details = []

    # Create an Edge browser instance
    browser = webdriver.Edge()

    for url in product_urls:
        product_info = {}

        # Load the product page in the browser
        browser.get(url)

        # Give the page some time to load (you can adjust this delay)
        time.sleep(3)

        try:
            # Extract additional product information
            product_info['Product URL'] = url
            product_info['Description'] = browser.find_element(By.ID, 'productDescription').text
            product_info['ASIN'] = browser.find_element(By.CSS_SELECTOR, 'th:contains("ASIN") + td').text
            product_info['Manufacturer'] = browser.find_element(By.CSS_SELECTOR, 'th:contains("Manufacturer") + td').text

            product_details.append(product_info)
        except Exception as e:
            print(f"Failed to retrieve data from URL {url} - {str(e)}")
            continue

    # Close the browser
    browser.quit()

    return product_details

# Example usage
if __name__ == "__main__":
    # Load the list of product URLs from a CSV file (replace with your own file)
    with open('amazon_products.csv', mode='r', newline='', encoding='utf-8') as csv_file:
        product_urls = [row['Product URL'] for row in csv.DictReader(csv_file)]

    product_details = scrape_additional_info(product_urls)

    # Save the additional data to a CSV file
    with open('amazon_product_details.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Product URL', 'Description', 'ASIN', 'Manufacturer']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in product_details:
            writer.writerow(product)

    print("Scraping of additional information completed.")
