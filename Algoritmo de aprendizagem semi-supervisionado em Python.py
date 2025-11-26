# Importar bibliotecas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import LabelPropagation
from sklearn.metrics import accuracy_score, classification_report

# Carregar conjunto de dados de exemplo (iris dataset)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Simular um cenário semi-supervisionado rotulando apenas alguns pontos
rng = 42
random_unlabeled_points = rng.permutation(len(y))
num_unlabeled_points = 100
y[random_unlabeled_points[:num_unlabeled_points]] = -1  # Rotulando como -1 para indicar dados não rotulados

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de propagação de rótulos
label_propagation_model = LabelPropagation()

# Treinar o modelo
label_propagation_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
predictions = label_propagation_model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo de Propagação de Rótulos: {accuracy}')

# Exibir o relatório de classificação
print('\nRelatório de Classificação:\n', classification_report(y_test, predictions))


#Este código demonstra um exemplo de como lidar com dados semi-supervisionados usando o algoritmo de propagação de rótulos (Label Propagation) da biblioteca Scikit-learn em Python. Vamos examinar cada parte do código:

#1. **Importação de bibliotecas**: Importamos as bibliotecas necessárias, incluindo `datasets` para carregar conjuntos de dados de exemplo, `train_test_split` para dividir os dados em conjuntos de treinamento e teste, `LabelPropagation` para criar o modelo de propagação de rótulos e métricas de avaliação como `accuracy_score` e `classification_report`.
#2. **Carregamento dos dados**: Carregamos o conjunto de dados de exemplo Iris usando `datasets.load_iris()`. Dividimos os dados em recursos (X) e rótulos (y).
#3. **Simulação de cenário semi-supervisionado**: Para simular um cenário semi-supervisionado, rotulamos aleatoriamente alguns pontos como não rotulados, atribuindo o valor -1 aos seus rótulos.
#4. **Divisão dos dados em treino e teste**: Usamos `train_test_split` para dividir os dados em conjuntos de treinamento e teste. Aqui, 80% dos dados são usados para treinamento e 20% para teste.
#5. **Criação e treinamento do modelo**: Criamos uma instância do modelo `LabelPropagation` e o treinamos com os dados de treinamento.
#6. **Fazendo previsões**: Usamos o modelo treinado para fazer previsões nos dados de teste.
#7. **Avaliação do modelo**: Calculamos a acurácia do modelo comparando as previsões com os rótulos verdadeiros usando `accuracy_score`. Também imprimimos um relatório de classificação usando `classification_report`, que fornece métricas de precisão, recall, F1-score e suporte para cada classe.
#O comentário no final do código ressalta que este é apenas um exemplo básico e que a escolha do modelo e a manipulação de dados semi-supervisionados podem variar dependendo do problema específico em questão. Portanto, é importante ajustar o código conforme necessário para o seu caso de uso.
