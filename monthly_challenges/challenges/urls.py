from django.urls import path
from . import views
urlpatterns = [
    # # URL config
    # path(URL, execute this function)
    # ? These are static paths
    # path("january", views.indexJan),
    # path("february", views.indexFeb)
    path("", views.index),  # /challenges/

    # > This is a dynamic path
    # * <> holds an identifier within it, and the type of value it should be (str, int, etc.)
    path("<int:month>", views.monthly_challenge_by_number),
    # Creating a named URL
    path("<str:month>", views.monthly_challenge, name="monthly_challenge")

]
