from django.urls import path
from accounts.views import login_user, logout_user, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    
    
]