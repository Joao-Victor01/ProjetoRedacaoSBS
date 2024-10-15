import pandas as pd
import joblib
import shap
from sklearn.model_selection import train_test_split

# Carregar o DataFrame com as features extraídas
arquivo_csv = '/Users/rainerterroso/Downloads/redacoes_features.csv'
df = pd.read_csv(arquivo_csv)

# Separar as features (X) e o alvo (y)
X = df[['num_caracteres', 'num_palavras', 'num_paragrafos', 'tamanho_medio_paragrafos',
        'palavras_unicas', 'repeticao_palavras', 'tamanho_medio_palavras', 
        'erros_ortograficos', 'erros_gramaticais', 'erros_concordancia']]
y = df['nota']

# Carregar o modelo de regressão linear treinado
modelo = joblib.load('/Users/rainerterroso/Downloads/ProjetoRedacaoSBS-melhorias-concordancia/modelo_treinado.pkl')

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplicando o SHAP no modelo carregado
explainer = shap.Explainer(modelo, X_train)  
shap_values = explainer(X_test)  

# Plotar o gráfico SHAP para visualização
shap.summary_plot(shap_values, X_test)

# Exemplo de gráfico de dependência para a primeira feature (por exemplo, 'num_caracteres')
shap.dependence_plot(0, shap_values.values, X_test)
