import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

# Load dataset
df = pd.read_csv("news_dataset.csv")

# Keep only necessary columns
df = df[['text', 'label']]

# Split features and labels
X = df['text']
y = df['label']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the model
model = PassiveAggressiveClassifier(max_iter=1000)
model.fit(X_train_vec, y_train)

# Make predictions
y_pred = model.predict(X_test_vec)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {round(accuracy * 100, 2)} %")
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
with open("fake_news_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Sample test
def predict_news(news_text):
    with open("fake_news_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    vec = vectorizer.transform([news_text])
    return model.predict(vec)[0]

# Example use
sample = "NASA discovers a new planet in the solar system"
print("Prediction:", predict_news(sample))
