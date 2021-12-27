import unittest
import requests
import json


class Test(unittest.TestCase):
    URL = "http://localhost:5000/"

    def test_1_get_operacion_cuadratica(self):
        response = requests.post(
            self.URL + "operacion/cuadratica",
            data=json.dumps(dict(valor_a=2, valor_b=7, valor_c=2)),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)

    def test_2_get_operacion_fibonacci(self):
        response = requests.post(
            self.URL + "operacion/fibonacci",
            data=json.dumps(dict(valor_n=10)),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    test = Test()
    test.test_1_get_operacion_cuadratica()
    test.test_2_get_operacion_fibonacci()
