from django.urls import path

from . import views

app_name = "Poll"
urlpatterns = [
    # /poll/
    path('', views.IndexView.as_view(), name='index'),
    # /poll/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /poll/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # /poll/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')

]
