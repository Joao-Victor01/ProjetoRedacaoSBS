# tests/test_corretor.py
import unittest
from src.corretor import avaliar_redacao

class TestCorretor(unittest.TestCase):
    
    def test_avaliar_redacao(self):
        redacao = "O concerto foi uma seção incrível."
        nota_final, erros_ortograficos, erros_gramaticais, erros_pln = avaliar_redacao(redacao)
        
        # Verificar se a nota foi calculada corretamente
        self.assertEqual(nota_final, 180)  # Exemplo de penalidade de 20 pontos para erros ortográficos
        self.assertGreater(len(erros_ortograficos), 0)
        self.assertEqual(len(erros_gramaticais), 0)
        self.assertEqual(len(erros_pln), 0)

if __name__ == "__main__":
    unittest.main()
