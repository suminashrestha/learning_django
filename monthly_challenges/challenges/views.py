from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "No junk food for a month!",
    "february": "Walk for atleast 20 minutes",
    "march": "Learn Django",
    "april": "Do exercises",
    "may": "go to gym",
    "june": "do yoga",
    "july": "take rest",
    "august": "travel as much as you can",
    "september": "learn more programming languages",
    "october": "focus on your studies",
    "november": "No more than 5 hrs of screen time",
    "december": "focus on self skills"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!!!!")
