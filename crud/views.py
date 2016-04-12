from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from crud.models import Person

def index(request):
    people = Person.objects.all()
    response = render(request, 'index.html', {'message':'Welcome!','people':people})
    return response

def insert(request):
    # If this is a post request we insert the person
    if request.method == 'POST':
        p = Person()
        p.name = request.POST.get('name')
        p.phone = request.POST.get('phone')
        p.age = request.POST.get('age')
        p.save()

        people = Person.objects.all()
        response = render(request, 'index.html', {'message':'Data saved successfully!','people':people})
        return response

    else:
        response = render(request, 'insert.html', {})
        return response


def delete(request, person_id):
    p = Person.objects.get(pk=person_id)
    p.delete()
    people = Person.objects.all()
    response = render(request, 'index.html', {'message':'Data deleted successfully!','people':people})
    return response

def edit(request, person_id):
    p = Person.objects.get(pk=person_id)

    if request.method == 'POST':
        p.name = request.POST['name']
        p.phone = request.POST['phone']
        p.age = request.POST['age']
        p.save()

        people = Person.objects.all()
        response = render(request, 'index.html', {'message':'Data edited successfully!','people':people})
        return response

    else:
        response = render(request, 'edit.html', {'person':p})
        return response
