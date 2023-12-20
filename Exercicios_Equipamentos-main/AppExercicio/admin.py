from django.contrib import admin
from .models import *

class detPosition(admin.ModelAdmin):
    list_display = ('id', 'nameposition')
    list_display_links = ('id', 'nameposition',)
    search_fields = ('nameposition',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin Comments
admin.site.register(Position,detPosition)

#############################################################################################

# Register your models here.
class detUsers(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'nameposition',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin Comments
admin.site.register(Users,detUsers)

#############################################################################################

class detComments(admin.ModelAdmin):
    list_display = ('id', 'description', 'date')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin
admin.site.register(Comments,detComments)

#############################################################################################

#registra as configurações realizadas do model na página de admin Equipment
class detEquipment(admin.ModelAdmin):
    list_display = ('id', 'description', 'image', 'comments')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

#registra as configurações realizadas do model na página de admin
admin.site.register(Equipment,detEquipment)