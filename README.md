# Next Word Prediction using LSTM and GRU

## Overview

This project is a Natural Language Processing (NLP) application that predicts the next word in a sequence of text using Deep Learning models. The model is trained on textual data and learns language patterns to generate accurate next-word predictions.

The project demonstrates text preprocessing, tokenization, sequence generation, deep learning model development, and prediction using LSTM and GRU neural networks.

---

## Features

* Text preprocessing and cleaning
* Tokenization and vocabulary generation
* Sequence creation for training
* Deep Learning-based prediction
* LSTM and GRU model implementation
* Real-time next word prediction
* User-friendly web interface
* Model evaluation and comparison

---

## Tech Stack

### Programming Language

* Python

### Libraries and Frameworks

* TensorFlow
* Keras
* NumPy
* Pandas
* Scikit-learn
* NLTK

### Web Framework

* Flask

### Frontend

* HTML
* CSS

---

## Project Architecture

1. Load and preprocess text dataset
2. Tokenize text and create vocabulary
3. Generate input sequences
4. Apply padding to sequences
5. Train LSTM and GRU models
6. Save trained model
7. Accept user input through web interface
8. Predict next word
9. Display prediction result

---

## Dataset

The model is trained on textual data consisting of sentences and phrases.

Preprocessing steps include:

* Lowercase conversion
* Tokenization
* Removal of unwanted characters
* Sequence generation
* Padding

---

## Model Implementation

### LSTM Model

Long Short-Term Memory (LSTM) networks are used to capture long-range dependencies in text and improve sequence prediction accuracy.

### GRU Model

Gated Recurrent Unit (GRU) networks are implemented as an alternative recurrent neural network architecture with fewer parameters and faster training.

---

## Results

The trained models successfully learn contextual relationships between words and predict the most probable next word based on the input sequence.

Example:

Input:

```text
Machine learning is
```

Output:

```text
a
```

Input:

```text
Artificial intelligence can
```

Output:

```text
help
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/mandar353/Next_Word_Prediction.git
```

### Navigate to Project Directory

```bash
cd Next_Word_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Project Structure

```text
Next_Word_Prediction/
│
├── app.py
├── model/
├── templates/
├── static/
├── dataset/
├── requirements.txt
├── README.md
└── saved_model/
```

---

## Future Enhancements

* Transformer-based models
* GPT-style text generation
* Larger training datasets
* Top-K predictions
* Beam search implementation
* Model deployment on cloud platforms

---

## Learning Outcomes

* Natural Language Processing
* Deep Learning
* LSTM Networks
* GRU Networks
* Text Tokenization
* Sequence Modeling
* Flask Development
* Model Deployment Concepts

---

## Author

Sonu Lad

GitHub: https://github.com/mandar353

LinkedIn: https://www.linkedin.com/in/sonu-lad-2184561b3
