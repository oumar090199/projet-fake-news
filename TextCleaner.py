from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# La classe TextCleaner
class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        cleaned_texts = []
        for text in X:
            text = text.lower()  # Mettre en minuscule
            text = re.sub(r'<.*?>', '', text)  # Supprimer le HTML
            text = re.sub(r'\[.*?\]', '', text)  # Supprimer les crochets carrés et leur contenu
            text = re.sub(r'[^a-zA-Z\s]', '', text)  # Supprimer les caractères spéciaux et les chiffres
            words = word_tokenize(text)  # Tokenisation
            words = [word for word in words if word not in stopwords.words('english')]  # Supprimer les mots vides
            cleaned_text = ' '.join(words)
            cleaned_texts.append(cleaned_text)
        return cleaned_texts