from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('board/',  views.board, name='board'),
    path('board/<int:pk>', views.posting, name='posting'),
    path('board/write/', views.write_posting, name='write'),

]
