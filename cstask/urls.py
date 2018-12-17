from django.urls import path
from . import views
app_name='cstask'
urlpatterns=[
    path('',views.index,name='home'),
    path('topiclist/',views.TopicList,name='topiclist'),
    path('topiclist/<int:topic_id>',views.EntryList,name='entrylist'),
    path('newtopic/',views.NewTopic,name='newtopic'),
    path('newentry/<int:topic_id>',views.NewEntry,name='newentry'),
    path('deletetopic/<int:topic_id>',views.DeleteTopic,name='deletetopic'),
    path('deleteentry/<int:entry_id>',views.DeleteEntry,name='deleteentry'),



]
