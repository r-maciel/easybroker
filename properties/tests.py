from django.http import response
from django.test import TestCase
from django.urls import reverse
from .myrequest import MyRequest
from .mypaginator import MyPaginator
from . import views
import json

# Create your tests here.
class TestMyPaginator(TestCase):
    """ Testear clase MyPaginator """
    paginator = MyPaginator(15, 1, {'total': 500, 'next_page': True}, 4, 'alguna.url')

    def test_get_paginator(self):
        """ Testear que los datos del paginator generado sean los correctos """
        self.assertEqual(self.paginator.current_page, 1)
        self.assertEqual(self.paginator.next_page, 2)
        self.assertEqual(self.paginator.last_page, 34)
        self.assertEqual(self.paginator.prev_page, None)
        self.assertEqual(self.paginator.pages, [1,2,3,4])
        self.assertEqual(self.paginator.url, 'alguna.url')


class TestMyRequest(TestCase):
    """ Testear clase MyRequest """

    def test_bad_url(self):
        """ Cuando la URL no es correcta y no se logra realizar el request, por lo tanto el código está vacío """
        new_request = MyRequest('https://api.hhhh.com/v1/properties/', 'GET')
        new_request.make_request()

        self.assertEqual(new_request.code, None)
        self.assertTrue(new_request.not_successful())

    def test_request_success_200(self):
        """ Cuando el request se realiza de manera exitosa y retorna código 200 """
        headers = {'accept': 'application/json', 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}
        new_request = MyRequest('https://api.stagingeb.com/v1/properties/', 'GET', headers)
        new_request.make_request()

        self.assertEqual(new_request.code, 200)
        self.assertFalse(new_request.not_successful())

    def test_request_error_code(self):
        """ Cuando el request se realiza pero hay algún error y la API retorna un código diferente a 200  """
        headers = {'accept': 'application/json', 'X-Authorization': 'l7u502pv46ba3ppgvj5y2aad50lb9'}
        new_request = MyRequest('https://api.stagingeb.com/v1/properties/45', 'GET', headers)
        new_request.make_request()

        self.assertNotEqual(new_request.code, 200)
        self.assertNotEqual(new_request.code, None)
        self.assertTrue(new_request.not_successful())


class TestViews(TestCase):
    """ Testear las vistas """

    def test_index_view(self):
        """ El status es 200 cuando la conexión a la página que lista las propiedades es correcta """
        response = self.client.get(reverse('properties:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_details_view(self):
        """ El status es 200 cuando la conexión a la página que muestra los detalles de una propiedad """
        response = self.client.get(reverse('properties:details', args=['EB-B5519']))
        self.assertEqual(response.status_code, 200)


class TestEasyBrokerAPI(TestCase):
    """ Tests para /properties endpoint """
    
    headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}

    def test_properties_code_200(self):
        """ Cuando se el request es exitoso y se trae las propiedades"""
        new_request = MyRequest('https://api.stagingeb.com/v1/properties', 'GET', self.headers)
        new_request.make_request()

        self.assertEqual(new_request.code, 200)
        self.assertFalse(new_request.not_successful())

    def test_properties_code_401(self):
        """ Cuando la api key es invalida o no se proporciono """
        new_request = MyRequest('https://api.stagingeb.com/v1/properties', 'GET')
        new_request.make_request()

        self.assertEqual(new_request.code, 401)
        self.assertTrue(new_request.not_successful())

    
class TestPropertyDetails(TestCase):
    """ Tests para /properties/{ID} endpoint """
    
    headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}

    def test_properties_details_code_200(self):
        """ Cuando se encuentra la propiedad socilictada y el request es exitoso """
        new_request = MyRequest('https://api.stagingeb.com/v1/properties/EB-C0119', 'GET', self.headers)
        new_request.make_request()

        self.assertEqual(new_request.code, 200)
        self.assertFalse(new_request.not_successful())

    def test_properties_details_code_401(self):
        """ Cuando la api key es invalida o no se proporciono """
        new_request = MyRequest('https://api.stagingeb.com/v1/properties/EB-C0119', 'GET')
        new_request.make_request()

        self.assertEqual(new_request.code, 401)
        self.assertTrue(new_request.not_successful())

    def test_properties_details_code_404(self):
        """ Cuando no se encuentra la propiedad solicitada """
        new_request = MyRequest('https://api.stagingeb.com/v1/properties/EB-XXX', 'GET', self.headers)
        new_request.make_request()

        self.assertEqual(new_request.code, 404)
        self.assertTrue(new_request.not_successful())


class TestContactRequest(TestCase):
    """ Testear /contact_request [POST] endpoint """
    headers = {'accept': 'application/json', 'content-type': 'application/json', 'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'}
    contact_data = json.dumps({
        "name": "John Smith",
        "phone": "5559090909",
        "email": "mail@example.com",
        "property_id": "EB-C0119",
        "message": "I'm interested in this property. Please contact me.",
        "source": "mydomain.com"
    })

    def test_contact_request_code_200(self):
        """ Cuando se encuentra la propiedad socilictada y el request es exitoso """
        new_request = MyRequest('https://api.stagingeb.com/v1/contact_requests', 'POST', self.headers, self.contact_data)
        new_request.make_request()

        self.assertEqual(new_request.code, 200)
        self.assertFalse(new_request.not_successful())

    def test_contact_request_code_401(self):
        """ Cuando la api key es invalida o no se proporciono """
        new_request = MyRequest('https://api.stagingeb.com/v1/contact_requests', 'POST', request_data=self.contact_data)
        new_request.make_request()

        self.assertEqual(new_request.code, 401)
        self.assertTrue(new_request.not_successful())

    def test_contact_request_code_404(self):
        """ Cuando no se encuentra la propiedad solicitada """
        contact_data = json.dumps({
            "name": "John Smith",
            "phone": "5559090909",
            "email": "mail@example.com",
            "property_id": "EB-XXXX",
            "message": "I'm interested in this property. Please contact me.",
            "source": "mydomain.com"
        })
        new_request = MyRequest('https://api.stagingeb.com/v1/contact_requests', 'POST', self.headers, contact_data)
        new_request.make_request()

        self.assertEqual(new_request.code, 404)
        self.assertTrue(new_request.not_successful())
    
    def test_contact_request_code_422(self):
        """ Cuando no se proporciona un nombre, email o número de teléfono"""
        contact_data = json.dumps({
            "property_id": "EB-C0119",
            "message": "I'm interested in this property. Please contact me.",
            "source": "mydomain.com"
        })
        new_request = MyRequest('https://api.stagingeb.com/v1/contact_requests', 'POST', self.headers, contact_data)
        new_request.make_request()

        self.assertEqual(new_request.code, 422)
        self.assertTrue(new_request.not_successful())