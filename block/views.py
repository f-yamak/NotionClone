from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "block/homepage.html")


def index(request):
    return render(request, "block/index.html")