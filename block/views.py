from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "block/homepage.html")


def index(request):
    return render(request, "block/index.html")


def anasayfa(request):
    return render(request, 'anasayfa.html')

def add_page(request):
    return render(request, 'add_page.html')

def gorevler(request):
    return render(request, 'gorevler.html')

def search(request):
    return render(request, 'search.html')

def inbox(request):
    return render(request, 'inbox.html')

def members_settings(request):
    return render(request, 'members_settings.html')

def calendar(request):
    return render(request, 'calendar.html')

def templates(request):
    return render(request, 'template.html')

def help_supports(request):
    return render(request, 'help_supports.html')

def trash(request):
    return render(request, 'trash.html')
