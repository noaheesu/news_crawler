# import requests
# from bs4 import BeautifulSoup
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def scrape_website():
#     response = requests.get("https://www.bbc.com/news/technology")
#     html = response.text

#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup.select(".gs-c-promo-heading")
#     titles_and_urls = []

#     for link in links:
#         title = link.text
#         url = "https://www.bbc.com" + link.attrs['href']
#         titles_and_urls.append((title, url))

#     return render_template('index.html', titles_and_urls=titles_and_urls)

# if __name__ == '__main__':
#     app.run()






import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def scrape_website():
    # Scrape titles from the BBC Technology section
    bbc_response = requests.get("https://www.bbc.com/news/technology")
    bbc_html = bbc_response.text
    bbc_soup = BeautifulSoup(bbc_html, 'html.parser')
    bbc_links = bbc_soup.select(".gs-c-promo-heading")
    bbc_titles = [link.text for link in bbc_links[:10]]

    # Scrape titles from the usatoday News section
    usa_response = requests.get("https://www.usatoday.com/tech/")
    usa_html = usa_response.text
    usa_soup = BeautifulSoup(usa_html, 'html.parser')
    usa_links = usa_soup.select(".gnt_m_tl")
    usa_titles = [link.text for link in usa_links[:10]]

    # Scrape titles from the usatoday News section
    venture_response = requests.get("https://venturebeat.com/")
    venture_html = venture_response.text
    venture_soup = BeautifulSoup(venture_html, 'html.parser')
    venture_links = venture_soup.select(".ArticleListing__title-link")
    venture_titles = [link.text for link in venture_links[:10]]
    

    # Combine titles from both sources
    titles = bbc_titles + usa_titles

    # return render_template('index.html', titles=titles)
    return render_template('index.html', bbc_titles=bbc_titles, usa_titles=usa_titles, venture_titles=venture_titles)

if __name__ == '__main__':
    app.run()

