from django.contrib import admin
from django.urls import path,include
from login import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("",views.homepage,name='homepage'),
    path("login/",views.loginapp,name="login"),
    path("signup/",views.signup,name="signup"),
    path("review/",views.review_ins,name='review'),
    path("reviews-customer/",views.veiwsection,name='views'),
    path("logout/",views.logout_view,name='logout'),
    path("blog/",views.Blog,name='blog'),
    path("blogspot/<str:slug>",views.Blogspot,name="blogspot"),
    path("rooms/",views.chat_room_chat,name="chat"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('chat/',views.chat_room_sel,name='chatroom'),  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
