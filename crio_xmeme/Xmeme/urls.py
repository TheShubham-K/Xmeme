from django.urls import path, include
from . import views

urlpatterns = [

    path('memes-form/', views.memes_form, name='memes_insert'), # get and post req. for insert operation.
    path('memes/<int:id>/', views.memes_form, name='memes_update'), # get and post req. for update operation.
    path('memes/', views.memes_List, name='memes_List'), # get req. to retrieve and display all records.
    path('delete/<int:id>/',views.memes_delete,name='memes_delete') # post req. to delete a meme using it's id
]