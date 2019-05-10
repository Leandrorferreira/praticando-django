from django.shortcuts import render
from roles.models import Role

# Create your views here.
def home(request):
    return render(request, 'index.html')

def lista_roles(request):
    roles = Role.objects.all()
    context = {'roles' : roles}
    return render(request, 'lista_roles', context)