from django.contrib import admin
from .models import Question , Answer ,Qcomment , Acomment

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Qcomment)
admin.site.register(Acomment)