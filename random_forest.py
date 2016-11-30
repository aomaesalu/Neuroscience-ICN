#!/usr/bin/env python2.7
# -*- coding: utf8 -*-i

from argparse import ArgumentParser
from lib.io import read_data
from lib.string import format_path
from lib.cross_validation import construct_data_sets
from lib.score import ConfusionMatrix, Score
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier


def run(data_path, cv_amount):

    # Read input data
    data = []
    for i in range(cv_amount):
        data.append(read_data(format_path(data_path, i + 1)))

    # Iterate through all of the data sets, using each of them for test data
    # exactly once, and using all others as training data sets at the same
    for test_index in range(cv_amount):

        # Construct training and test data sets
        train_data, test_data = construct_data_sets(data, cv_amount, test_index)

        # Classification
        model = RandomForestClassifier(n_estimators=500)#, max_features=10, max_leaf_nodes=15, max_depth=5)
        model.fit(train_data['neural_responses'], train_data['image_category'])

        # Prediction
        prediction = model.predict(test_data['neural_responses'])

        # Scoring
        confusion_matrix = ConfusionMatrix(test_data['image_category'],
                                           prediction)
        print(confusion_matrix)
        score = Score(test_data['image_category'], prediction)
        print(score)

if __name__ == '__main__':

    # Parse command line arguments
    PARSER = ArgumentParser()
    PARSER.add_argument('data_path', help='the pickled data file path')
    PARSER.add_argument('cv_amount', help='the amount of equal sized data ' +
                        'sets created upon partitioning the data', type=int)
    ARGUMENTS = PARSER.parse_args()

    # Run the data classification script
    run(ARGUMENTS.data_path, ARGUMENTS.cv_amount)
