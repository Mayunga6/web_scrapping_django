# Football Statistics Scraper

## Overview

This web application scrapes football websites to obtain detailed information about:
- The home form for the home team
- The away form for the away team
- Head-to-head statistics
- Player statistics

Additionally, the application scrapes predictions from the Forebet website. Despite running without errors, the application currently displays "no results found" under all the outputs. Further research is needed to identify and resolve the issue.

## Features

- **Home Form**: Retrieves the performance data of the home team in their home matches.
- **Away Form**: Gathers performance data of the away team in their away matches.
- **Head-to-Head Statistics**: Provides historical match data between the two teams.
- **Player Statistics**: Compiles individual player performance metrics.
- **Predictions**: Scrapes match predictions from the Forebet website.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/web_scrapping_django.git
   cd soccer_stats

2. set up the environment
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   
3. Install the required dependencies:
   pip install -r requirements.txt

4. Set up environment variables:
   Create a .env file in the project root directory and add the following:
   SECRET_KEY=your_secret_key_here

## Usage
Run the application:
python manage.py runserver
Access the web application at http://127.0.0.1:8000.

## Troubleshooting
No Results Found
If the application shows "no results found" under all outputs, consider the following steps:

1. **Check Website Structure**: Verify that the HTML structure of the websites being scraped has not changed. Use browser   
   Developer Tools to inspect the current structure.
2. **Update Selectors**: Ensure your CSS selectors or XPath expressions match the current HTML structure.
3. **Handle Dynamic Content**: Use tools like Selenium for pages that load content dynamically with JavaScript.
4. **Add Logging**: Implement logging to print intermediate results and identify where the scraping process fails.
5. **Error Handling**: Use try-except blocks to catch and log exceptions during scraping.
6. **Check User-Agent**: Ensure your requests include a proper User-Agent header to avoid being blocked by the websites.
7. **Verify URL Patterns**: Ensure the URLs you are scraping are correct and follow expected patterns.
8. **Test in Isolation**: Test each part of your scraping code separately to ensure each component works correctly.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
   
