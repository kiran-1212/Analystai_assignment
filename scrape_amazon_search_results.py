from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import re

# Function to scrape Amazon search results
def scrape_amazon_search_results(url, num_pages):
    all_products = []

    # Create an Edge browser instance
    browser = webdriver.Edge()

    for page in range(1, num_pages + 1):
        # Construct the URL for each page of search results
        page_url = f"{url}&page={page}"

        # Load the page in the browser
        browser.get(page_url)

        # Wait for product elements to be present
        try:
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.s-result-item'))
            )
        except Exception as e:
            print(f"Failed to retrieve data from page {page} - {str(e)}")
            continue

        # Extract product information using Selenium
        product_elements = browser.find_elements(By.CSS_SELECTOR, '.s-result-item')
        
        for product_element in product_elements:
            product_info = {}
            
            try:
                # Extract product name, price, rating, and review count
                product_name_element = product_element.find_element(By.CSS_SELECTOR, '.a-text-normal')
                product_info['Product Name'] = product_name_element.text
                product_info['Product Price'] = product_element.find_element(By.CSS_SELECTOR, '.a-offscreen').text
                product_info['Rating'] = product_element.find_element(By.CSS_SELECTOR, '.a-icon-alt').get_attribute('innerHTML')
                product_info['Number of Reviews'] = product_element.find_element(By.CSS_SELECTOR, '.a-size-base').text
                
                # Extract product URL correctly using regular expressions
                product_url_element = product_element.find_element(By.CSS_SELECTOR, '.a-link-normal')
                product_url = product_url_element.get_attribute('href')
                # Check if the URL starts with 'https://www.amazon.in'
                if not re.match(r'^https://www.amazon.in', product_url):
                    product_url = 'https://www.amazon.in' + product_url
                product_info['Product URL'] = product_url

                all_products.append(product_info)
            except Exception as e:
                print(f"Failed to retrieve data from page {page} - {str(e)}")

    # Close the browser
    browser.quit()

    return all_products

# Example usage
if __name__ == "__main__":
    amazon_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
    num_pages_to_scrape = 2  # Change this to scrape more pages

    scraped_data = scrape_amazon_search_results(amazon_url, num_pages_to_scrape)

    # Save the data to a CSV file
    with open('amazon_products.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Product Name', 'Product Price', 'Rating', 'Number of Reviews', 'Product URL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in scraped_data:
            writer.writerow(product)

    print("Scraping and data saving completed.")
