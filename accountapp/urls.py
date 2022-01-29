from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [
    
    path(route = 'login/', view = LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path(route = 'logout/', view = LogoutView.as_view(), name='logout'),

    path(route = 'create/', view = AccountCreateView.as_view(), name='create'),
    path(route = 'detail/<int:pk>', view = AccountDetailView.as_view(), name='detail'),
    path(route = 'update/<int:pk>', view = AccountUpdateView.as_view(), name='update'),
    path(route = 'delete/<int:pk>', view = AccountDeleteView.as_view(), name='delete'),
]