import json
import requests
import pandas as pd
from datetime import datetime
import os
import googletrans
from googletrans import Translator

def run_translator():
    CUR_DIR = os.path.abspath(os.path.dirname(__file__))

    translator = Translator()
    valid_languages = googletrans.LANGUAGES.keys()

    df = pd.read_json(CUR_DIR + "/" + "tweets-json.json")

    # Drop rows where the source language is unclear
    for i, row in df.iterrows():
        if df.at[i, 'Language'] != 'en':
            if df.at[i, 'Language'] not in valid_languages:
                df.drop(i, inplace=True)

    # Translate tweets and replace text with translation
    for i, row in df.iterrows():
        if df.at[i, 'Language'] != 'en':
            df.at[i, 'Text'] = translator.translate(df.at[i, 'Text'], dest="en", src=df.at[i, 'Language']).text

    print(df.head(4))
    df.to_json(CUR_DIR + "/" + "translated-tweets-json.json")