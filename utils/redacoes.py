import uol_redacoes_xml

# Carregar as redações
essays = uol_redacoes_xml.load()

# Verificar quantas redações foram carregadas
print(f"Número de redações carregadas: {len(essays)}")

# Exibir o texto da primeira redação
print("Texto da primeira redação:")
print(essays[0].text)
