# 🧠 Learning Python — PLN

Projeto desenvolvido para estudar **Processamento de Linguagem Natural (PLN)** utilizando Python e a biblioteca **NLTK**.

O projeto explora, de forma prática, como um computador pode analisar textos e identificar sentimentos, além de demonstrar uma etapa básica de PLN através da **tokenização**.

---

## 📌 Sobre o projeto

O objetivo deste projeto é compreender os conceitos básicos de **Processamento de Linguagem Natural** por meio de experimentos simples em Python.

Foram desenvolvidas duas abordagens para classificação de sentimentos:

- 🔹 **Com tokenização:** o texto é dividido em tokens antes da análise.
- 🔹 **Sem tokenização explícita:** o texto é enviado diretamente para o analisador de sentimentos.

A comparação entre as duas abordagens permite observar a diferença entre uma etapa de PLN realizada explicitamente pelo programa e o processamento realizado internamente por uma biblioteca.

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python**
- 📚 **NLTK (Natural Language Toolkit)**
- 💭 **VADER Sentiment Analysis**

---

## 🔎 Conceitos estudados

Durante o desenvolvimento foram trabalhados conceitos como:

- Processamento de Linguagem Natural
- Tokenização
- Análise de sentimentos
- Classificação de textos
- Sentimentos positivo, negativo e neutro
- Negação
- Intensificadores
- Gírias
- Sarcasmo
- Pontuação
- Letras maiúsculas
- Score `compound`

---

## ⚙️ Como funciona

### 1. Entrada

O usuário digita uma frase no terminal.

```text
Digite uma frase: This movie is excellent!
```

### 2. Tokenização

Na versão com tokenização, a frase é dividida em unidades menores:

```text
This | movie | is | excellent | !
```

Essas unidades são chamadas de **tokens**.

### 3. Análise de sentimento

O VADER analisa a frase e retorna diferentes pontuações:

```text
neg
neu
pos
compound
```

O valor utilizado para determinar a classificação final é o `compound`.

### 4. Classificação

A classificação utilizada no projeto é:

| Valor `compound` | Sentimento |
|---|---|
| `>= 0.05` | 🟢 Positivo |
| `<= -0.05` | 🔴 Negativo |
| Entre os valores | ⚪ Neutro |

---

## 🧪 Exemplos

### Sentimento positivo

```text
This movie is excellent!
```

Resultado esperado:

```text
Sentimento: POSITIVO
```

### Sentimento negativo

```text
This movie is terrible.
```

Resultado esperado:

```text
Sentimento: NEGATIVO
```

### Negação

```text
This is not a good movie.
```

Esse tipo de frase demonstra uma dificuldade comum da análise de sentimentos: uma palavra isoladamente positiva pode assumir outro significado quando aparece junto de uma negação.

### Sarcasmo

```text
Awesome, another parking ticket. Just what I need!
```

Esse exemplo demonstra como o sarcasmo pode dificultar a interpretação automática de sentimentos.

---

## 🇧🇷 Observação sobre português

O VADER foi desenvolvido principalmente para análise de textos em **inglês**.

Por isso, embora o programa consiga receber textos em português, sua análise não necessariamente terá a mesma qualidade que teria em inglês.

Esse é um dos pontos observados durante o projeto e representa uma das limitações da abordagem utilizada.

---

## 📂 Estrutura do projeto

```text
LearningPython-PLN/
│
├── 📁 ...
├── 📄 README.md
└── 📄 ...
```

> A estrutura pode variar conforme os experimentos adicionados ao projeto.

---

## 🎯 Objetivos de aprendizagem

Este projeto foi desenvolvido com o objetivo de:

- compreender os conceitos básicos de PLN;
- entender o funcionamento da tokenização;
- utilizar uma biblioteca de PLN em Python;
- experimentar análise automática de sentimentos;
- comparar diferentes formas de processamento;
- identificar limitações de classificadores baseados em léxico.

---

## 🚀 Possíveis melhorias

Como próximos passos, o projeto pode evoluir para:

- suporte melhor para português;
- criação de um classificador próprio;
- utilização de conjuntos de dados para treinamento;
- comparação entre diferentes métodos de análise;
- tratamento de frases mais complexas;
- desenvolvimento de uma interface gráfica ou web.

---

## 📚 Referências

- [NLTK — Natural Language Toolkit](https://www.nltk.org/)
- [NLTK — Sample usage for sentiment](https://www.nltk.org/howto/sentiment.html)
- [NLTK — SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.SentimentIntensityAnalyzer.html)

---

## 👨‍💻 Autor

**Eduardo Ribeiro**

Projeto desenvolvido para estudos de **Python e Processamento de Linguagem Natural (PLN)**.

⭐ Se este projeto foi útil para você, fique à vontade para explorar o código e acompanhar a evolução do projeto.