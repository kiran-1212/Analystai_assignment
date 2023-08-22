# Web Scraping Assignment

This assignment involves scraping product information from Amazon's website. The assignment is divided into two parts:

## Part 1: Scrape Amazon Search Results

### Description
In Part 1, we scrape Amazon search results for bags. We aim to collect data on various products, including their names, prices, ratings, number of reviews, and product URLs.

### Implementation
We utilize Selenium, a web scraping tool, to navigate through Amazon's search results pages. The data is extracted from each product listing using XPath and CSS selectors.

### Code
- The Part 1 code is available in the `scrape_amazon_search_results` directory.
- `scrape_amazon_search_results.py` contains the script to scrape search results.
- The scraped data is saved in a CSV file named `amazon_products.csv`.

### Usage
- Run the `scrape_amazon_search_results.py` script to collect Amazon search results data.
- Specify the Amazon search URL and the number of pages to scrape.

## Part 2: Scrape Additional Product Information

### Description
In Part 2, we utilize the product URLs obtained in Part 1 to scrape additional information about each product. We aim to collect data such as product descriptions, ASINs, manufacturer details, and more.

### Implementation
We again use Selenium to visit each product's URL and extract the desired information from the product pages.

### Code
- The Part 2 code is available in the `scrape_additional_info` directory.
- `scrape_additional_info.py` contains the script to scrape additional product information.
- The scraped data is saved in a CSV file named `amazon_product_details.csv`.

### Usage
- Run the `scrape_additional_info.py` script to collect additional product information.
- The script reads product URLs from the `amazon_products.csv` file obtained in Part 1.

Feel free to reach out if you have any questions or encounter issues during the assignment.

Happy web scraping!
