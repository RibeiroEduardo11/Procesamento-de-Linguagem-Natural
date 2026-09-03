import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

nltk.download("vader_lexicon")
nltk.download("punkt")

analisador = SentimentIntensityAnalyzer()

while True:
    texto = input("\nDigite uma frase (ou 'sair' para encerrar): ")

    if texto.lower() == "sair":
        break

    # 1. Tokenização
    tokens = word_tokenize(texto, language="portuguese")

    print("\nTexto:", texto)
    print("Tokens:", tokens)

    # 2. Análise de sentimento
    resultado = analisador.polarity_scores(texto)

    print("Resultado:", resultado)

    # 3. Classificação do sentimento
    if resultado["compound"] >= 0.05:
        print("Sentimento: POSITIVO")
    elif resultado["compound"] <= -0.05:
        print("Sentimento: NEGATIVO")
    else:
        print("Sentimento: NEUTRO")