from django.conf.urls import include, url



urlpatterns = [
    url(r'^$',
        'core360.views.dashboard',
        name='url_avaliacoes_home'),

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
    
    url(r'^evaluation_respond/(?P<pk_evaluation>\d+)/$',
        'core360.views.evaluation_respond',
        name='url_evaluation_respond'),    

    url(r'^answers_respond/(?P<pk_answer>\d+)/$',
        'core360.views.answers_respond',
        name='url_answers'),

    url(r'^reports/$',
        'core360.views.reports',
        name='url_avaluation_reports'),

    url(r'^reports_boss/$',
        'core360.views.reports_boss',
        name='url_avaluation_reports_boss'),
] 