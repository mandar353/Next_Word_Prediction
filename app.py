import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


from flask import Flask, render_template, request
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
with open('model_GRU.pkl', 'rb') as f:
    model = pickle.load(f)
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

app = Flask(__name__)

max_sequence_len = model.input_shape[1] + 1

def predict_next_word(seed_text):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted_probs = model.predict(token_list, verbose=0)[0]
    predicted_index = np.argmax(predicted_probs)
    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word
    return ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    seed_text = request.form['seed_text']
    next_word = predict_next_word(seed_text)
    return render_template('result.html', seed_text=seed_text, next_word=next_word)

if __name__ == '__main__':
    app.run(debug=True)
