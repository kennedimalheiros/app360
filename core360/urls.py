from django.conf.urls import include, url



urlpatterns = [
    url(r'^department/$',
        'core360.views.department_list', 
        name='url_avaliacoes_department'),
    url(r'^new$',
        'core360.views.department_create',
        name='url_department_new'),
    url(r'^edit/(?P<pk>\d+)$',
        'core360.views.department_update',
        name='url_department_edit'),
    url(r'^delete/(?P<pk>\d+)$',
        'core360.views.department_delete',
        name='url_department_delete'),
]