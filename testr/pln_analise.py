import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

analisador = SentimentIntensityAnalyzer()

while True:
    texto = input("\nDigite uma frase (ou 'sair' para encerrar): ")

    if texto.lower() == "sair":
        break

    resultado = analisador.polarity_scores(texto)

    print("\nTexto:", texto)
    print("Resultado:", resultado)

    if resultado["compound"] >= 0.05:
        print("Sentimento: POSITIVO")
    elif resultado["compound"] <= -0.05:
        print("Sentimento: NEGATIVO")
    else:
        print("Sentimento: NEUTRO")