from django.shortcuts import render
from . models import Topic,Entry
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from. forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'home.html')

@login_required
def TopicList(request):
    topicss = Topic.objects.filter(owner=request.user).order_by('-created_at')
    context = {'topicss':topicss}
    return render(request,'topiclist.html',context)

@login_required
def EntryList(request,topic_id):
    try:
        topicss  = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        raise Http404('This topic is not present')


    if request.user !=topicss.owner:
        raise Http404
    entrys   = topicss.entry_set.all()
    context  = {'topicss':topicss, 'entrys':entrys}
    return render(request,'entrylist.html',context)

@login_required
def NewTopic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        newtopics = form.save(commit=False)
        newtopics.owner= request.user
        newtopics.save()
        return HttpResponseRedirect(reverse('cstask:topiclist'))
    context = {'form':form}
    return render(request,'newtopic.html',context)

@login_required
def NewEntry(request,topic_id):
    try:
        topicss = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist:
        raise Http404('topic does not exists')
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        newentrys = form.save(commit=False)
        newentrys.topic = topicss
        newentrys.save()
        return HttpResponseRedirect(reverse('cstask:entrylist', args=[topic_id]))
    context = {'topicss':topicss,'form':form}
    return render(request,'newentry.html',context)

@login_required
def DeleteTopic(request,topic_id):
    topicss=Topic.objects.get(id=topic_id)
    if request.user !=topicss.owner:
        raise Http404
    topicss.delete()
    return HttpResponseRedirect(reverse('cstask:topiclist'))

@login_required
def DeleteEntry(request,entry_id):
    entrys = Entry.objects.get(id=entry_id)
    topicss = entrys.topic
    if request.user !=topicss.owner:
        raise Http404

    entrys.delete()
    return HttpResponseRedirect(reverse('cstask:entrylist', args=[topicss.id]))
