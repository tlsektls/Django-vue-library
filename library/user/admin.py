from django.contrib import admin
from user.models import User
 
 
class UserAdmin(admin.ModelAdmin):
    # 내가 출력하고 싶은 제목명인 필드명 user_id과 name 을 표시한다.
    list_display = ('user_id', 'name')
 
 
admin.site.register(User, UserAdmin)