from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from concept_map.models import Node, Connection
from concept_map.forms import NodeForm, ConnectionForm

class NodeListView(ListView):
    model = Node
    template_name = 'concept_map/node_list.html'
    context_object_name = 'nodes'

class NodeDetailView(DetailView):
    model = Node
    template_name = 'concept_map/node_detail.html'
    context_object_name = 'node'

class NodeCreateView(CreateView):
    model = Node
    form_class = NodeForm
    template_name = 'concept_map/node_form.html'

class ConnectionCreateView(CreateView):
    model = Connection
    form_class = ConnectionForm
    template_name = 'concept_map/connection_form.html'

    def form_valid(self, form):
        # Save the form and redirect to the node list view
        response = super().form_valid(form)
        return redirect('concept_map:node_list')