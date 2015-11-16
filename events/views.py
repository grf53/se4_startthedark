from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event


def tonight(request):
    events = Event.objects.filter(latest=True).today()
    context = {
        'events': events,
    }
    return render_to_response(
        'tonight.html',
        context,
        context_instance=RequestContext(request)
    )
