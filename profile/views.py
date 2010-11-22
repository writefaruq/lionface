from django.template import loader, Context
from django.http import HttpResponse
from lionface.profile.models import Place

def places(request):
	places = Place.objects.all()
	t = loader.get_template("places.html")
	c = Context({'places' : places })
	return HttpResponse(t.render(c))
