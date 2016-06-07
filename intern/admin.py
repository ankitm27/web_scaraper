from django.contrib import admin
from .models import Profile,Domain,Database
# Register your models here.

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["username", "firstname", "lastname", "gender","dob"]
	class Meta:
		model = Profile

class DomainModelAdmin(admin.ModelAdmin):
	list_display = ["username", "domain"]
	class Meta:
		model = Domain

class DatabaseModelAdmin(admin.ModelAdmin):
	list_display = ["domain", "categary", "company"]
	class Meta:
		model = Database

admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Domain, DomainModelAdmin)
admin.site.register(Database, DatabaseModelAdmin)

