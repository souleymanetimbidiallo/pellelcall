# Personnalisation de l'administration du site
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Offer, Souscription, Conference

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Informations complémentaires"
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_birthdate')
    list_select_related = ('profile', )

    def get_birthdate(self, instance):
        return instance.profile.birthdate
    get_birthdate.short_description = "Date de naissance"
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

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


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Souscription, SouscriptionAdmin)
admin.site.register(Conference, ConferenceAdmin)