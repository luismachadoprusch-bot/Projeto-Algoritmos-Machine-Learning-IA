from sympy import symbols, Function, ForAll, Exists, And, Or, Not, Implies # type: ignore

# Definir variáveis
x, y = symbols('x y')

# Predicados como funções (callable)
P = Function('P')
Q = Function('Q')

# Fórmulas de lógica de primeira ordem (uso correto de Implies e ordem de argumentos em ForAll/Exists)
formula1 = ForAll(Implies(P(x), Q(x)), x)   # ∀x (P(x) → Q(x))
formula2 = Exists(And(P(x), Q(x)), x)      # ∃x (P(x) ∧ Q(x))
formula3 = Or(P(x), Not(Q(y)))             # P(x) ∨ ¬Q(y)

# Exemplo de avaliação em um domínio finito (simples demonstrador)
# Definimos um pequeno modelo que dá valores de verdade para P(n) e Q(n)
domain = [1, 2]
modelo = {P(1): True, P(2): False, Q(1): True, Q(2): True}

def eval_atom(atom, model):
	"""Avalia um átomo P(n) ou Q(n) usando o dicionário model."""
	return bool(model.get(atom, False))

# Avaliar ∀x (P(x) → Q(x)) no domínio finito
formula1_val = all((not eval_atom(P(v), modelo)) or eval_atom(Q(v), modelo) for v in domain)

# Avaliar ∃x (P(x) ∧ Q(x)) no domínio finito
formula2_val = any(eval_atom(P(v), modelo) and eval_atom(Q(v), modelo) for v in domain)

# A fórmula3 contém variáveis livres (x, y). Para demonstrar, avaliamos com uma atribuição exemplo x=1, y=2
formula3_val_example = eval_atom(P(1), modelo) or (not eval_atom(Q(2), modelo))

print(f"A fórmula 1 é verdadeira no modelo (domínio {domain})? {formula1_val}")
print(f"A fórmula 2 é verdadeira no modelo (domínio {domain})? {formula2_val}")
print(f"A fórmula 3 (com x=1,y=2) é verdadeira no modelo? {formula3_val_example}")

# Neste exemplo, usamos sympypara criar fórmulas de lógica de primeira ordem e avaliá-las em um modelo específico. Observe que as variáveis P​​e Qsão tratadas como predicadas sobre inteiros. Você pode adaptar isso para representar predicados específicos do seu domínio.
#
# Se você estiver trabalhando com lógica de primeira ordem em contextos mais complexos, você pode precisar de bibliotecas mais especializadas ou ferramentas dedicadas. Este exemplo é uma introdução básica usando sympy.


#Este código demonstra o uso da biblioteca SymPy em Python para manipulação e avaliação de expressões de lógica de primeira ordem. Vamos analisar linha por linha:

#1. **`from sympy import symbols, ForAll, Exists, And, Or, Not`**: Importa símbolos e operadores lógicos necessários da biblioteca SymPy.
#2. **`x, y = symbols('x y')`**: Define símbolos `x` e `y` para representar variáveis na lógica de primeira ordem.
#3. **`P = symbols('P', integer=True)` e `Q = symbols('Q', integer=True)`**: Define os símbolos `P` e `Q` como predicados com a opção `integer=True`, indicando que eles representam funções inteiras.
#4. **`formula1 = ForAll(x, P(x) >> Q(x))`**: Define uma fórmula de lógica de primeira ordem onde para todo `x`, `P(x)` implica `Q(x)` (`>>` representa a implicação lógica).
#5. **`formula2 = Exists(x, P(x) & Q(x))`**: Define uma fórmula de lógica de primeira ordem onde existe algum `x` tal que `P(x)` e `Q(x)` são verdadeiros (`&` representa a conjunção lógica).
#6. **`formula3 = Or(P(x), Not(Q(y)))`**: Define uma fórmula de lógica de primeira ordem onde `P(x)` é verdadeiro ou `Q(y)` é falso (`Or` representa a disjunção lógica e `Not` a negação).
#7. **`modelo = {P(1): True, P(2): False, Q(1): True, Q(2): True}`**: Define um modelo que atribui valores de verdade aos predicados `P` e `Q` para os elementos 1 e 2.
#8. **`print(f"A fórmula 1 é verdadeira no modelo? {formula1.subs(modelo)}")`**: Avalia se a `formula1` é verdadeira no modelo fornecido e imprime o resultado.
#9. **`print(f"A fórmula 2 é verdadeira no modelo? {formula2.subs(modelo)}")`**: Avalia se a `formula2` é verdadeira no modelo fornecido e imprime o resultado.
#10. **`print(f"A fórmula 3 é verdadeira no modelo? {formula3.subs(modelo)}")`**: Avalia se a `formula3` é verdadeira no modelo fornecido e imprime o resultado.
#Isso basicamente executa uma série de testes para verificar se as expressões lógicas são verdadeiras ou falsas em relação a um modelo específico, fornecendo saídas correspondentes para cada teste.
