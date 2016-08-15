from django.contrib import admin
from app01.models import Bbs, Category, BBS_user, User_Comment

class BbsAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'content','created_at','ranking','author',)
    search_fields = ('author', 'title',)
    list_filter = ('created_at',)
admin.site.register(Bbs,BbsAdmin)
admin.site.register(Category)
admin.site.register(BBS_user)
admin.site.register(User_Comment)
