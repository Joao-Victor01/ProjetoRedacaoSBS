# src/corretor.py
from processamento import aplicar_regras_conhecimento, aplicar_languagetool
import xml.etree.ElementTree as ET
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib  # Para salvar e carregar o modelo
import time  # Para medir o tempo de execução

# Caminho do arquivo de erros de concordância
caminho_erros_concordancia = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\errosConcordancia.txt"

# Função para carregar erros de concordância do arquivo
def carregar_erros_concordancia(caminho_arquivo):
    erros_concordancia = {}
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                if not linha.startswith("#") and linha.strip():
                    erro, correcao = linha.split('|')
                    erros_concordancia[erro.strip()] = correcao.strip()
        print(f"Erros de concordância carregados: {len(erros_concordancia)}")
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado. Nenhum erro carregado.")
    return erros_concordancia

# Função para salvar novos erros de concordância no arquivo
def salvar_erros_concordancia(caminho_arquivo, novos_erros):
    with open(caminho_arquivo, 'a', encoding='utf-8') as f:
        for erro, correcao in novos_erros.items():
            f.write(f"{erro} | {correcao}\n")
    print(f"Novos erros de concordância salvos: {len(novos_erros)}")

# Função para verificar erros de concordância
def verificar_concordancia(texto, erros_concordancia):
    erros_detectados = {}
    palavras = texto.split()

    for i in range(len(palavras) - 1):
        par_palavras = f"{palavras[i]} {palavras[i+1]}"
        if par_palavras in erros_concordancia:
            erro = f"Erro de concordância encontrado: '{par_palavras}' -> Correção: '{erros_concordancia[par_palavras]}'"
            erros_detectados[par_palavras] = erros_concordancia[par_palavras]
            print(erro)

    return erros_detectados

# Função para extrair features da redação, incluindo erros ortográficos e gramaticais
def extrair_features(texto, erros_concordancia):
    print("Iniciando extração de features...")

    try:
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
        print("Aplicando regras ortográficas e gramaticais...")
        erros_ortograficos = aplicar_regras_conhecimento(texto)
        erros_gramaticais = aplicar_languagetool(texto)

        # Verificar erros de concordância
        erros_concordancia_detectados = verificar_concordancia(texto, erros_concordancia)
        numero_erros_concordancia = len(erros_concordancia_detectados)

        numero_erros_ortograficos = len(erros_ortograficos)
        numero_erros_gramaticais = len(erros_gramaticais)

        # Retorna as features em um array
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
            numero_erros_gramaticais,
            numero_erros_concordancia,
        ]
    except Exception as e:
        print(f"Erro ao extrair características: {e}")
        return None  # Retornar None se houver um erro

# Função para treinar o modelo de regressão linear com as features
def treinar_modelo(redacoes, notas):
    print("Iniciando o treinamento do modelo...")

    # Carregar erros de concordância
    erros_concordancia = carregar_erros_concordancia(caminho_erros_concordancia)

    features = []
    novos_erros = {}  # Dicionário para novos erros
    for redacao in redacoes:
        feature = extrair_features(redacao, erros_concordancia)  # Passando erros de concordância
        if feature is not None:  # Verificar se a extração foi bem-sucedida
            features.append(feature)

        # Verifica se há novos erros de concordância detectados
        erros_detectados = verificar_concordancia(redacao, erros_concordancia)
        novos_erros.update(erros_detectados)

    # Salva os novos erros de concordância no arquivo
    if novos_erros:
        salvar_erros_concordancia(caminho_erros_concordancia, novos_erros)

    # Dividir os dados em conjunto de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(features, notas, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    start_time = time.time()  # Registra o tempo de início
    modelo.fit(X_train, y_train)
    end_time = time.time()  # Registra o tempo de término

    # Avaliar o modelo
    score = modelo.score(X_test, y_test)
    print(f"Precisão do modelo: {score * 100:.2f}%")

    # Salvar o modelo treinado
    caminho_modelo = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\modelo_treinado.pkl"
    joblib.dump(modelo, caminho_modelo)
    print(f"Modelo salvo em {caminho_modelo}")

    # Calcular e exibir o tempo gasto
    tempo_gasto = end_time - start_time
    print(f"Tempo gasto para treinar o modelo: {tempo_gasto:.2f} segundos")

    return modelo

# Carregar o arquivo XML e extrair textos e notas
def carregar_dataset(caminho_xml, limite=None):  # Adicionando o parâmetro limite
    print("Carregando o dataset...")
    tree = ET.parse(caminho_xml)
    root = tree.getroot()
    redacoes = []
    notas = []

    for essay in root.findall('.//essay'):  # Carregar todas as redações
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
            notas.append(criterio1)  # Adicionando a nota correspondente

        # Limitar o número de redações se o limite for especificado
        if limite is not None and len(redacoes) >= limite:
            break
    
    print(f"Dataset carregado com sucesso. Total de redações: {len(redacoes)}")
    return redacoes, notas  # Retornar as redações e suas notas

# Função para avaliar uma redação com o modelo
def avaliar_redacao_com_modelo(texto, modelo):
    features = extrair_features(texto, erros_concordancia)  # Passando o texto e erros de concordância
    nota_prevista = modelo.predict([features])[0]
    
    # Aplicar as regras de conhecimento e LanguageTool
    erros_ortograficos = aplicar_regras_conhecimento(texto)
    erros_languagetool = aplicar_languagetool(texto)

    return nota_prevista, erros_ortograficos, erros_languagetool

# Exemplo de uso
if __name__ == "__main__":
    print("Iniciando processo...")
    caminho_xml = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\DatasetRedacoes.xml"
    redacoes, notas = carregar_dataset(caminho_xml, limite=None)  

    # Treinar o modelo
    modelo = treinar_modelo(redacoes, notas)

    # Carregar erros de concordância para uso na avaliação
    erros_concordancia = carregar_erros_concordancia(caminho_erros_concordancia)

    # Avaliar a primeira redação
    for texto_original in redacoes[:1]:  # Avaliar a primeira redação
        print("Avaliando redação...")
        nota_prevista, erros_ortograficos, erros_languagetool = avaliar_redacao_com_modelo(texto_original, modelo)
        print(f"Texto Original: {texto_original}")
        print(f"Nota Prevista para Competência 1: {nota_prevista:.2f}")
        print(f"Erros Ortográficos: {erros_ortograficos}")
        print(f"Erros LanguageTool: {erros_languagetool}")
