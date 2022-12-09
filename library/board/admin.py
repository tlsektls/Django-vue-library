from django.contrib import admin
from .models import Map, OffDay, NewsBoard

# Register your models here.
admin.site.register(Map)
admin.site.register(OffDay)

class NewsBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_title' , 'news_date')
    fields = ['news_title', 'news_content','news_poster', 'news_date']
    
admin.site.register(NewsBoard, NewsBoardAdmin)

