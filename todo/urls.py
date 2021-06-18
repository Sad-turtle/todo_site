from django.contrib import admin
from django.urls import path
from todosite import views
 
urlpatterns = [
    #####################home_page###########################################
    path('', views.index, name="todosite"),
    ####################give id no. item_id name or item_id=i.id ############
    path('del/<int:item_id>', views.remove, name="del"),
    ########################################################################
    path('admin/', admin.site.urls),
]