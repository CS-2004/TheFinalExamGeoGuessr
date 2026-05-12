from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/index.html')

# views pulled from exam template
questions = [
    {"country": "France", "capital": "Paris"},
    {"country": "Canada", "capital": "Montreal"},
    {"country": "Brazil", "capital": "Brasilia"},
    {"country": "Monaco", "capital": "Monaco"},
    {"country": "Spain", "capital": "Madrid"},
    {"country": "Singapore", "capital": "Singapore"},
    {"country": "Japan", "capital": "Tokio"},
    {"country": "Israel", "capital": "Jerusalem"},
    {"country": "China", "capital": "Beijing"},
    {"country": "Australia", "capital": "Canberra"},
]