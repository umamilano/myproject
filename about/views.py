#views app about
from django.shortcuts import render

# Create your views here.
content = {
    'title':'My Portfolio'
}
def index(request):
    return render(request,'about/index.html',content)
