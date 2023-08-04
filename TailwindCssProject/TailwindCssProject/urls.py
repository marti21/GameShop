"""
URL configuration for TailwindCssProject project.

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
from TailwindCssGameApp.views import get_trend_games, loginUser, show_error_404, get_game, game_list
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('i18n/', set_language, name='set_language'),

    path('login/', loginUser, name='login'),
    path('', get_trend_games, name='trends'),
    path('game/<str:gameName>', get_game, name='game'),
    path('games/', game_list, name='games')
)

handler404 = show_error_404