try:
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.probability import FreqDist
    from nltk.corpus import stopwords
except Exception:
    print("ImportError: 'nltk' não encontrado. Instale dependências com:")
    print("    python -m pip install -r requirements.txt")
    raise

# Baixar recursos necessários (você só precisa fazer isso uma vez)
# Esses downloads precisam ser executados quando o pacote NLTK for usado pela primeira vez
nltk.download('punkt')
nltk.download('stopwords')

# Texto de exemplo
sample_text = "Processamento de Linguagem Natural é fascinante! NLTK é uma ótima ferramenta para isso."

# Tokenização de palavras
tokens = word_tokenize(sample_text)

# Remoção de stopwords (palavras comuns que geralmente não contribuem para o significado)
stop_words = set(stopwords.words('portuguese'))  # Pode ser 'english' dependendo do idioma
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Contagem de frequência de palavras
fdist = FreqDist(filtered_tokens)

# Exibir palavras mais frequentes
print("Palavras mais frequentes:")
for word, freq in fdist.most_common(5):
    print(f"{word}: {freq} vezes")



#Esse código é um exemplo simples de como usar a biblioteca NLTK (Natural Language Toolkit) em Python para realizar algumas operações básicas de processamento de linguagem natural (PLN). Vamos passar pelo código linha por linha:

#1. `import nltk`: Isso importa o pacote NLTK, que é uma biblioteca muito útil para trabalhar com texto e PLN em Python.
#2. `from nltk.tokenize import word_tokenize`: Esta linha importa a função `word_tokenize` do módulo `tokenize` dentro do pacote `nltk`. `word_tokenize` é usada para dividir o texto em palavras (tokens).
#3. `from nltk.probability import FreqDist`: Aqui, estamos importando a classe `FreqDist` do módulo `probability` dentro do pacote `nltk`. Esta classe é usada para calcular a distribuição de frequência de uma lista de palavras.
#4. `from nltk.corpus import stopwords`: Esta linha importa a lista de stopwords do pacote `nltk.corpus`. Stopwords são palavras comuns que geralmente não contribuem muito para o significado de um texto.
#5. `nltk.download('punkt')`: Este comando faz o download do tokenizador punkt, que é usado pela função `word_tokenize` para dividir o texto em palavras.
#6. `nltk.download('stopwords')`: Aqui, estamos fazendo o download da lista de stopwords disponível no NLTK.
#7. `sample_text = "Processamento de Linguagem Natural é fascinante! NLTK é uma ótima ferramenta para isso."`: Define uma string de exemplo que contém o texto que queremos analisar.
#8. `tokens = word_tokenize(sample_text)`: Usa a função `word_tokenize` para dividir a string `sample_text` em uma lista de palavras (tokens).
#9. `stop_words = set(stopwords.words('portuguese'))`: Define uma lista de stopwords no idioma português. Isso será usado para remover as stopwords do texto.
#10. `filtered_tokens = [word for word in tokens if word.lower() not in stop_words]`: Cria uma nova lista chamada `filtered_tokens` que contém apenas as palavras de `tokens` que não estão na lista de stopwords. As palavras são convertidas para minúsculas antes de verificar se estão na lista de stopwords.
#11. `fdist = FreqDist(filtered_tokens)`: Cria um objeto `FreqDist` a partir da lista de tokens filtrados. Isso calcula a frequência de cada palavra na lista.
#12. `print("Palavras mais frequentes:")`: Imprime uma mensagem para indicar que as próximas linhas mostrarão as palavras mais frequentes.
#13. `for word, freq in fdist.most_common(5):`: Itera sobre as 5 palavras mais frequentes na distribuição de frequência (`fdist`) e imprime cada palavra e sua frequência.
#14. `print(f"{word}: {freq} vezes")`: Imprime o par palavra-frequência para cada uma das 5 palavras mais frequentes.
#Este código é útil para mostrar como realizar operações básicas de PLN, como tokenização, remoção de stopwords e cálculo da frequência das palavras em um texto.
