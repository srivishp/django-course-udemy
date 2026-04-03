from django.urls import path
from . import views
urlpatterns = [
    # # URL config
    # path(URL, execute this function)
    # ? These are static paths
    # path("january", views.indexJan),
    # path("february", views.indexFeb)

    # > This is a dynamic path
    # * <> holds an identifier
    path("<month>", views.monthly_challenge)

]
