from apps.contact.forms import MessageForm, InterestedForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def message_form(request, template_name="contact/message.html"):
    form = MessageForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = 'Missatge rebut!'
            request.user.message_set.create(message=msg)
            return HttpResponseRedirect("/contacte")

    data = {
        'form': form,
    }
    return render_to_response(template_name, data, RequestContext(request))


def interested_form(request, template_name="contact/afiliacio.html"):
    form = InterestedForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = 'Apuntat correctament!'
            request.user.message_set.create(message=msg)
            return HttpResponseRedirect("/afiliacio")

    data = {
        'form': form,
    }
    return render_to_response(template_name, data, RequestContext(request))


