import random
import nltk
from nltk.corpus import brown
 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC

# List of input-output pairs

def modleA(dataset,user_input):
# Split the data into inputs and outputs
 inputs, outputs = zip(*dataset)

# Create a CountVectorizer to convert the input text into numerical feature vectors
 vectorizer = CountVectorizer()
 X = vectorizer.fit_transform(inputs)

# Create a LinearSVC classifier and train it using the input feature vectors
 model = LinearSVC()
 model.fit(X, outputs)

# Test the chatbot
 input_features = vectorizer.transform([user_input])
 prediction = model.predict(input_features)[0]
 return prediction
data = [("Hi, how are you?", "I'm doing well, thanks for asking"),
        ("What do you do?", "I'm a chatbot"),
        ("What's your favorite color?", "I don't have a favorite color")]

def modleM(dataset,user_input,no_data_found= "no data found"):
    if user_input in dataset:
     chat =dataset[user_input]
     return chat
    elif user_input not in dataset:
       return(no_data_found)
