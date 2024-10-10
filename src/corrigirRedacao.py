import joblib
from processamento import aplicar_regras_conhecimento, aplicar_languagetool
from corretor import carregar_erros_concordancia, extrair_features

# Caminho do modelo salvo e arquivo de erros de concordância
caminho_modelo = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\modelo_treinado.pkl"
caminho_erros_concordancia = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\errosConcordancia.txt"

# Função para corrigir a redação com o modelo salvo
def corrigir_redacao(texto_redacao):
    # Carregar o modelo salvo
    modelo = joblib.load(caminho_modelo)
    
    # Carregar os erros de concordância
    erros_concordancia = carregar_erros_concordancia(caminho_erros_concordancia)

    # Extrair as features do texto da redação
    features = extrair_features(texto_redacao, erros_concordancia)

    # Verificar se as features foram extraídas corretamente
    if features is None:
        print("Erro ao extrair características da redação.")
        return

    # Fazer a previsão da nota usando o modelo
    nota_prevista = modelo.predict([features])[0]
    
    # Aplicar as correções ortográficas e gramaticais
    erros_ortograficos = aplicar_regras_conhecimento(texto_redacao)
    erros_gramaticais = aplicar_languagetool(texto_redacao)

    # Exibir os resultados
    print(f"\nTexto Original:\n{texto_redacao}")
    print(f"\nNota Prevista para Competência 1: {nota_prevista:.2f}")
    
    print("\nErros Ortográficos:")
    for erro in erros_ortograficos:
        print(f"- Palavra incorreta: {erro[0]} -> Correção sugerida: {erro[1]}")
    
    print("\nErros Gramaticais:")
    for erro in erros_gramaticais:
        print(erro)

# Solicitar o texto da redação ao usuário
texto_redacao = input("Digite o texto da redação para correção:\n")

# Corrigir a redação fornecida
corrigir_redacao(texto_redacao)
