"""
URL configuration for udbmsp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from udbmsp_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('loginpage/',views.login),
    path('signup/',views.signup),
    path('profview/',views.profview),
    path('gradesheet/<int:val>',views.gradesheet),
    path('csedept/',views.csedept),
    path('biodept/',views.biodept),
    path('envidept/',views.envidept),
    path('archedept/',views.archedept),
    path('materdept/',views.materdept),
    path('mathdept',views.mathdept),
    path('scholdept',views.scholdept),
    path('course/<int:id>',views.course),
    path('adcos',views.adcos),
    path('addquery',views.addquery),
    path('enroll/<int:Pd>',views.enroll),
    path('students',views.students),
    path('faculty',views.faculty),
    path('student/<int:did>',views.studentdid),
    path('try',views.tryi),
    path('upmark/<int:fid>',views.upmark),
    path('contact',views.contact),
    path('blog',views.blog),
    path('adreply',views.adreply),
    path('remove',views.removeu)
    
]
