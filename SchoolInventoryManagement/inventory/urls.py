# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name="index"),
#     path('inventoryview/', views.inventory_view, name="inventory_view"),
#     path('add_to_reservation/<int:equipment_id>/', views.add_to_reservation, name='add_to_reservation'),
# ]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inventoryview/', views.inventory_view, name="inventory_view"),
    path('add_to_reservation/<int:equipment_id>/', views.add_to_reservation, name="add_to_reservation"),
]