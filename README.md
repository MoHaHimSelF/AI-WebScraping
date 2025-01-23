# AI Web Scraper App with ollama3.2

This is an AI-powered web scraping application built using Streamlit + ollama. The app allows users to scrape content from a given URL, clean the scraped content, and search for specific information within the content using natural language processing.

## Features

- **Scrape Website**: Enter a URL to scrape content from the website.
- **Clean Content**: The scraped content is cleaned to remove unnecessary elements.
- **Search Content**: Describe what you want to search for in the cleaned content, and the app will find relevant information.


## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run main.py
    ```
2. Open your web browser and go to `http://localhost:8501`.
3. Enter the URL you want to scrape in the input field and click the "Scrape URL" button.
4. Once the content is scraped and cleaned, you can describe what you want to search for in the content and click the "Search" button to find relevant information.

## Files

- `main.py`: The main application file containing the Streamlit app code.
- `parse.py`: Contains the `parse_with_ollama` function for parsing content.
- `scrape.py`: Contains functions for scraping and cleaning website content.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Note

This simple AI web scraper has many limitations due to the use of the free source library SELENIUM and the main goal here is messing around with AI on my local machine for free
