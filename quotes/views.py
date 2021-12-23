from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote

# Create your views here.
class QuoteListView(ListView):
    model = Quote
    template_name = "home.html"