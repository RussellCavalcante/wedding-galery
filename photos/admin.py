from django.contrib import admin
from .forms import ComentarioObrigatorio
from . import models


class ComentarioInline(admin.TabularInline):
    model = models.CommentPhotos
    formset = ComentarioObrigatorio
    min_num = 1
    extra = 0
    can_delete = True


class PhotosAdmin(admin.ModelAdmin):
    list_display = ['imagem', 'nome',
                    'usuario_dono', 'visivel']
    inlines = [
        ComentarioInline
    ]


admin.site.register(models.Photos, PhotosAdmin)
admin.site.register(models.CommentPhotos)
