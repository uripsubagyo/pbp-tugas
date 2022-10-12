from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import finish_task
from todolist.views import remove_task
from todolist.views import add_task_modal
from todolist.views import show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task' ),
    path('finish-task/<int:pk>', finish_task, name='finish_task' ),
    path('remove-task/<int:pk>', remove_task, name='remove_task' ),
    path('add/', add_task_modal, name='add_task_modal'),
    path('json/', show_json, name='show_json')
]

