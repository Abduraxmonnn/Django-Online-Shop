from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),

    path('categroy/', include('apps.categories.urls'))
]
