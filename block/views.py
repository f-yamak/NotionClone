import json
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EditForm, PostForm
from block.models import *
from django.core.serializers import serialize
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Event, Birthday
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Post, Event, Movie, Birthday
import json

from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Event, Birthday
from datetime import datetime
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, "block/homepage.html")


def index(request):
    return render(request, "block/index.html")


def add_page(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # PostForm'u request.POST verisiyle oluştur
        if form.is_valid():  # Form doğru verilerle doldurulmuşsa
            form.save()  # Formu veritabanına kaydet
            messages.success(request, "Post başarıyla oluşturuldu.")
            return redirect('add_page')  # Yeni bir post eklemek için sayfayı yeniden yükle
        else:
            messages.error(request, "Formda hatalar var. Lütfen tekrar deneyin.")
    else:
        form = PostForm()  # Her iki koşul altında formu tanımla
    
    return render(request, 'add_page.html', {'form': form, 'posts': Post.objects.all()})

def post_detail(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'gorevler.html', {'post': post})



def deleted_posts(request):
    deleted_posts=Post.objects.filter(deleted=True)
    return render(request, 'deleted_posts.html',{'deleted_posts':deleted_posts})
def deleted_birthdays(request):
    deleted_birthdays=Birthday.objects.filter(deleted=True)
    return render(request, 'deleted_birthdays.html',{'deleted_birthdays':deleted_birthdays})
def deleted_events(request):
    deleted_events=Event.objects.filter(deleted=True)
    print(deleted_events)
    return render(request, 'deleted_events.html',{'deleted_events':deleted_events})
def deleted_movies(request):
    deleted_movies=Movie.objects.filter(deleted=True)
    return render(request, '.html',{'deleted_movies':deleted_movies})
    


def inbox(request):
    return render(request, 'inbox.html')

def members_settings(request):
    return render(request, 'members_settings.html')




def calendar(request):
    today = datetime.now()


    # Bu hafta içindeki etkinlikleri al
    events = Event.objects.all()
    closest_event = Event.objects.filter(date__gte=today).order_by('date').first()

    # Bu hafta içindeki doğum günlerini al
    birthdays = Birthday.objects.all()

    # JSON verisini bir sözlük içine yerleştir
    data = {
        'closest_event': closest_event,
        'birthdays': birthdays,
    }
    print(data)
    
    return render(request, 'calendar.html', {'data': data})


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
        
        upcoming_birthdays = Birthday.objects.all().order_by('birth_date')[:6]
        
        # Şablonla birlikte upcoming_birthdays'i gönder
        return render(request, 'birthday.html', {'upcoming_birthdays': upcoming_birthdays})
        
    
    upcoming_birthdays = Birthday.objects.all().order_by('birth_date')[:6]
    return render(request, 'birthday.html',{'upcoming_birthdays': upcoming_birthdays})


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
        existing_movie = Movie.objects.filter(title=title, description=description,deleted=False).exists()
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
        
       
        movies=Movie.objects.filter(deleted=False)
        
        # Şablonla birlikte upcoming_birthdays'i gönder
        return render(request, 'movie.html',{'movies': movies})
        
    else:
        movies=Movie.objects.filter(deleted=False)
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
        
        upcoming_events = Event.objects.filter(deleted=False).order_by('date')[:3]

        
        return render(request, 'event.html', {'upcoming_events': upcoming_events})
        
    upcoming_events = Event.objects.filter(deleted=False).order_by('date')[:3]
    return render(request, 'event.html', {'upcoming_events': upcoming_events})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def delete_post(request, post_id):
    # Post nesnesini al veya 404 hatası gönder
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        # Post nesnesinin deleted alanını True olarak işaretle
        post.deleted = True
        post.save()
        
        
        # Eğer başka bir sayfaya yönlendirme yapmak istiyorsanız, burada onu belirtin
        return redirect('add_page')
    
    # Eğer gönderim yöntemi "GET" ise, sadece sayfayı göster
    return render(request, 'add_page.html')
def delete_birthday(request, birthday_id):
   
    delete_birthday = get_object_or_404(Birthday, id=birthday_id)
    
    if request.method == 'POST':
        delete_birthday.deleted = True
        delete_birthday.save()
        return redirect('birthday')
    return render(request, 'birthday.html')


def delete_event(request, event_id):
    delete_event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        delete_event.deleted = True
        delete_event.save()
        return redirect('event')
    return render(request, 'event.html')


def delete_movie(request, movie_id):   
    delete_movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        delete_movie.deleted = True
        delete_movie.save()
        return redirect('movie')
    
    return render(request, 'movie.html')


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)  # veya başka bir sayfaya yönlendirme
    else:
        form = EditForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})
    
    
def undo_delete_post(request, post_id):
    # Post nesnesini al veya 404 hatası gönder
    post = get_object_or_404(Post, id=post_id)

   
    post.deleted = False
    post.save()

    # İlgili sayfaya yönlendir
    return redirect('deleted_posts')
def undo_delete_movies(request,movie_id):
    # Post nesnesini al veya 404 hatası gönder
    movie = get_object_or_404(Movie, id=movie_id)

    # Post nesnesinin deleted alanını False olarak işaretle
    movie.deleted = False
    movie.save()

    # İlgili sayfaya yönlendir
    return redirect('deleted_movies')
def undo_delete_events(request, event_id):
    # Post nesnesini al veya 404 hatası gönder
    event = get_object_or_404(Post, id=event_id)

    # Post nesnesinin deleted alanını False olarak işaretle
    event.deleted = False
    event.save()

    # İlgili sayfaya yönlendir
    return redirect('deleted_posts')
def undo_delete_birthdays(request, birthday_id):
    # Post nesnesini al veya 404 hatası gönder
    birthday = get_object_or_404(Birthday, id=birthday_id)

    # Post nesnesinin deleted alanını False olarak işaretle
    birthday.deleted = False
    birthday.save()

    # İlgili sayfaya yönlendir
    return redirect('deleted_birthdays')