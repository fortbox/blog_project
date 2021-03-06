from django.contrib import admin
from models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'date_publish',)

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-min.js',
            '/static/js/kindeditor/lang/zh_CN.js',
            '/static/js/kindeditor/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
