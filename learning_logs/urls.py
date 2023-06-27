from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # pagina inicial.
    path('', views.index, name='index'),  
    # pagina que mostra todos os tópicos.                      
    path('topics/', views.topics, name='topics'),  
    # pagina de detalhes para um único tópico.            
    path('topics/<int:topic_id>/', views.topic, name='topic'), 
    # pagina para dicionar um tópico novo.
    path('new_topic/', views.new_topic, name='new_topic'), 
    # pagina para adicionar uma entrada nova.     
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #TODO edição de um Topic
    #edição de uma entrada.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]