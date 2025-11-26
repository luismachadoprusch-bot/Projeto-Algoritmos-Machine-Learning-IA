# Importar bibliotecas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de Árvore de Decisão
decision_tree_model = DecisionTreeClassifier()

# Treinar o modelo
decision_tree_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predictions = decision_tree_model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo de Árvore de Decisão: {accuracy}')

# Exibir o relatório de classificação
print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))

# Este código é um exemplo de como usar a biblioteca scikit-learn (sklearn) para criar um modelo de classificação
# de Árvore de Decisão e avaliar sua performance em um conjunto de dados. Vou explicar linha por linha:

# 1. Importação de Bibliotecas
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, classification_report

# - Aqui, estamos importando as bibliotecas necessárias do scikit-learn. `datasets` para carregar conjuntos de dados
#   de exemplo, `train_test_split` para dividir o conjunto de dados em treino e teste, `DecisionTreeClassifier` para
#   criar o modelo de Árvore de Decisão, e `accuracy_score` e `classification_report` para avaliar a performance
#   do modelo.

# 2. Carregar Conjunto de Dados
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target

# - Estamos carregando o conjunto de dados de exemplo chamado Iris Dataset. `X` contém as características (atributos)
#   das flores e `y` contém as classes (rótulos) das flores.

# 3. Dividir o Conjunto de Dados
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# - Aqui, estamos dividindo o conjunto de dados em conjuntos de treino e teste. O parâmetro `test_size=0.2` indica que
#   20% dos dados serão usados como conjunto de teste, enquanto o restante será usado para treino. O `random_state=42`
#   é para garantir que a divisão seja sempre a mesma.

# 4. Criar e Treinar o Modelo de Árvore de Decisão
# decision_tree_model = DecisionTreeClassifier()
# decision_tree_model.fit(X_train, y_train)
# - Estamos criando um modelo de Árvore de Decisão usando o `DecisionTreeClassifier` e o treinando com os dados de treino.

# 5. Fazer Previsões
# predictions = decision_tree_model.predict(X_test)
# - Aqui, estamos usando o modelo treinado para fazer previsões sobre os dados de teste.

# 6. Avaliar a Precisão do Modelo
# accuracy = accuracy_score(y_test, predictions)
# print(f'Acurácia do modelo de Árvore de Decisão: {accuracy}')
# - Calculamos a precisão do modelo comparando as previsões feitas com os rótulos reais dos dados de teste usando
#   `accuracy_score`. Em seguida, imprimimos a acurácia.

# 7. Exibir o Relatório de Classificação
# print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))
# - O `classification_report` fornece várias métricas de avaliação (como precisão, recall, F1-score) para cada classe
#   no conjunto de dados de teste. Ele ajuda a entender melhor o desempenho do modelo em diferentes classes.
