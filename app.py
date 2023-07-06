import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def scrape_website():
    # Scrape BBC Technology
    bbc_response = requests.get("https://www.bbc.com/news/technology")
    bbc_html = bbc_response.text
    bbc_soup = BeautifulSoup(bbc_html, 'html.parser')
    bbc_links = bbc_soup.select(".gs-c-promo-heading")
    bbc_titles_and_urls = [(link.text, "https://www.bbc.com" + link.attrs['href']) for link in bbc_links[:10]]

    # Scrape USA Today Tech
    usa_today_response = requests.get("https://www.usatoday.com/tech/")
    usa_today_html = usa_today_response.text
    usa_today_soup = BeautifulSoup(usa_today_html, 'html.parser')
    usa_today_links = usa_today_soup.select(".gnt_m_tl")
    usa_today_titles_and_urls = [(link.text, link.attrs['href']) for link in usa_today_links[:10]]

    # Scrape VentureBeat
    venturebeat_response = requests.get("https://venturebeat.com/")
    venturebeat_html = venturebeat_response.text
    venturebeat_soup = BeautifulSoup(venturebeat_html, 'html.parser')
    venturebeat_links = venturebeat_soup.select(".ArticleListing__title-link")
    venturebeat_titles_and_urls = [(link.text, link.attrs['href']) for link in venturebeat_links[:10]]

    return render_template('index.html',
                           bbc_titles_and_urls=bbc_titles_and_urls,
                           usa_today_titles_and_urls=usa_today_titles_and_urls,
                           venturebeat_titles_and_urls=venturebeat_titles_and_urls)

if __name__ == '__main__':
    app.run()
