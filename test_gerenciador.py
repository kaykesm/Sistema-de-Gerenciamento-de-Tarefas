import unittest
from src.gerenciador import criar_tarefa, listar_tarefas

class TestGerenciador(unittest.TestCase):
    def test_criar_tarefa(self):
        criar_tarefa("Estudar GitHub Actions")
        tarefas = listar_tarefas()
        self.assertGreater(len(tarefas), 0)

if __name__ == '__main__':
    unittest.main()
