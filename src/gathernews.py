# gathernews

import nltk
import newspaper
import webbrowser

url = ('https://polygon.com/')
pcgamer = 'https://pcgamer.com/'
theverge = 'https://theverge.com/'

sites = (url,pcgamer,theverge)
keywordarticle = list()
scrapedarticle = list()

def articlescraper(source):
    news_source = newspaper.build(source, memoize_articles=False)
    for article in news_source.articles:
        scrapedarticle.append(article)

def scraper(sources):
    collected = list()
    for source in sources:
        articlescraper(source)

scraper(sites)

keyword = input("Enter a keyword or press 'Enter':")

print('Gathering up news')

for article in scrapedarticle:
    if keyword in article.url:
        keywordarticle.append(article)

writer = open('news_summary.txt', 'w', encoding="utf-8")

for article in keywordarticle:
    try:
        article.download()
        article.parse()
    except:
        continue
        writer.write('\n' + str(article.title))
        writer.write('-')

    for author in article.authors:
        if author != article.authors[0]:
            writer.write(',')
        writer.write(str(author))

    article.nlp()
    writer.write('\n' + article.summary + '\n\n')
writer.close()
