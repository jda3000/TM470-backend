from django.contrib import admin

from common.models import Comment, Like, File

admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(File)
