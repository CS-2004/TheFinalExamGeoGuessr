from django.shortcuts import render
import random

# views pulled from exam template
questions = [
    {"country": "France", "capital": "Paris", "flag": "assets/images/france.png"},
    {"country": "Canada", "capital": "Montreal", "flag": "assets/images/canada.png"},
    {"country": "Brazil", "capital": "Brasilia", "flag": "assets/images/brazil.png"},
    {"country": "Monaco", "capital": "Monaco", "flag": "assets/images/monaco.png"},
    {"country": "Spain", "capital": "Madrid", "flag": "assets/images/spain.png"},
    {"country": "Singapore", "capital": "Singapore", "flag": "assets/images/singapore.png"},
    {"country": "Japan", "capital": "Tokyo", "flag": "assets/images/japan.png"},
    {"country": "Israel", "capital": "Jerusalem", "flag": "assets/images/israel.png"},
    {"country": "China", "capital": "Beijing", "flag": "assets/images/china.png"},
    {"country": "Australia", "capital": "Canberra", "flag": "assets/images/australia.png"},
]

def home(request):

    #first visit if score is not in session, set it to 0
    if "score" not in request.session:
        request.session["score"] = 0

    #if you want to reset the score, you can uncomment this line
    # request.session["score"] = 0

    #buzzer for correct answer
    buzzer = None

    #register user input
    if request.method == "POST":
        user_answer = request.POST.get("answer")
        correct_answer = request.POST.get("capital")

    #proceed to check for user input (turn them lowercase it would be more fair)
    if user_answer.lower().strip() == correct_answer.lower().strip():
        request.session["score"] += 1
        buzzer = "correct"
    else:
        buzzer = "wrong"

    #pick random country for user to guess
    question = random.choice(questions)

    #let the app know in regards to user input and the flags
    context = {
        "country": question["country"],
        "capital": question["capital"],
        "score": request.session["score"],
        "flag": question["flag"],
        "buzzer": buzzer,
    }

    #send everything such as the score, the country, the capital, and the flag to the template
    return render(request, 'mainapp/index.html', context)
