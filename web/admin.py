from django.contrib import admin
from .models import Tutorial ,TutorialSeries ,TutorialCategory
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):

	fieldsets = [
		("Article/date", {"fields":["Tittle","Date_Published"]}),
		("Contant", {"fields":["Contant"]}),
		("Tutorial URL", {"fields":["Tutorial_slug"]}),
		("Tutorial Series", {"fields":["Tutorial_Series"]})

		]

admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)