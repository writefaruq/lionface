from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin

# Profile has three main objects: Place, User and Event

class Place(models.Model):
	''' holds a generic place information with unique zipcode '''
	name = models.CharField(_('Name'), max_length = 50, blank = True)
	street_line1 = models.CharField(_('Address 1'), max_length = 100, blank = True)
	street_line2 = models.CharField(_('Address 2'), max_length = 100, blank = True)
	zipcode = models.CharField(_('ZIP code'), max_length = 10, primary_key = True)
	city = models.CharField(_('City'), max_length = 100, blank = True)
	state = models.CharField(_('State'), max_length = 100, blank = True)
	# French specifics fields
	#cedex = models.CharField(_('CEDEX'), max_length = 100, blank = True)    
	postal_box = models.CharField(_('Postal box'), max_length = 20, blank = True)
	country = models.CharField(_('Country'), max_length = 100, blank = True)

class Event(models.Model):
	''' holds an event created by user associated with a Place '''	
	name = models.CharField(max_length=50)
	venue = models.CharField(max_length=50)
	desc = models.TextField()
	start_time = models.DateTimeField()
	end_time =  models.DateTimeField()	
	location = models.ForeignKey(Place)
	
class User(models.Model):
	''' represents individual, business or non-profit  associted with a Place'''
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	birthday = models.DateTimeField()
	location = models.ForeignKey(Place)

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('zipcode', 'name')
	
class EventAdmin(admin.ModelAdmin):
	list_display = ('location', 'name')
	
class UserAdmin(admin.ModelAdmin):
	list_display = ('location', 'location')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(User, UserAdmin)
