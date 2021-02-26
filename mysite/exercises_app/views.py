from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import FormView
from .models import Band
from .forms import AddUserForm, LoginForm, UserProfileForm, HistoryModelForm


# Create your views here.
class ListUsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'list_users.html', {'users': users})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'user_profile.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'],
                                     email=form.cleaned_data['email'],
                                     first_name=form.cleaned_data['first_name'],
                                     last_name=form.cleaned_data['last_name'])
            return redirect('../login/')
        else:
            return render(request, 'user_profile.html', {'form': form})

class UserProfileView(View):
    def get(self, request):
        form = UserProfileForm()
        return render(request, 'user_profile.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            return render(request, 'user_profile.html', {'form': form, 'status': 'ok'})
        else:
            return render(request, 'user_profile.html', {'form': form, 'status': 'error'})

class HistoryView(FormView):
    template_name = 'history.html'
    form_class = HistoryModelForm
    success_url = '/'

    def form_valid(self, form):
        update_history = form.save()
        return super().form_valid(form)

def show_band(request, id):
    band = Band.objects.get(id=id)
    albums = band.album_set.all()
    name = band.name
    genre = band.genre
    year = band.year
    still_active = band.still_active
    history = band.history
    return render(request, 'bands.html', {'name': name, 'genre': genre,
                  'release_year': year, 'still_active': still_active, 'id': band.id,
                                          'albums': albums, 'history': history})

class ListBandsView(View):
    def get(self, request):
        bands = Band.objects.all()
        return render(request, 'list_bands.html', {'bands': bands})

