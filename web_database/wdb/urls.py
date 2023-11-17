from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('<slug:model_type>/', tables, name='list'),
    path('<slug:model_type>/update/<int:model_id>/', update, name='update'),
    path('<slug:model_type>/delete/<int:model_id>/', delete, name='delete'),
    path('posts/procedure_e_by_p', employee_by_post, name='prep'),
]
