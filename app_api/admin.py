from django.contrib import admin
from app_api.models import Post, Tag, Category, RareUser
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(RareUser)