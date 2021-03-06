from django.contrib import admin
from .models import Poll, Choice, Vote, Post, Photo

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)

class PhotoInline(admin.TabularInline):
    model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

# Register your models here.
admin.site.register(Post, PostAdmin)

