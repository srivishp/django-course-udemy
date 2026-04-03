from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# ? These are static views/functions
# def indexJan(request):
#     # Function takes a request and gives a response
#     return HttpResponse("This works in January!")


# def indexFeb(request):
#     # Function takes a request and gives a response
#     return HttpResponse("This works in February!")


# > This is a dynamic view/captured value
# * month is the identifier
def monthly_challenge(request, month):
    if month == "january":
        challenge_text = "This works in January!"
    elif month == "february":
        challenge_text = "This works in February"
    else:
        return HttpResponse("This month is not supported!")

    return HttpResponse(challenge_text)
