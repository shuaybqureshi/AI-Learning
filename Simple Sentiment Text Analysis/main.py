#

from textblob import TextBlob
from newspaper import Article

url = 'https://www.benzinga.com/news/earnings/23/10/35089526/us-stocks-rise-following-adp-data-dow-rises-over-50-points/'

article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.text

blob = TextBlob(text)
sentiment = blob.sentiment.polarity 
print(sentiment)