# src/test_redacao.py
from corretor import avaliar_redacao_completa, extrair_features  # Importando a função extrair_features
from processamento import aplicar_regras_conhecimento, aplicar_pln
from sklearn.linear_model import LinearRegression
import xml.etree.ElementTree as ET

# Exemplo de redação para teste
redacao_exemplo = """
A liberdade de expressão, assim como o direito à intimidade são conquistas históricas. Quando um entra em contato com o outro, é preciso pesar com bom senso os dois lados.
Em épocas de regimes autoritários como as ditaduras militares na América Latina e fascistas na Europa, a imprensa não tinha liberdade para veicular notícias diversas, esbarrando comumente na censura. Nessas épocas, as pessoas também sofriam graves violações em suas vidas privadas por meio de tortura e constrangimentos, por exemplo, mas com a ascenção da democracia no ocidente , esses direitos foram amplamente protegidos por lei.
Porém, há casos em que essas garantias são postas em conflito, como em que figuras públicas, principalmente políticas, são pauta de notícias que esbarram em sua intimidade. Assim, o alvo dessas matérias, pode requerer sigilo 
por se tratar da sua vida privada enquanto a imprensa vê cerceada sua liberdade de expressão.
Portanto, é preciso avaliar até onde o direito de expressão pode ser abusivo, lesar a honra do cidadão, e até mesmo causar transtornos psicológicos ao alvo das notícias. Dessa forma, o bem estar do ser humano deve estar à frente da liberdade de expressão quando esta não for de suma necessidade ao conhecimento público.
"""

# Avaliar a redação com modelo
def avaliar_redacao_completa(texto, modelo):
    features = extrair_features(texto)
    nota_prevista = modelo.predict([features])[0]

    # Aplicar as regras de conhecimento e PLN
    erros_ortograficos, erros_gramaticais = aplicar_regras_conhecimento(texto)
    erros_pln = aplicar_pln(texto)

    return nota_prevista, erros_ortograficos, erros_gramaticais, erros_pln

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

    # Treinar o modelo (Linear Regression)
    modelo = LinearRegression()
    features = [extrair_features(redacao) for redacao in redacoes]
    modelo.fit(features, notas)

    return modelo

# Função principal para teste
if __name__ == "__main__":
    modelo = carregar_e_treinar_modelo()
    
    # Avaliar a redação de exemplo
    nota_final, erros_ortograficos, erros_gramaticais, erros_pln = avaliar_redacao_completa(redacao_exemplo, modelo)

    # Exibir os resultados
    print(f"Texto da Redação:\n{redacao_exemplo}")
    print(f"Nota Final: {nota_final:.2f}")
    print(f"Erros Ortográficos: {erros_ortograficos}")
    print(f"Erros Gramaticais: {erros_gramaticais}")
    print(f"Erros PLN: {erros_pln}")
