from django.urls import path, re_path
from . import views

app_name = 'noteapp'

urlpatterns = [
    # re_path(r'^(?P<page>\w+)$',views.main, name='main'),
    path('', views.main, name='main'),
    path('note/', views.note, name='note'),
    path('tag/', views.tag, name='tag'),
    path('tags/', views.tags, name='tags'),
    path('tag/edit/<int:tag_id>', views.tag_edit, name='tag_edit'),
    path('tag/delete/<int:tag_id>', views.tag_delete, name='tag_delete'),
    path('detail/<int:note_id>', views.detail, kwargs={'page': 1}, name='detail',),
    path('edit/<int:note_id>', views.note_edit, name='note_edit'),
    path('done/<int:note_id>', views.set_done, name='set_done'),
    path('notdone/<int:note_id>', views.set_notdone, name='set_notdone'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
    path('filter/<str:state>', views.main, name='filter'),
    path('filter/tag/<int:tag_id>', views.main, name='filter_tag'),  
]