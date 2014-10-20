from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from datetime import datetime

from notes.models import Note

def index(request):
	note_list = Note.objects.all()
	template = loader.get_template('notes/index.html')
	context = RequestContext(request, {
		'note_list': note_list,
	})
	return HttpResponse(template.render(context))

def new(request):
	if request.method == 'POST':
		note = Note()
		note.text = request.POST.get('text', '')
		note.user = User.objects.get(pk=request.POST.get('user', ''))
		note.date = datetime.now()
		note.save()
		return redirect('/notes/')
	users = User.objects.all()
	template = loader.get_template('notes/new.html')
	context = RequestContext(request, {
		'users': users
	})
	return HttpResponse(template.render(context))

def show(request, note_id):
	return HttpResponse("TODO show note: %s" % note_id)

def edit(request, note_id):
	note = Note.objects.get(pk=note_id)
	if request.method == 'POST':
		note.user = User.objects.get(pk=request.POST.get('user', note.user))
		note.text = request.POST.get('text', note.text)
		note.save()
		return redirect('/notes/')
	users = User.objects.all()
	template = loader.get_template('notes/edit.html')
	context = RequestContext(request, {
		'note': note,
		'users': users
	})
	return HttpResponse(template.render(context))

def delete(request, note_id):
	note = Note.objects.get(pk=note_id)
	note.delete()
	return redirect('/notes/')
