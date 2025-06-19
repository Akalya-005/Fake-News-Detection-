import tkinter as tk
from tkinter import messagebox
import joblib

# Load the model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to predict news
def predict_news():
    input_text = text_entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    transformed_text = vectorizer.transform([input_text])
    prediction = model.predict(transformed_text)[0]

    if prediction == 'FAKE':
        result_label.config(text="🚨 Prediction: FAKE News", fg="red")
    else:
        result_label.config(text="✅ Prediction: REAL News", fg="green")

# Build GUI
root = tk.Tk()
root.title("📰 Fake News Detector")
root.geometry("500x400")
root.configure(bg="#f5f5f5")

title = tk.Label(root, text="Fake News Detector", font=("Helvetica", 18, "bold"), bg="#f5f5f5")
title.pack(pady=10)

text_entry = tk.Text(root, height=10, width=55, font=("Arial", 11))
text_entry.pack(pady=10)

predict_btn = tk.Button(root, text="Check News", command=predict_news, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="raised")
predict_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5f5")
result_label.pack(pady=10)

root.mainloop()
