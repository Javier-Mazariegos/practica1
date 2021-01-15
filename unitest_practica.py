import unittest
import practica

class TestPractica(unittest.TestCase):
    def test_calcular(self):
        self.assertEqual( practica.calcular(76.21),"O")
        self.assertEqual( practica.calcular(65),"A")
        self.assertEqual( practica.calcular(55.5),"B")
        self.assertEqual( practica.calcular(47.2),"C")
        self.assertEqual( practica.calcular(1.0),"D")
if __name__ == "__main__":
    unittest.main()
