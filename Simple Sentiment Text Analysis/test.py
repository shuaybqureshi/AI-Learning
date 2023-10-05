from textblob import TextBlob

with open('mytext.txt','r') as f: 
    text = f.read()
blob = TextBlob(text)
print(blob.sentiment.polarity)