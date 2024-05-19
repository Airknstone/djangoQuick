from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# Static urls
# def janurary(request):
#     return HttpResponse("This janurary!")

# def february(request):
#     return HttpResponse("This february!")

monthly_challenges = {
    "january": "Janurary",
    "february": "February",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(
        monthly_challenges.keys()
    )  # Convert the object to a list and use the key to find the index
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


# This is a dynamic URL example
# instead of making 12 views, for 12 months make one that changes depending on the month
# month comes from the urls pattern <month>
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )

    except:  # pylint: disable=bare-except
        raise Http404()
