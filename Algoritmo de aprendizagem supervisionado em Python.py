# Importar bibliotecas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de Regressão Logística
logistic_model = LogisticRegression()

# Treinar o modelo
logistic_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predictions = logistic_model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo de Regressão Logística: {accuracy}')

# Exibir o relatório de classificação
print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))

#Esse código é um exemplo de como usar a biblioteca `scikit-learn` em Python para construir e avaliar um modelo de Regressão Logística para classificação. Vamos analisá-lo linha por linha:

#1. **Importação de bibliotecas:** Aqui, estamos importando as bibliotecas necessárias para trabalhar com machine learning em Python. Isso inclui o conjunto de dados Iris (`datasets`), funções para dividir o conjunto de dados em treino e teste (`train_test_split`), o modelo de Regressão Logística (`LogisticRegression`), e algumas métricas de avaliação de modelo (`accuracy_score` e `classification_report`).
#2. **Carregamento dos dados:** O conjunto de dados Iris é carregado usando a função `load_iris()` da biblioteca `datasets`. Os dados são divididos em dois arrays `X` (features) e `y` (rótulos).
#3. **Divisão do conjunto de dados:** O conjunto de dados é dividido em conjuntos de treino e teste usando a função `train_test_split()`. Neste caso, 80% dos dados são usados para treino e 20% para teste.
#4. **Criação do modelo:** Um objeto de Regressão Logística é criado usando `LogisticRegression()`.
#5. **Treinamento do modelo:** O modelo é treinado com os dados de treino usando o método `fit()`.
#6. **Previsões:** Usamos o modelo treinado para fazer previsões nos dados de teste usando o método `predict()`.
#7. **Avaliação do modelo:** A acurácia do modelo é calculada usando a função `accuracy_score()`, comparando as previsões com os rótulos reais dos dados de teste. Em seguida, é exibido um relatório de classificação usando `classification_report()`, que fornece métricas de precisão, recall, f1-score e suporte para cada classe.
#O comentário no final do código fornece uma breve explicação do que está sendo feito e lembra ao usuário que diferentes conjuntos de dados podem exigir diferentes abordagens e modelos. É uma boa prática adaptar o código de acordo com o caso de uso específico.
