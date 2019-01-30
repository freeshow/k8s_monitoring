from django.urls import path
from . import views

app_name = 'alert'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name="vote")
    path('', views.index, name='index'),
    path('node_alert', views.node_alert, name='node_alert'),
    path('pod_alert', views.pod_alert, name='pod_alert')
]