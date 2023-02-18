from django import forms
from concept_map.models import Node, Connection

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['name', 'description']

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['from_node', 'to_node']