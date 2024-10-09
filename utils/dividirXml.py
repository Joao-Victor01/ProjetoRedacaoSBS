import xml.etree.ElementTree as ET

# Caminho do arquivo XML original
caminho_xml_original = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\DatasetRedacoes.xml"
# Caminho do novo arquivo XML a ser criado
caminho_xml_novo = r"C:\Users\joao-\Desktop\JV\Educação\UFPB\Disciplinas\Sistemas Baseados em Conhecimento\Projeto_Redacao\data\DatasetReduzido.xml"

# Função para criar um novo arquivo XML com as 10 primeiras redações
def criar_novo_xml(caminho_xml_original, caminho_xml_novo):
    # Carregar o arquivo XML original
    tree = ET.parse(caminho_xml_original)
    root = tree.getroot()

    # Criar o novo elemento raiz
    novo_root = ET.Element("redacoes")

    # Contador para limitar a 10 redações
    contador = 0

    # Iterar sobre as redações no arquivo original
    for essay in root.findall('.//essay'):
        if contador >= 10:  # Limitar a 10 redações
            break
        
        original_tag = essay.find('original')
        criteria = essay.find('criteria')

        if original_tag is not None and criteria is not None:
            # Criar um novo elemento para cada redação
            nova_redacao = ET.Element("redacao")

            # Adicionar o texto original
            texto_original = ET.SubElement(nova_redacao, "texto_original")
            texto_original.text = original_tag.text.strip() if original_tag.text is not None else 'Texto não encontrado'

            # Adicionar a nota
            nota_tag = criteria.find('criterion[name="Competência 1"]/score')
            if nota_tag is not None and nota_tag.text is not None:
                nota = ET.SubElement(nova_redacao, "nota")
                nota.text = nota_tag.text.strip().replace(',', '.')

            # Adicionar a nova redação ao novo root
            novo_root.append(nova_redacao)

            contador += 1

    # Criar uma nova árvore e escrever no arquivo
    novo_tree = ET.ElementTree(novo_root)
    novo_tree.write(caminho_xml_novo, encoding='utf-8', xml_declaration=True)

    print(f"Novo arquivo XML criado com sucesso: {caminho_xml_novo}")

# Executar a função
if __name__ == "__main__":
    criar_novo_xml(caminho_xml_original, caminho_xml_novo)
