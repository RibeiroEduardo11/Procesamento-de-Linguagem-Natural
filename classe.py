import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

# Downloads necessários
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('vader_lexicon')

# Texto que será analisado
texto = """
Eu odiei este aplicativo
"""

# -----------------------------------------
# 1. TOKENIZAÇÃO
# -----------------------------------------

tokens = word_tokenize(texto, language='portuguese')

print("TOKENS:")
print(tokens)


# -----------------------------------------
# 2. NORMALIZAÇÃO
# -----------------------------------------

tokens_minusculos = [
    palavra.lower()
    for palavra in tokens
    if palavra.isalpha()
]

print("\nTOKENS NORMALIZADOS:")
print(tokens_minusculos)


# -----------------------------------------
# 3. REMOÇÃO DE STOPWORDS
# -----------------------------------------

stop_words = set(stopwords.words('portuguese'))

tokens_sem_stopwords = [
    palavra
    for palavra in tokens_minusculos
    if palavra not in stop_words
]

print("\nSEM STOPWORDS:")
print(tokens_sem_stopwords)


# -----------------------------------------
# 4. STEMMING
# -----------------------------------------

stemmer = RSLPStemmer()

stems = [
    stemmer.stem(palavra)
    for palavra in tokens_sem_stopwords
]

print("\nSTEMMING:")
print(stems)


# -----------------------------------------
# 5. FREQUÊNCIA DAS PALAVRAS
# -----------------------------------------

frequencia = Counter(tokens_sem_stopwords)

print("\nFREQUÊNCIA:")
for palavra, quantidade in frequencia.most_common():
    print(f"{palavra}: {quantidade}")


# -----------------------------------------
# 6. ANÁLISE DE SENTIMENTO
# -----------------------------------------

analisador = SentimentIntensityAnalyzer()

resultado = analisador.polarity_scores(texto)

print("\nANÁLISE DE SENTIMENTO:")
print(resultado)

# Interpretação simples
compound = resultado['compound']

if compound >= 0.05:
    sentimento = "Positivo"
elif compound <= -0.05:
    sentimento = "Negativo"
else:
    sentimento = "Neutro"

print(f"Sentimento: {sentimento}")