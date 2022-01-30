from django.contrib import admin

# Register your models here.

from .models import Academy, Department, NoteUpload, Subject

admin.site.register(NoteUpload)
admin.site.register(Academy)
admin.site.register(Department)
admin.site.register(Subject)