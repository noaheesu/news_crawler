# News Crawling Project

This project is a web scraping application that crawls multiple news websites and extracts the titles and URLs of articles related to technology. It was created with the purpose of aggregating technology news from various sources into a single platform for easy access and reference.

## Purpose

The purpose of this project is to provide a convenient way to stay updated with the latest technology news. By crawling multiple news websites, the application gathers articles specifically related to technology and presents them in a unified format. This allows users to browse through the headlines and quickly access the full articles by clicking on the provided URLs.

## Tools and Technologies Used

- **Python**: The project is implemented in Python, a versatile programming language commonly used for web scraping tasks.
- **Flask**: Flask is a lightweight web framework used to develop the application. It provides routing capabilities and serves the scraped data to users via HTTP.
- **requests**: The `requests` library is used to make HTTP requests to the target websites and retrieve their HTML content.
- **BeautifulSoup**: BeautifulSoup is a powerful library for parsing HTML and extracting data. It is utilized in this project to extract the titles and URLs of the news articles from the HTML documents.
- **HTML and CSS**: The application uses HTML templates to render the scraped data and CSS for basic styling.

## Project Structure

The project consists of the following files:

- `main.py`: The main Python script that contains the Flask application and the web scraping logic.
- `templates/index.html`: The HTML template file that renders the scraped titles and URLs.
- `styles.css`: The CSS file for styling the HTML template.

## Installation

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/news-crawling-project.git`
2. Navigate to the project directory: `cd news-crawling-project`
3. Install the required Python packages: `pip install -r requirements.txt`
