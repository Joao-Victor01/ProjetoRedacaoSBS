import xml.etree.ElementTree as ET

# Carregar o arquivo XML
tree = ET.parse('C:/Users/joao-/Desktop/JV/Educação/UFPB/Disciplinas/Sistemas Baseados em Conhecimento/Projeto_Redacao/data/DatasetRedacoes.xml')  
root = tree.getroot()

# Função para extrair o texto da redação e as notas por competência
def extrair_redacao_e_notas(essay_element):
    # Extrair o texto original da redação
    texto = essay_element.find('original').text.strip() if essay_element.find('original') is not None else 'Texto não encontrado'
    
    # Extrair as notas das competências
    competencias = {}
    criteria = essay_element.find('criteria')
    if criteria is not None:
        for criterion in criteria.findall('criterion'):
            nome = criterion.find('name').text.strip()
            nota = criterion.find('score').text.strip()
            competencias[nome] = nota

    return texto, competencias

# Limitar o número de redações a exibir
quantidade_redacoes = 5  # Altere para o número de redações que você deseja exibir
contador = 0

# Extrair as redações e suas notas
for essay in root.findall('.//essay'):
    if contador >= quantidade_redacoes:
        break
    texto, competencias = extrair_redacao_e_notas(essay)
    print(f"Texto da Redação:\n{texto}")
    print(f"Notas por Competência: {competencias}")
    print("-" * 80)
    contador += 1
