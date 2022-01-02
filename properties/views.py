from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib import messages
import json

# Importamos nuestra clase para hacer request
from .myrequest import MyRequest
# Importamos nuestra clase paginar
from .mypaginator import MyPaginator
# Importamos nuestro form
from .forms import ContactMessage
    
# Create your views here.
@require_http_methods(["GET"])
def index(request):
    """ Vista para mostrar las propiedades """
    page = int(request.GET.get('page')) if request.GET.get('page','').isnumeric() else 1 # Evitar valores no deseados
    limit = 15
    status = 'published'

    url = f'https://api.stagingeb.com/v1/properties?page={page}&limit={limit}&search%5Bstatuses%5D%5B%5D={status}'

    new_request = MyRequest(url, 'GET')
    new_request.make_request()

    if new_request.not_successful():
        return render(request, 'error.html')
    
    if not new_request.response_data['content']:
        return redirect('properties:index')

    context = {
        'properties': new_request.response_data['content'],
        'paginator': MyPaginator(limit, page, new_request.response_data['pagination'], 3, 'properties:index'),
    }

    return render(request, 'properties/index.html', context)

@require_http_methods(["GET"])
def details(request, pk):
    """ Vista para los detalles de las propiedades """
    url = f'https://api.stagingeb.com/v1/properties/{pk}'

    new_request = MyRequest(url, 'GET')
    new_request.make_request()

    if new_request.not_successful(): 
        return render(request, 'error.html')

    # En caso de que el usuario se haya equivocado de mostramos los datos pasados para que los corrija
    form = ContactMessage(request.session['form_data']) if 'form_data' in request.session else ContactMessage()
    context = {
        'property': new_request.response_data,
        'form': form,
    }

    return render(request, 'properties/details.html', context)

@require_http_methods(["POST"])
def message(request, pk):
    """ Crear un nuevo mensaje para la propiedad """
    url = 'https://api.stagingeb.com/v1/contact_requests'

    form_data = request.POST
    form = ContactMessage(form_data)

    if form.is_valid():
        data_to_send = form.cleaned_data
        data_to_send['property_id'] = pk
        data_to_send['source'] = 'luisroberto.com'

        new_request = MyRequest(url, 'POST', json.dumps(data_to_send))
        new_request.make_request()

        if new_request.not_successful(): 
            messages.warning(request, 'Tu mensaje no pudo ser entregado. Inténtalo más tarde.')
            request.session['form_data'] = form_data
        else:
            if 'form_data' in request.session:
                del request.session['form_data']

            messages.success(request, '¡Mensaje enviado exitosamente!')
    else:
        request.session['form_data'] = form_data

    return redirect(reverse('properties:details', args=[pk]))