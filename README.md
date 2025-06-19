📰 Fake News Detector (with GUI)
A simple and smart desktop app that helps you detect whether a piece of news is FAKE or REAL using machine learning.

Built using:

Python 🐍

Tkinter for GUI 💻

Machine Learning (trained on real-world news data) 🤖

✅ Features
🧠 Predicts if the news is real or fake

✍️ User-friendly text input box

🎨 Simple, clean, emoji-powered UI

💡 Built-in machine learning model (99% accuracy)

🚀 How to Run the App
1. Clone or download the project:
bash
Copy
Edit
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
2. Install required libraries:
Make sure Python is installed, then:

bash
Copy
Edit
pip install -r requirements.txt
(If you don’t have a requirements.txt, just install joblib and scikit-learn.)

3. Run the app:
bash
Copy
Edit
python fake_news_gui.py
🖥️ The app will open in a new window. Paste any news text and hit Check News!

📊 Model Info
The model was trained on a dataset of real and fake news articles with 99.44% accuracy.

Class	Precision	Recall	F1-Score
FAKE	1.00	0.99	0.99
REAL	0.99	1.00	0.99

🤖 Tech Used
Python

Tkinter (for GUI)

Scikit-learn (for model)

TF-IDF Vectorizer

Joblib (for model saving/loading)