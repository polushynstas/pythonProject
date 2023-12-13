This Python script is a web scraper designed to extract job listings from the Work.ua website. It utilizes the BeautifulSoup, Requests, and Pandas libraries to gather information and store it in a CSV file.

## Features

- **URL_TEMPLATE:** The script is configured to scrape job listings from a specific page on Work.ua (https://www.work.ua/ru/jobs-odesa/?page=2). You can customize the URL by modifying the `URL_TEMPLATE` variable.

- **FILE_NAME:** The extracted data is saved to a CSV file named "test.csv." You can change the file name by modifying the `FILE_NAME` variable.

- **parse():** The main function of the script, `parse()`, sends a GET request to the specified URL, extracts job titles, links, and descriptions using BeautifulSoup, and organizes the data into a dictionary.

- **DataFrame:** The extracted data is then converted into a Pandas DataFrame for easy manipulation and analysis.

## Libraries Used

- **BeautifulSoup4:** A Python library for pulling data out of HTML and XML files. It is used to navigate and search the HTML content of the Work.ua pages.

- **Requests:** A simple HTTP library for making web requests. It is used to retrieve the HTML content of the Work.ua pages.

- **Pandas:** A powerful data manipulation and analysis library. It is used to create a DataFrame and save the extracted data to a CSV file.
## Usage

1. Install the required libraries using the following command:pip install beautifulsoup4 requests pandas

2. Run the script to perform web scraping and generate the CSV file: main.py

3. The extracted data will be saved in the specified CSV file.