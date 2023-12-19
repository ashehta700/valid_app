from django.urls import path , include
from printPreview import views



urlpatterns = [
    path('accounts/signup',views.signup,name='signup'),
    path('', views.index , name = "index"),
    path('<int:id>', views.print_label , name = "print"),
    path('replay/<int:id>', views.replay , name = "replay"),
    path('download<path:attachment_display_name>', views.download_file, name='download_file'),

] 