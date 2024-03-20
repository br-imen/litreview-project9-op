"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import authentication.views
import homepage.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.SignUpView.as_view(), name="signup"),
    path('home/', homepage.views.homepage, name='homepage'),
    path('ticket-upload/', homepage.views.ticket_upload, name='ticket_upload'),
    path('ticket-update/<int:id>',homepage.views.ticket_update, name='ticket_update'),
    path('ticket-delete/<int:id>',homepage.views.ticket_delete, name='ticket_delete'),
    path('review-upload/<int:id>', homepage.views.review_upload, name='review_upload'),

]

        
if settings.DEBUG :
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    