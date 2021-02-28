"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exercises_app.views import LoginView, UserProfileView, ListUsersView, LogoutView, AddUserView, HistoryView, ListBandsView, show_band, BandAddView, AlbumAddView, SongAddView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('list_users/', ListUsersView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('add_user/', AddUserView.as_view()),
    path('history/', HistoryView.as_view()),
    path('user_profile/', UserProfileView.as_view()),
    path('list_bands/', ListBandsView.as_view()),
    path('/show-band/<int:id>/',show_band),
    path('add_band/', BandAddView.as_view()),
    path('add_song/', SongAddView.as_view()),
    path('add_album/', AlbumAddView.as_view()),
]
