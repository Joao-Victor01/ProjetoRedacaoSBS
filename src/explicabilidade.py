# src/explicabilidade.py
import shap

# Função para calcular explicabilidade com SHAP
def explicabilidade_shap(modelo, features):
    explainer = shap.Explainer(modelo)
    shap_values = explainer(features)
    
    # Gera plots para visualizar a explicabilidade
    shap.summary_plot(shap_values, features)

# Exemplo de uso de SHAP (quando tiver um modelo treinado)
if __name__ == "__main__":
    from corretor import carregar_dataset, extrair_features, treinar_modelo
    
    caminho_xml = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\DatasetRedacoes.xml"
    redacoes = carregar_dataset(caminho_xml)
    
    # Extrair features e notas
    features, notas = extrair_features(redacoes)
    
    # Treinar o modelo
    modelo = treinar_modelo(features, notas)
    
    # Usando SHAP para justificar a nota
    explicabilidade_shap(modelo, features)
