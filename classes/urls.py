from django.urls import path

from . import views

app_name = 'classes'
urlpatterns = [
    path('', views.IndexView, name="home"),
    path('all/', views.AllClassView.as_view(), name="all"),
    path('<int:pk>/', views.DetailView, name="detail"),
    path('create/', views.CreateView, name="create"),
    path('update/<int:pk>', views.UpdateView, name="update"),
    path('delete/<int:pk>', views.DeleteView, name="delete"),
    path('themes/', views.ThemesView, name="themes"),
    path('account/', views.AccountView.as_view(), name="account"),

]
