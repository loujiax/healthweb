from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name='vegetables'

urlpatterns = [

    path('', views.VegetableListView.as_view(), name='all'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login_social.html')),

    path('vegetable/<int:pk>', views.VegetableDetailView.as_view(), name='vegetable_detail'),

    path('vegetable/create',

        views.VegetableCreateView.as_view(success_url=reverse_lazy('vegetables:all')), name='vegetable_create'),

    path('vegetable/<int:pk>/update',

        views.VegetableUpdateView.as_view(success_url=reverse_lazy('vegetables:all')), name='vegetable_update'),

    path('vegetable/<int:pk>/delete',

        views.VegetableDeleteView.as_view(success_url=reverse_lazy('vegetables:all')), name='vegetable_delete'),

    path('vegetable_picture/<int:pk>', views.stream_file, name='vegetable_picture'),
]

