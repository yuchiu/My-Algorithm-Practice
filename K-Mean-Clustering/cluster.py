
import sys
import os
from os.path import join, dirname
from dateutil import parser  # pylint: disable=E0401
from pymongo import MongoClient  # pylint: disable=E0401
from sklearn.feature_extraction.text import TfidfVectorizer  # pylint: disable=E0401
from sklearn.cluster import KMeans  # pylint: disable=E0401
from sklearn.metrics import adjusted_rand_score  # pylint: disable=E0401
import json


def load_json_multiple(segments):
    chunk = ""
    for segment in segments:
        chunk += segment
        try:
            yield json.loads(chunk)
            chunk = ""
        except ValueError:
            pass


def cluster_news():
    news_article = []
    with open('news.json') as f:
        for all_news in load_json_multiple(f):
            news_article.append(all_news['text'])

    # vectorize news article using tfidf vectorizer
    tfidfVectorizer = TfidfVectorizer()
    X = tfidfVectorizer.fit_transform(news_article)

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(news_article)
    true_k = 10
    model = KMeans(n_clusters=true_k, init='k-means++',
                   max_iter=100, n_init=1)
    model.fit(X)
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print ("Cluster %d:" % i),
        for ind in order_centroids[i, :10]:
            print (' %s' % terms[ind]),

    print("clustered "+str(len(news_article))+" of news articles.")


def run():
    try:
        cluster_news()
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    run()
