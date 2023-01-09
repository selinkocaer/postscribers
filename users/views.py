from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)
