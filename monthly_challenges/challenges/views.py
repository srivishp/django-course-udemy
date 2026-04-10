from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# this import is used to load the template and render it with the context
# from django.template.loader import render_to_string

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

def index(request):

    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

# > This is a dynamic view/captured value
# * month is the identifier


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    # Reverse function takes the name of the URL and gives the actual URL back
    redirect_path = reverse("monthly_challenge", args=[
                            redirect_month])  # /challenge/january
    # f-string usage
    # return HttpResponseRedirect(f"/challenges/{redirect_month}")
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.capitalize()]
        # We are using render instead of render_to_string and HttpResponse because render takes care of loading the template, rendering it with the context and returning the HttpResponse all in one step.
        return render(request, "challenges/challenge.html", {
            # > These are the context variables that we are passing to the template.
            # We can use these variables in the template to display the challenge text and the month name.
            "title": month + "'s Challenge",
            "text": challenge_text,
            "month_name": month
        })
        # Returning HTML instead of just text
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
