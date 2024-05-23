from django.contrib import admin
from .models import Post, Event, Movie, Shopping, Birthday, BlogPost

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Movie)
admin.site.register(Shopping)
admin.site.register(Birthday)
admin.site.register(BlogPost)
