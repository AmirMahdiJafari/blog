from django.contrib import admin
from .models import Tutorial
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):

	fieldsets = [
		("Article/date", {"fields":["Tittle","Date_Published"]}),
		("Contant", {"fields":["Contant"]}),
		]

admin.site.register(Tutorial,TutorialAdmin)