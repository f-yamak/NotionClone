from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render

from block.models import *

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

def birthday(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        birth_date = request.POST.get('birth_date')

        birthday = Birthday.objects.create(
            person_name=person_name,
            birth_date=birth_date,
        )

        birthday.save()
        
        today = timezone.now().date()
        upcoming_birthdays = Birthday.objects.filter(birth_date__gte=today).order_by('birth_date')[:3]
        print(upcoming_birthdays)

        messages.success(request, "Randevu başarıyla oluşturuldu.")
        
        # Şablonla birlikte upcoming_birthdays'i gönder
        return render(request, 'birthday.html', {'upcoming_birthdays': upcoming_birthdays})
        
    else:
        return render(request, 'birthday.html')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        movie = Movie.objects.create(
            title=title,
            description=description,
            
        )
        print("2")
        print(movie)
        existing_movie = Movie.objects.filter(title=title, description=description).exists()
        if existing_movie:
            messages.warning(request, "Bu film zaten eklenmiş.")
        else:
            movie = Movie.objects.create(
                title=title,
                description=description,
            )
            movie.save()
            messages.success(request, "Film başarıyla eklendi.")

        movie.save()
        
       
        movies=Movie.objects.all()
        messages.success(request, "Randevu başarıyla oluşturuldu.",{'movies': movies})
        print("3")
        
        # Şablonla birlikte upcoming_birthdays'i gönder
        return render(request, 'movie.html')
        
    else:
        movies=Movie.objects.all()
        return render(request, 'movie.html',{'movies': movies})

def movie(request):
   
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        movie = Movie.objects.create(
            title=title,
            description=description,
            
        )
        print("2")
        print(movie)
        existing_movie = Movie.objects.filter(title=title, description=description).exists()
        if existing_movie:
            messages.warning(request, "Bu film zaten eklenmiş.")
        else:
            movie = Movie.objects.create(
                title=title,
                description=description,
            )
            movie.save()
            messages.success(request, "Film başarıyla eklendi.")

        movie.save()
        
       
        movies=Movie.objects.all()
        messages.success(request, "Randevu başarıyla oluşturuldu.",{'movies': movies})
        print("3")
        
        # Şablonla birlikte upcoming_birthdays'i gönder
        return render(request, 'movie.html')
        
    else:
        movies=Movie.objects.all()
        return render(request, 'movie.html',{'movies': movies})

def shopping(request):
    return render(request, 'shopping.html')
def event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time =request.POST.get('time')

        event = Event.objects.create(
            name=name,
            date=date,
            time=time
        )

        event.save()
        
        today = timezone.now().date()
        upcoming_events = Event.objects.filter(date__gte=today).order_by('date')[:3]
        print(upcoming_events)

        messages.success(request, "Randevu başarıyla oluşturuldu.")
        
        # Şablonla birlikte upcoming_birthdays'i gönder
        return render(request, 'event.html', {'upcoming_events': upcoming_events})
        
    else:
        return render(request, 'event.html')