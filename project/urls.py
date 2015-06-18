from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login',
            {'template_name': 'index.html'}, name='url_login'),

    url(r'^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/',
    )),
    url(r'^accounts/', include('django.contrib.auth.urls')),


    url(r'^accounts/profile/$', 'project.views.dashboard',
    name='url_dashborard'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'registration/logout.html'}, name='url_logout'),

    # Change Password URLs:
    url(r'^accounts/password_change/$', 
        'django.contrib.auth.views.password_change', 
        {'post_change_redirect' : '/accounts/password_change/done/',
        'template_name':'registration/password_change_form.html'}, 
        name="password_change"), 
    
    url(r'^accounts/password_change/done/$', 
        'django.contrib.auth.views.password_change_done'),

    #URL reset
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'project.views.reset_confirm', name='reset_confirm'),
    url(r'^reset/$', 'project.views.reset', name='reset'),
    url(r'^reset_succeful/$', 'project.views.password_confirmation', name='url_reset_suceful'),

    url(r'^admin/', include(admin.site.urls)),
]
