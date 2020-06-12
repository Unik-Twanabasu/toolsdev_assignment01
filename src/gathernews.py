# gathernews

import nltk
import newspaper

keyword = input("Enter a keyword or press 'Enter':")

polygon = newspaper.build('http://polygon.com')

pcgamer = newspaper.build('http://pcgamer.com')

theverge = newspaper.build('http://theverge.com')


def articlekeyword(keyword, Article):
    try:
        Article.download()
        Article.parse()
        Article.nlp()
    except:
        return False
        if keyword in Article.keywords: return True
        return False


def articleScraper(keyword, articles, myArticles):
    tempSummaries = ""
    for Article in articles:
        if keyword == "" or articlekeyword(keyword, Article):
            try:
                myArticles.append(Article)
                Article.download()
                Article.parse()
            except:
                continue
                tempSummaries += Article.title
                tempSummaries += "-"
                tempSummaries += ",".join(Article.authors)
                Article.nlp()
                tempSummaries += "\n"
                tempSummaries += Article.summary
                tempSummaries += "\n\n"
            return tempSummaries


myArticles = []
summaries = ""
summaries += articleScraper(keyword, polygon.articles[:10], myArticles)
summaries += articleScraper(keyword, pcgamer.articles[:10], myArticles)
summaries += articleScraper(keyword, theverge.articles[:10], myArticles)

summaries = summaries.encode("ascii", "ignore").decode()
with open("news_summary.txt", "w")as f:
    f.write(summaries)

print("sourced form:")
print("Polygon")
print("PCGamer")
print("TheVerge")
