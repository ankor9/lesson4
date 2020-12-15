from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def test_json_data(request):
    resp_data = {}
    resp_data['name'] = 'Anastasia Pomozova'
    #resp_data['phone_book'] = []
    book = []
    book.append({"name" : "Vasya", "phone" : 6540044})
    book.append({"name": "Masha", "phone": 6540043})
    book.append({"name": "Kostya", "phone": 6540042})
    resp_data['phone_book'] = book
    return JsonResponse(resp_data)