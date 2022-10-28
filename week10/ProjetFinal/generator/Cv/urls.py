from os import name

from django.conf.urls.static import static
from django.urls import path,include
from Cv.views import  generer, download, index, verification
from accueil.views import home
from QrCode.views import demo,tel,sms,email,wiffi,accueil
from django.conf import settings

from accueil.views import home
from eqrApp.views import employee_list, manage_employee, save_employee, view_card, view_details, view_scanner, \
    delete_employee, homee

urlpatterns = [

    path('', home, name="home"),
    path('index', index, name="index"),
path('demo', demo, name='demo'),
path('tel', tel, name='tel'),
path('sms', sms, name='sms'),
path('email', email, name='email'),
path('wiffi', wiffi, name='wiffi'),
path('accueil', accueil, name='acceuil'),
path('base', home, name='base'),
    path('verification', verification, name="verification"),
    path('<int:id>', generer, name="generer"),
    path('download', download, name="download"),
path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    #path('',views.home),
    #path('login',views.login_page,name='login-page'),
    #path('user_login',views.login_user,name='login-user'),
    path('h',homee,name='home-page'),
    #path('logout',views.logout_user,name='logout'),
    path('employee_list',employee_list,name='employee-page'),
    path('add_employee',manage_employee,name='add-employee'),
    path('edit_employee/<int:pk>',manage_employee,name='edit-employee'),
    path('save_employee',save_employee,name='save-employee'),
    path('view_card/<int:pk>',view_card,name='view-card'),
    path('view_details/<str:code>',view_details,name='view-details'),
    path('view_details',view_details,name='scanned-code'),
    path('scanner',view_scanner,name='view-scanner'),
    path('delete_employee/<int:pk>',delete_employee,name='delete-employee'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)