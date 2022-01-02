import requests

class MyRequest:
    """ Clase para realizar requests JSON"""

    def __init__(self, url, method, request_data={}):
        self.url = url
        self.method = method
        self.request_data = request_data
        self.headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}
    
    def make_request(self):
        """ Realizar peticiones a cualquier URL """
        try:
            response = requests.request(self.method, self.url, headers=self.headers, data=self.request_data)
            self.response_data = response.json()
            self.code = response.status_code
        except requests.exceptions.RequestException as e:
            self.code = self.response_data = None
            print(f'\n{e}\n')

    def not_successful(self):
        """ Devuelve True, si la petición no fue exitosa e imprime los errores """
        if self.code != 200:
            if self.code:
                print(f'\nError code: {self.code}')
                print(f"Error details: {self.response_data['error']}\n")

            return True