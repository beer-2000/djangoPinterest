from django.urls import path
from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path(route = 'hello_world/', view = hello_world, name='hello_world'),

    path(route = 'create/', view = AccountCreateView.as_view(), name='create'),
]