# Language Translator App - Streamlit

A simple Streamlit web app for translating text between English, Hindi, Marathi, Spanish, French, German, Arabic, Japanese and more.

## Features

- Translate text from one language to another
- English to Hindi translation
- Hindi to English translation
- Supports many popular languages
- Translation history
- Download translation result as `.txt`
- Batch translate using CSV upload
- Beginner-friendly project structure

## Project Structure

```text
language_translator_streamlit/
│
├── app.py
├── translator_utils.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Create project folder

```bash
mkdir language_translator_streamlit
cd language_translator_streamlit
```

### 2. Create virtual environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## CSV Batch Translation Format

Upload a CSV file with one column named:

```text
text
```

Example:

```csv
text
Hello, how are you?
I am learning data engineering.
This is my Streamlit project.
```

## Important Note

This project uses `deep-translator`, which connects to online translation services. You need an internet connection for translation to work.
