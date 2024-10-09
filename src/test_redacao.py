# src/test_redacao.py
from corretor import avaliar_redacao_com_modelo
from processamento import aplicar_regras_conhecimento, aplicar_languagetool
import joblib  # Para carregar o modelo salvo

# Exemplo de redação para teste
redacao_exemplo = """
A liberdade de expressão, assim como o direito à intimidade são conquistas históricas. Quando um entra em contato com o outro, é preciso pesar com bom senso os dois lados.
Em épocas de regime autoritários como as ditadura militar na América Latina e fascistas na Europa, a imprensa não tinha liberdade para veicular notícias diversas, esbarrando comumente na censura. Nessas épocas, as pessoas também sofriam graves violações em suas vidas privadas por meio de tortura e constrangimentos, por exemplo, mas com a ascenção da democracia no ocidente, esses direitos foram amplamente protegidos por lei.
Porém, há casos em que essas garantias são postas em conflito, como em que figuras públicas, principalmente políticas, são pauta de notícias que esbarram em sua intimidade. Assim, o alvo dessas matérias, pode requerer sigilo 
por se tratar da sua vida privada enquanto a imprensa vê cerceada sua liberdade de expressão.
Portanto, é preciso avaliar até onde o direito de expressão pode ser abusivo, lesar a honra do cidadão, e até mesmo causar transtornos psicológicos ao alvo das notícias. Dessa forma, o bem estar do ser humano deve estar à frente da liberdade de expressão quando esta não for de suma necessidade ao conhecimento público.
"""

# Função para carregar o modelo salvo
def carregar_modelo_salvo():
    caminho_modelo = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\modelo_treinado_teste.pkl"
    try:
        modelo = joblib.load(caminho_modelo)
        print(f"Modelo carregado de {caminho_modelo}")
        return modelo
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        return None

# Função principal para teste
if __name__ == "__main__":
    modelo = carregar_modelo_salvo()  # Carregar o modelo treinado previamente
    
    if modelo is not None:
        # Avaliar a redação de exemplo
        nota_final, erros_ortograficos, erros_languagetool = avaliar_redacao_com_modelo(redacao_exemplo, modelo)

        # Exibir os resultados
        print(f"Texto da Redação:\n{redacao_exemplo}")
        print(f"Nota Final: {nota_final:.2f}")
        print(f"Erros Ortográficos: {erros_ortograficos}")
        print(f"Erros LanguageTool: {erros_languagetool}")
    else:
        print("Não foi possível carregar o modelo.")
