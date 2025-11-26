#O teorema de Bayes é uma fórmula fundamental em probabilidade condicional. Vou fornecer um exemplo simples em Python para ilustrar como você pode implementar o teorema de Bayes em um contexto de classificação. Neste exemplo, usaremos o teorema de Bayes ingênuo (Naive Bayes) para classificar o texto como positivo ou negativo:

class NaiveBayesClassifier:
    def __init__(self, positive_prob, negative_prob):
        self.positive_prob = positive_prob
        self.negative_prob = negative_prob

    def classify(self, text):
        # Aplicar o Teorema de Bayes
        evidence = text.split()
        positive_likelihood = self.calculate_likelihood(self.positive_prob, evidence)
        negative_likelihood = self.calculate_likelihood(self.negative_prob, evidence)

        # Classificar com base nas probabilidades calculadas
        if positive_likelihood > negative_likelihood:
            return "Positivo"
        else:
            return "Negativo"

    def calculate_likelihood(self, prior_prob, evidence):
        likelihood = prior_prob  # Inicializar com a probabilidade priori

        # Simplesmente multiplicar as probabilidades de cada palavra no texto
        for word in evidence:
            likelihood *= self.word_probability(word)

        return likelihood

    def word_probability(self, word):
        # Probabilidades condicionais fictícias para ilustração
        positive_word_prob = 0.8
        negative_word_prob = 0.2

        # Supondo que as palavras são independentes (Naive Bayes)
        return positive_word_prob if word in ["good", "excellent"] else negative_word_prob

# Exemplo de uso
positive_prior_prob = 0.5
negative_prior_prob = 0.5

classifier = NaiveBayesClassifier(positive_prior_prob, negative_prior_prob)

# Texto de exemplo a ser classificado
input_text = "This movie is excellent and highly recommended."

# Classificar o texto
classification_result = classifier.classify(input_text)
print(f"A classificação do texto é: {classification_result}")

#Este é um exemplo muito simplificado para ilustrar a aplicação do teorema de Bayes ingênuo em uma tarefa de classificação de texto. Em um cenário real, você precisaria de dados mais complexos e probabilidades mais precisas para obter resultados significativos.


#Este é um exemplo simplificado de como implementar um classificador de texto utilizando o Teorema de Bayes ingênuo (Naive Bayes). Vamos passar pelo código e explicar cada parte:


class NaiveBayesClassifier:
    def __init__(self, positive_prob, negative_prob):
        self.positive_prob = positive_prob
        self.negative_prob = negative_prob

    def classify(self, text):
        # Aplicar o Teorema de Bayes
        evidence = text.split()
        positive_likelihood = self.calculate_likelihood(self.positive_prob, evidence)
        negative_likelihood = self.calculate_likelihood(self.negative_prob, evidence)

        # Classificar com base nas probabilidades calculadas
        if positive_likelihood > negative_likelihood:
            return "Positivo"
        else:
            return "Negativo"

    def calculate_likelihood(self, prior_prob, evidence):
        likelihood = prior_prob  # Inicializar com a probabilidade priori

        # Simplesmente multiplicar as probabilidades de cada palavra no texto
        for word in evidence:
            likelihood *= self.word_probability(word)

        return likelihood

    def word_probability(self, word):
        # Probabilidades condicionais fictícias para ilustração
        positive_word_prob = 0.8
        negative_word_prob = 0.2

        # Supondo que as palavras são independentes (Naive Bayes)
        return positive_word_prob if word in ["good", "excellent"] else negative_word_prob


#1. `NaiveBayesClassifier`: É a classe que define o classificador Naive Bayes. Ela possui métodos para inicializar os valores de probabilidade positiva e negativa, classificar textos e calcular a probabilidade condicional de cada palavra.

2#. `__init__`: O método de inicialização da classe que recebe as probabilidades positivas e negativas como argumentos e as armazena nos atributos `positive_prob` e `negative_prob`, respectivamente.

#3. `classify`: Este método recebe um texto como entrada, divide-o em palavras (evidence) e calcula a probabilidade de ser positivo e negativo usando o Teorema de Bayes. Retorna a classificação do texto como "Positivo" ou "Negativo" com base nas probabilidades calculadas.

#4. `calculate_likelihood`: Método para calcular a verossimilhança de uma evidência (uma lista de palavras) dada a probabilidade priori. Ele multiplica a probabilidade priori pela probabilidade condicional de cada palavra no texto.

#5. `word_probability`: Método para calcular a probabilidade condicional de uma palavra dada. Neste exemplo, as probabilidades condicionais são definidas de forma fictícia para ilustração, onde as palavras "good" e "excellent" têm uma alta probabilidade de serem positivas, enquanto todas as outras palavras têm uma alta probabilidade de serem negativas.


# Exemplo de uso
positive_prior_prob = 0.5
negative_prior_prob = 0.5

classifier = NaiveBayesClassifier(positive_prior_prob, negative_prior_prob)

# Texto de exemplo a ser classificado
input_text = "This movie is excellent and highly recommended."

# Classificar o texto
classification_result = classifier.classify(input_text)
print(f"A classificação do texto é: {classification_result}")


#Neste trecho, um exemplo de uso do classificador é fornecido. É inicializado um objeto `NaiveBayesClassifier` com probabilidades prévias positivas e negativas iguais. Em seguida, é fornecido um texto de exemplo que será classificado como "Positivo" ou "Negativo" com base nas probabilidades calculadas pelo classificador.

#Este é um exemplo simplificado para ilustrar o conceito do Teorema de Bayes ingênuo em classificação de texto. Em cenários reais, seriam necessários dados mais complexos e probabilidades mais precisas para obter resultados significativos.
