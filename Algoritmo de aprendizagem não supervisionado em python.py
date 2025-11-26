# Exemplo simples de aprendizado não supervisionado usando o algoritmo K-Means. Neste exemplo, usaremos a biblioteca scikit-learn e o conjunto de dados Iris:

# Importar bibliotecas
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple


def load_iris_data() -> np.ndarray:
    """
    Carrega o conjunto de dados Iris.
    
    Returns:
        np.ndarray: Matriz de características do conjunto de dados Iris.
    """
    iris = datasets.load_iris()
    return iris.data


def perform_kmeans_clustering(data: np.ndarray, n_clusters: int = 3, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """
    Realiza o agrupamento K-Means nos dados fornecidos.
    
    Args:
        data: Matriz de características para agrupamento.
        n_clusters: Número de clusters a serem formados.
        random_state: Semente para reprodutibilidade.
        
    Returns:
        Tuple contendo os rótulos dos clusters e os centróides.
    """
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans_model.fit(data)
    
    return kmeans_model.labels_, kmeans_model.cluster_centers_


def visualize_clusters(data: np.ndarray, labels: np.ndarray, centroids: np.ndarray) -> None:
    """
    Visualiza os clusters e seus centróides.
    
    Args:
        data: Matriz de características.
        labels: Rótulos dos clusters para cada ponto de dados.
        centroids: Coordenadas dos centróides dos clusters.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', edgecolor='k')
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=3, color='r')
    plt.title('Clusters identificados pelo K-Means')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.colorbar(label='Cluster')
    plt.show()


def main() -> None:
    """Função principal que executa o fluxo completo de clustering."""
    # Carregar dados
    X = load_iris_data()
    
    # Realizar clustering
    labels, centroids = perform_kmeans_clustering(X)
    
    # Visualizar resultados
    visualize_clusters(X, labels, centroids)


if __name__ == "__main__":
    main()#tri como usar o K-Means para encontrar padrões nos dados, mesmo sem rótulos prévios, e visualizar esses padrões por meio da clusterização.
