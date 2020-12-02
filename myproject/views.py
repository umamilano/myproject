#views myproject
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


file_index = 'index.html'
if settings.MAINTENANCE:
    file_index = 'under_cont.html'
else:
    file_index = 'index.html'


def index(request):
    content = {
        'judul':'My Portfolio',
        'nav': [
            ['/','Home'],
            ['/about','About']
        ]
    }
    return render(request,file_index,content)
