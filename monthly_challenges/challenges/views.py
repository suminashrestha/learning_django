from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "No junk food for a month!"
    elif month == 'february':
        challenge_text = "Walk for atleast 20 minutes"
    elif month == 'march':
        challenge_text = "Learn Django"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
