from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from notes.models import Note

def index(request):
	note_list = Note.objects.all()
	template = loader.get_template('notes/index.html')
	context = RequestContext(request, {
		'note_list': note_list,
	})
	return HttpResponse(template.render(context))

def show(request, note_id):
	return HttpResponse("show note: %s" % note_id)

def edit(request, note_id):
	return HttpResponse("edit note: %s" % note_id)
