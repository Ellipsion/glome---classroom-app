from django.shortcuts import render, redirect

from .forms import RegisterForm


def RegisterView(request):
    template_name = 'users/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()

    return render(request, template_name, {'form': form})


def IndexView(request):
    template_name = 'users/index.html'

    return render(request, template_name)
