import math

class MyPaginator:
    """ Clase para obtener los datos necesarios para paginar en template """
    def __init__(self, limit, page, data, index_len, url):
        self.current_page = page
        self.next_page = (page + 1) if data['next_page'] else None
        self.last_page = math.ceil(data['total'] / limit)
        self.prev_page = (page - 1) if page > 1 else None
        self.pages = self.get_pages(index_len)
        self.url = url

    def get_pages(self, index_len):
        """ Obtener lista de los índices de las páginas que se mostrarán en el template  """
        if self.last_page - self.current_page > 1:
            return [i for i in range(self.current_page, self.current_page+index_len)]
        else:
            return [i+1 for i in range(self.last_page - index_len, self.last_page)]