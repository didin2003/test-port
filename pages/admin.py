from django.contrib import admin
from .models import About, Skill, Project, Experience, Education, ContactMessage

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ContactMessage)
