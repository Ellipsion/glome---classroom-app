from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import request, HttpResponseRedirect, response
from django.template import context
from django.views import generic
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse
from crispy_forms.utils import render_crispy_form

from django.contrib.auth.models import User
from .models import Classes
from .forms import CreateForm

DayOfTheWeek = [
    0,
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

Month = [
    0,
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]


class Today:
    month = Month[timezone.now().month]
    day = timezone.now().day
    year = timezone.now().year
    weekday = DayOfTheWeek[timezone.now().isoweekday()]

    def str_day(self):
        day = str(self.day)
        if len(day) == 1:
            return '0' + str(self.day)
        else:
            return str(self.day)


def IndexView(request):
    user = request.user
    template_name = 'classes/index.html'

    today = Today()

    all_class_list = user.classes.all()
    recent_class_list = user.classes.order_by('-class_pub_datetime')[:5]
    print(recent_class_list)

    day_today = timezone.now().isoweekday()
    active_class_list = []
    for class1 in user.classes.all():
        day_list = []

        if (class1.Monday == True) or (class1.Alldays == True):
            day_list.append(1)
        if (class1.Tuesday == True) or (class1.Alldays == True):
            day_list.append(2)
        if (class1.Wednesday == True) or (class1.Alldays == True):
            day_list.append(3)
        if (class1.Thursday == True) or (class1.Alldays == True):
            day_list.append(4)
        if (class1.Friday == True) or (class1.Alldays == True):
            day_list.append(5)
        if (class1.Saturday == True) or (class1.Alldays == True):
            day_list.append(6)
        if (class1.Sunday == True) or (class1.Alldays == True):
            day_list.append(7)

        for day in day_list:
            if day_today == day:
                active_class_list.append(class1)

    context = {
        'recent_classes': recent_class_list,
        'active_class_list': active_class_list,
        'all_class_list': all_class_list,
        'today': today,
        'time': timezone.now().time,
    }

    return render(request, template_name, context)


class AllClassView(generic.ListView):
    template_name = 'classes/all.html'
    context_object_name = 'all_classes'

    def get_queryset(self):
        return self.request.user.classes.all()


# class DetailView(generic.DetailView):
#     template_name = 'classes/detail.html'
#     model = Classes
def DetailView(request, pk):
    template_name = 'classes/detail.html'
    user = request.user
    selected_class = user.classes.get(pk=pk)

    return render(request, template_name, {'selected_class': selected_class})


def CreateView(request):
    template_name = 'classes/create.html'
    previous_url = request.META.get('HTTP_REFERER')
    mainForm = CreateForm()
    fields = list(mainForm)

    if request.method == 'POST':
        mainForm = CreateForm(request.POST)
        mainForm.instance.user = request.user
        if mainForm.is_valid():
            mainForm.save()

            return redirect('/classes/')

    context = {'main_form': mainForm,
               'form_fields': fields,
               'previous_url': previous_url}

    return render(request, template_name, context)


def UpdateView(request, pk):
    template_name = 'classes/create.html'
    user = request.user
    selected_class = user.classes.get(pk=pk)
    previous_url = request.META.get('HTTP_REFERER')
    mainForm = CreateForm(instance=selected_class)
    fields = list(mainForm)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=selected_class)
        if form.is_valid():

            form.save()
            # return HttpResponseRedirect(reverse('classes:detail', args=(pk,)))
            return redirect(reverse('classes:detail', args=(pk,)))

    context = {'main_form': mainForm,
               'form_fields': fields,
               'previous_url': previous_url}

    return render(request, template_name, context)


def key_in_string(key, string):
    if key in string:
        return True
    else:
        return False


def DeleteView(request, pk):
    template_name = 'classes/delete.html'
    previous_url = request.META.get('HTTP_REFERER')

    user = request.user
    selected_class = user.classes.get(pk=pk)

    if request.method == 'POST':
        selected_class.delete()
        return redirect('/classes/all')

    return render(request, template_name, {'class': selected_class, 'previous_url': previous_url, })


class AccountView(generic.ListView):
    template_name = 'classes/account.html'
    context_object_name = 'user'

    def get_queryset(self):
        return self.request.user


def ThemesView(request):
    template_name = 'classes/themes.html'

    context = {'user': request.user.classes.all()}
    return render(request, template_name, context)


# def indexview(request):
#     template_name = 'classes/index.html'

#     day_today_int = timezone.now().isoweekday()

#     class_list = []
#     for class1 in Classes.objects.all():
#         for day in class1.day_set.all():
#             if day_today_int == day.class_day:
#                 class_list.append(class1)

    # return render(request, template_name, {'class_list': class_list, })
