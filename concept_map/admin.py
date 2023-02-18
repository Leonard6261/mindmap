from django.contrib import admin
from concept_map.models import Node, Connection

class ConnectionInline(admin.TabularInline):
    model = Connection
    fk_name = 'from_node'

class NodeAdmin(admin.ModelAdmin):
    inlines = [ConnectionInline]

admin.site.register(Node, NodeAdmin)
admin.site.register(Connection)