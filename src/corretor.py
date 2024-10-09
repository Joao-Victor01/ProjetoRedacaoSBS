from processamento import aplicar_regras_conhecimento, aplicar_languagetool
import xml.etree.ElementTree as ET
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Função para extrair features da redação
def extrair_features(texto):
    print("Iniciando extração de features...")
    
    numero_caracteres = len(texto)
    palavras = texto.split()
    numero_palavras = len(palavras)
    parágrafos = texto.split('\n')
    numero_paragrafos = len(parágrafos)
    tamanho_medio_paragrafos = sum(len(p) for p in parágrafos) / max(numero_paragrafos, 1)
    palavras_unicas = len(set(palavras))
    repeticao_palavras = numero_palavras / max(palavras_unicas, 1)
    tamanho_medio_palavras = sum(len(p) for p in palavras) / max(numero_palavras, 1)

    # Aplicar as regras de conhecimento
    print("Aplicando regras ortográficas...")
    erros_ortograficos = aplicar_regras_conhecimento(texto)

    # Aplicar correções gramaticais com LanguageTool
    print("Aplicando correções gramaticais com LanguageTool...")
    erros_gramaticais = aplicar_languagetool(texto)

    numero_erros_ortograficos = len(erros_ortograficos)
    numero_erros_gramaticais = len(erros_gramaticais)

    print("Extração de features concluída.")
    return [
        numero_caracteres,
        numero_palavras,
        numero_paragrafos,
        tamanho_medio_paragrafos,
        palavras_unicas,
        repeticao_palavras,
        tamanho_medio_palavras,
        numero_erros_ortograficos,
        numero_erros_gramaticais
    ]

# Função para treinar o modelo de regressão linear
def treinar_modelo(redacoes, notas):
    print("Iniciando o treinamento do modelo...")
    features = [extrair_features(redacao) for redacao in redacoes]
    X_train, X_test, y_train, y_test = train_test_split(features, notas, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    score = modelo.score(X_test, y_test)
    print(f"Precisão do modelo: {score * 100:.2f}%")

    caminho_modelo = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\modelo_treinado.pkl"
    joblib.dump(modelo, caminho_modelo)
    print(f"Modelo salvo em {caminho_modelo}")

    return modelo

# Função para avaliar uma redação com o modelo
def avaliar_redacao_com_modelo(texto, modelo):
    features = extrair_features(texto)
    nota_prevista = modelo.predict([features])[0]

    erros_ortograficos = aplicar_regras_conhecimento(texto)
    erros_gramaticais = aplicar_languagetool(texto)

    return nota_prevista, erros_ortograficos, erros_gramaticais

# Função para carregar o dataset
def carregar_dataset(caminho_xml):
    print("Carregando o dataset...")
    tree = ET.parse(caminho_xml)
    root = tree.getroot()
    redacoes = []
    notas = []

    for essay in root.findall('.//essay'):
        original_tag = essay.find('original')
        texto_original = original_tag.text.strip() if original_tag is not None and original_tag.text is not None else 'Texto não encontrado'

        criterio1 = None
        criteria = essay.find('criteria')
        if criteria is not None:
            for criterion in criteria.findall('criterion'):
                nome = criterion.find('name').text.strip() if criterion.find('name') is not None else 'Nome não encontrado'
                if nome == "Competência 1":
                    score_tag = criterion.find('score')
                    if score_tag is not None and score_tag.text is not None:
                        try:
                            nota = score_tag.text.split()[0].strip().replace(',', '.')
                            criterio1 = float(nota)
                        except ValueError:
                            print(f"Erro ao converter a nota para float: {score_tag.text}")

        if criterio1 is not None:
            redacoes.append(texto_original)
            notas.append(criterio1)

    print(f"Dataset carregado com sucesso. Total de redações: {len(redacoes)}")
    return redacoes, notas

# Exemplo de uso
if __name__ == "__main__":
    print("Iniciando processo...")
    caminho_xml = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\DatasetRedacoes.xml"
    redacoes, notas = carregar_dataset(caminho_xml)

    modelo = treinar_modelo(redacoes, notas)

    for texto_original in redacoes[:1]:
        print("Avaliando redação...")
        nota_prevista, erros_ortograficos, erros_gramaticais = avaliar_redacao_com_modelo(texto_original, modelo)
        print(f"Texto Original: {texto_original}")
        print(f"Nota Prevista para Competência 1: {nota_prevista:.2f}")
        print(f"Erros Ortográficos: {erros_ortograficos}")
        print(f"Erros Gramaticais: {erros_gramaticais}")
