from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "January": "This works in January!",
    "February": "This works in February!",
    "March": "This works in March!",
    "April": "This works in April!",
    "May": "This works in May!",
    "June": "This works in June!",
    "July": "This works in July!",
    "August": "This works in August!",
    "September": "This works in September!",
    "October": "This works in October!",
    "November": "This works in November!",
    "December": "This works in December!"
}

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
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    # f-string usage
    return HttpResponseRedirect(f"/challenges/{redirect_month}")
  #  return HttpResponse(f"This works for month number {month}!")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.capitalize()]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
