from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
import requests, math

def make_request(url):
    """ Realizar peticiones a cualquier URL """
    headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}
    method = 'GET'
    try:
        response = requests.request(method, url, headers=headers)
        data = response.json()
        code = response.status_code
    except requests.exceptions.RequestException as e:
        code = data = None
        print(f'\n{e}\n')
        
    return code, data

def status_not_successful(code, data):
    """ Devuelve True, si la petición no fue exitosa e imprime los errores """
    if code != 200:
        if code:
            print(f'\nError code: {code}')
            print(f"Error details: {data['error']}\n")

        return True

def get_paginator(limit, page, data, index_len, url):
    """ Datos de la paginación en templates """
    next_page = (page + 1) if data['next_page'] else None
    last_page = math.ceil(data['total'] / limit)
    prev_page = (page - 1) if page > 1 else None
    pages = [i for i in range(page, page+index_len)] if last_page - page > 1 else [i+1 for i in range(last_page - index_len, last_page)]

    paginator = {
        'current_page': page,
        'next_page': next_page,
        'prev_page': prev_page,
        'last_page': last_page,
        'pages': pages,
        'url': url,
    }

    return paginator
    
# Create your views here.
@require_http_methods(["GET"])
def index(request):
    """ Vista para mostrar las propiedades """
    page = int(request.GET.get('page')) if request.GET.get('page','').isnumeric() else 1 # Evitar valores no deseados
    limit = 15
    status = 'published'

    url = f'https://api.stagingeb.com/v1/properties?page={page}&limit={limit}&search%5Bstatuses%5D%5B%5D={status}'

    code, data = make_request(url)
    
    if status_not_successful(code, data): 
        return render(request, 'error.html')
    
    if not data['content']:
        return redirect('properties:index')

    context = {
        'properties': data['content'],
        'paginator': get_paginator(limit, page, data['pagination'], 3, 'properties:index'),
    }

    return render(request, 'properties/index.html', context)

@require_http_methods(["GET"])
def details(request, pk):
    """ Vista para los detalles de las propiedades """
    url = f'https://api.stagingeb.com/v1/properties/{pk}'

    code, data = make_request(url)

    if status_not_successful(code, data): 
        return render(request, 'error.html')

    context = {
        'property': data,
    }

    return render(request, 'properties/details.html', context)