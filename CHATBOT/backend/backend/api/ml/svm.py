from sklearn.svm import SVC
import numpy as np
import pandas as pd


class SVM:
    """
    Fits a SVM model using ALL the given data in train_dataset_name
    """
    def __init__(self, train_dataset_name, test_dataset_name):

        # Save set of possible symptoms
        self.symptom_set = pd.read_csv(train_dataset_name).columns[:-1].values.tolist() #Exclude last col, prognosis col

        svm = SVC(probability=True)

        # Create model from training data
        train_dataset = pd.read_csv(train_dataset_name)
        X_train = train_dataset.iloc[:, :-1].values
        # print(X_train)
        Y_train = train_dataset.iloc[:, -1].values
        self.model = svm.fit(X_train, Y_train)

        # Get test accuarcy
        test_dataset = pd.read_csv(test_dataset_name)
        X_test = test_dataset.iloc[:, :-1].values
        Y_test = test_dataset.iloc[:, -1].values
        self.score = svm.score(X_test, Y_test)

    """
    Return a dictionary of disease to likelihoods given a list of symptoms
    """
    def get_predictions(self, symptoms):
        X = self.format_symptoms(symptoms) #Uses helper to properly form symptoms
        classes = self.model.classes_ #Possible diseases
        probabilities = self.model.predict_proba([X])
        return dict(zip(classes, probabilities[0])) #gets vector of probabilities for each class (disease)

    """
    Returns one prediction for a disease given a list of symptoms
    """
    def get_prediction(self, symptoms):
        X = self.format_symptoms(symptoms) #Uses helper to properly form symptoms
        # print(X)
        print(self.model.predict([X]))
        return self.model.predict([X])

    """
    HELPER function to convert a list of symptoms (any order) to properly formed input vector X (containing one hot encoding of symptoms)
    """
    def format_symptoms(self, symptoms):
        symptom_index = dict(zip(self.symptom_set, range(len(self.symptom_set)))) #Convert list to (word -> index) dict

        X = np.zeros(len(self.symptom_set))
        for symptom in symptoms:
            if symptom in symptom_index:
                X[symptom_index[symptom]] = 1
        return X

    """
    Get the accuarcy of the model for a given test set between 0 and 1
    The accuarcy will vary depending on the test set given
    (ie. If set is same as training set, accuarcy will be 100%)
    """
    def get_test_score(self):
        return self.score


#Testing
#svm = SVM('Training.csv','Testing.csv')
#symptoms = ['continuous_sneezing' ,'shivering' ,'chills']
#print('Test accuarcy: ' + str(svm.get_test_score()))
#print('Prediction: ' + str(svm.get_prediction(symptoms)))
#print('Prediction: ' + str(svm.get_predictions(symptoms)))