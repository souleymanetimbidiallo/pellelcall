from django.contrib import admin
from django.utils.text import Truncator

from .models import Profile, Offer, Souscription, Conference

class ProfileAdmin(admin.ModelAdmin):
    list_display   = ('user', 'birthdate', 'address', 'avatar')
    list_filter    = ('address',)
    search_fields  = ('user', 'address')
    fields = ('user', 'birthdate', 'address', 'avatar')

class OfferAdmin(admin.ModelAdmin):
    list_display   = ('title', 'description', 'price')
    list_filter    = ('users', 'price' )
    search_fields  = ('title', 'description')
    fields = ('title', 'description', 'price',)

class SouscriptionAdmin(admin.ModelAdmin):
    list_display   = ('user', 'offer', 'souscriptionDate')
    list_filter    = ('offer',)
    ordering       = ('souscriptionDate', )
    search_fields  = ('user', 'offer')
    fields = ('user', 'offer', 'souscriptionDate')
    
class ConferenceAdmin(admin.ModelAdmin):
    list_display   = ('title', 'beginDate', 'endDate', 'initiator')
    list_filter    = ('title',)
    search_fields  = ('title', 'description')
    fields = ('title', 'description',  'beginDate', 'endDate', 'initiator', 'participants')



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Souscription, SouscriptionAdmin)
admin.site.register(Conference, ConferenceAdmin)