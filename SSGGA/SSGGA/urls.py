"""SSGGA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp.views import mainpage
from cafeapp.views import createcafe, searchcafe
from account.views import signup, update_profile
from board.views import createpost, board, post, cafemain
from cafe_deco.views import cafe_main, cafe_main_admin, cafe_setting, bulletinboard_page, change_save
from board.views import createpost, board, post, cafemain, deletepost, update
from board.views import createpost, board, post, cafemain, deletepost, update
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage, name="mainpage"),
    path('createcafe/',createcafe, name="createcafe"),
    path('signup/', signup, name="signup"),
    path('update_profile/', update_profile, name="update_profile"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('createpost/', createpost, name="createpost"),
    path('board/', board, name="board"),
    path('cafemain/<int:i_id>', cafemain, name="cafemain"),
    path('post/<int:post_id>', post, name="post"),
    path('deletepost/<int:post_id>/', deletepost, name="deletepost"),
    path('update/<int:post_id>/', update, name="update"),
    path('searchcafe/',searchcafe,name="searchcafe"),
    path('cafe_main/',cafe_main,name="cafe_main"),
    path('cafe_main_admin/',cafe_main_admin,name="cafe_main_admin"),
    path('cafe_setting/',cafe_setting,name="cafe_setting"),
    path('change_save/',change_save,name="change_save"),
    path('bulletinboard_page/',bulletinboard_page,name="bulletinboard_page"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)