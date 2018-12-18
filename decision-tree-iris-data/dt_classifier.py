import numpy as pd  # pylint: disable=E0401
import pandas as pd  # pylint: disable=E0401
import tkinter  # pylint: disable=E0401
from matplotlib import pyplot as plt  # pylint: disable=E0401
from sklearn.tree import DecisionTreeClassifier  # pylint: disable=E0401
from sklearn.model_selection import train_test_split  # pylint: disable=E0401
from sklearn.metrics import confusion_matrix  # pylint: disable=E0401
from sklearn.metrics import accuracy_score  # pylint: disable=E0401


# data source http://archive.ics.uci.edu/ml/datasets/Iris
def load_csv():
    iris_data = pd.read_csv("iris.data")
    return iris_data


def dt_classifier():
    iris_data = load_csv()
    data_frame_x = iris_data[["sepal_length",
                              "sepal_width", "petal_length", "petal_width"]]
    data_frame_y = iris_data.Class
    # split data into training dataset and testing dataset into 70% training and 30% testing
    x_train, x_test, y_train, y_test = train_test_split(
        data_frame_x, data_frame_y, test_size=0.3, random_state=4)

    # build decision tree model
    model = DecisionTreeClassifier()
    fitted_model = model.fit(x_train, y_train)
    predictions = fitted_model.predict(x_test)

    print('confusion matrix: ')
    print(confusion_matrix(y_test, predictions))
    print('accuracy: {}'.format(accuracy_score(y_test, predictions)))


if __name__ == '__main__':
    dt_classifier()
