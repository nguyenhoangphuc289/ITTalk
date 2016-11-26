from django.conf.urls import url
from apps.home.views import *

app_name = 'home'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^question/$', question, name='question'),
    url(r'^question/insert/$', question_insert, name='question_insert'),
    url(r'^schedule/$', schedule, name='schedule'),
    url(r'^detail/(?P<pid>[0-9]+)/$', detail, name='detail'),
    url(r'^post/$', post, name='post'),
    url(r'^post/insert/$', post_insert, name='post_insert'),
    url(r'^ajax/feeds/$', ajax_load_more, name='load_more_feeds'),
    url(r'^ajax/delete/$', ajax_delete_post, name='ajax_delete_post'),
    url(r'^ajax/dislike/$', ajax_downvote_post, name='ajax_downvote_post'),
    url(r'^ajax/undislike/$', ajax_undo_downvote_post, name='ajax_undo_downvote_post'),
]
