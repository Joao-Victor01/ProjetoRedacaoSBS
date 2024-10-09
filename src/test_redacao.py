# src/test_redacao.py
from corretor import avaliar_redacao_com_modelo
from processamento import aplicar_regras_conhecimento, aplicar_languagetool
import xml.etree.ElementTree as ET
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib  # Para salvar e carregar o modelo

# Exemplo de redação para teste
redacao_exemplo = """
A liberdade de expressão, assim como o direito à intimidade são conquistas históricas. Quando um entra em contato com o outro, é preciso pesar com bom senso os dois lados.
Em épocas de regime autoritários como as ditadura militar na América Latina e fascistas na Europa, a imprensa não tinha liberdade para veicular notícias diversas, esbarrando comumente na censura. Nessas épocas, as pessoas também sofriam graves violações em suas vidas privadas por meio de tortura e constrangimentos, por exemplo, mas com a ascenção da democracia no ocidente, esses direitos foram amplamente protegidos por lei.
Porém, há casos em que essas garantias são postas em conflito, como em que figuras públicas, principalmente políticas, são pauta de notícias que esbarram em sua intimidade. Assim, o alvo dessas matérias, pode requerer sigilo 
por se tratar da sua vida privada enquanto a imprensa vê cerceada sua liberdade de expressão.
Portanto, é preciso avaliar até onde o direito de expressão pode ser abusivo, lesar a honra do cidadão, e até mesmo causar transtornos psicológicos ao alvo das notícias. Dessa forma, o bem estar do ser humano deve estar à frente da liberdade de expressão quando esta não for de suma necessidade ao conhecimento público.
"""

# Carregar o dataset e treinar o modelo
def carregar_e_treinar_modelo():
    caminho_xml = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\DatasetRedacoes.xml"
    
    # Função para carregar o dataset (extraída do corretor.py)
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

    redacoes, notas = carregar_dataset(caminho_xml)

    # Treinar e salvar o modelo
    return treinar_modelo(redacoes, notas)

# Função principal para teste
if __name__ == "__main__":
    modelo = carregar_e_treinar_modelo()  # Carregar ou treinar o modelo
    
    # Avaliar a redação de exemplo
    nota_final, erros_ortograficos, erros_languagetool = avaliar_redacao_com_modelo(redacao_exemplo, modelo)

    # Exibir os resultados
    print(f"Texto da Redação:\n{redacao_exemplo}")
    print(f"Nota Final: {nota_final:.2f}")
    print(f"Erros Ortográficos: {erros_ortograficos}")
    print(f"Erros LanguageTool: {erros_languagetool}")
