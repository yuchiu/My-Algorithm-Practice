
import numpy as np  # pylint: disable=E0401
import pandas as pd  # pylint: disable=E0401
from sklearn.model_selection import train_test_split  # pylint: disable=E0401
from sklearn.naive_bayes import MultinomialNB  # pylint: disable=E0401
from sklearn.feature_extraction.text import TfidfVectorizer  # pylint: disable=E0401

# data source https://archive.ics.uci.edu/ml/machine-learning-databases/00228/


def load_csv():
    # read data and transform into format of index, status, message
    data_frame = pd.read_csv('spamCollection', sep='\t',
                             names=['Status', 'Message'])
    # 5572 emails, 4825 ham, 747 spam
    print("total : "+str(len(data_frame)))
    data_frame.loc[data_frame["Status"] == 'ham', "Status", ] = 1
    print("ham: "+str(len(data_frame[data_frame.Status == 1])))
    data_frame.loc[data_frame["Status"] == 'spam', "Status", ] = 0
    print("spam: "+str(len(data_frame[data_frame.Status == 0])))
    return data_frame


def classify_email():
    data_frame = load_csv()
    data_frame_x = data_frame["Message"]
    data_frame_y = data_frame["Status"]
    # split data into training dataset and testing dataset into x and y
    x_train, x_test, y_train, y_test = train_test_split(
        data_frame_x, data_frame_y, test_size=0.2, random_state=4)

    # vectorize emails message both training dataset and testing dataset using tfidf vectorizer
    vectorizer = TfidfVectorizer(min_df=1, stop_words='english')
    x_train_vectorized = vectorizer.fit_transform(x_train)
    x_test_vectorized = vectorizer.transform(x_test)

    y_train = y_train.astype('int')

    # using multinomial Naive Bayes classifier
    NB_classifier = MultinomialNB()
    NB_classifier.fit(x_train_vectorized, y_train)

    predictions = NB_classifier.predict(x_test_vectorized)
    print("predictions result: "+str(predictions))
    actual = np.array(y_test)
    print("actual result: "+str(actual))

    # check if prediction matches actual value
    corrent_count = 0
    for i in range(len(predictions)):
        # if prediction value equal actual value, increase corrent_count by 1
        if predictions[i] == actual[i]:
            corrent_count = corrent_count+1
    accuracy = corrent_count/len(predictions)
    print("predicted: "+str((len(predictions))) +
          " email messages, correct count: "+str(corrent_count))
    print("accuracy: "+str(accuracy))


def run():
    try:
        classify_email()
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    run()
