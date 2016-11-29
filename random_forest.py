#!/usr/bin/env python2.7
# -*- coding: utf8 -*-i

from argparse import ArgumentParser
from lib.io import read_data
from lib.score import Score
from sklearn.ensemble import RandomForestClassifier


def run(train_path, test_path):

    # Read input data
    train_data = read_data(train_path)
    test_data = read_data(test_path)

    # Classification
    model = RandomForestClassifier(n_estimators=1000)
    model.fit(train_data['neural_responses'], train_data['image_category'])

    # Prediction
    prediction = model.predict(test_data['neural_responses'])

    # Scoring
    score = Score(test_data['image_category'], prediction)
    print(score)

if __name__ == '__main__':

    # Parse command line arguments
    PARSER = ArgumentParser()
    PARSER.add_argument('train_path', help='the pickled input training data \
                                            file path')
    PARSER.add_argument('test_path', help='the pickled input testing data \
                                           file path')
    ARGUMENTS = PARSER.parse_args()

    # Run the data classification script
    run(ARGUMENTS.train_path, ARGUMENTS.test_path)
