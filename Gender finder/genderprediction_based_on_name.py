import random

from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names

#print(names)
def extract_features(word, N = 2):
    last_n_letters = word[-N:]
    return {'feature': last_n_letters.lower()}

#print(type(names))
male_list = [(name, 'male') for name in names.words('male.txt')]
female_list = [(name, 'female') for name in names.words('female.txt')]
data = (male_list + female_list)

#print(data)
random.seed(5)
random.shuffle(data)

namesInput = input("Enter name: ")
train_sample = int(0.8 * len(data))
print(train_sample)
for i in range(1, 6):
    print('\nNumber of end letters:', i)
    features = [(extract_features(n, i), gender) for (n, gender) in data]
    print(features)
    train_data, test_data = features[:train_sample],features[train_sample:]
    classifier = NaiveBayesClassifier.train(train_data)
    accuracy_classifier = round(100 * nltk_accuracy(classifier, test_data), 2)
    print('Accuracy = ' + str(accuracy_classifier) + '%')
    print(namesInput, '==>', classifier.classify(extract_features(namesInput, i)))
