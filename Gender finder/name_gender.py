import pandas as pd

from nltk import NaiveBayesClassifier
from nltk.classify import accuracy

#data = pd.read_csv("name_gender.csv")
male_data = pd.read_csv("Indian-Male-Names.csv")
female_data = pd.read_csv("Indian-Female-Names.csv")

frames = [male_data, female_data]
data = pd.concat(frames)
data = data.dropna()

#print(data)
def extract_features(word, N=2):
    last_n_letters = word[-N:]
    return {'feature': last_n_letters.lower()}

train_sample = int(0.8 * len(data))
#print(train_sample)

name = input("Enter name: ")
for i in range(1,6):
    print("Number of end letters", i)
    features = [(extract_features(row["name"], i), row["gender"]) for index, row in data.iterrows()]
    train_data, test_data = features[:train_sample], features[train_sample:]
    model = NaiveBayesClassifier.train(train_data)
    acc = round(100 * accuracy(model, test_data), 2)
    print("Accuracy " + str(acc) + "%" )
    print(name, "==>", model.classify(extract_features(name, i)))
