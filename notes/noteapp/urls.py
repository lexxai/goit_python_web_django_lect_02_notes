from django.urls import path
from . import views

app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('note/', views.note, name='note'),
    path('tag/', views.tag, name='tag'),
    path('tags/', views.tags, name='tags'),
    path('tag/edit/<int:tag_id>', views.tag_edit, name='tag_edit'),
    path('tag/delete/<int:tag_id>', views.tag_delete, name='tag_delete'),
    path('detail/<int:note_id>', views.detail, name='detail'),
    path('done/<int:note_id>', views.set_done, name='set_done'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
    path('filter/<str:state>', views.main, name='filter'),
    path('filter/tag/<int:tag_id>', views.main, name='filter_tag'),  
]