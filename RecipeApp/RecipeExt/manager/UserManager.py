import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Chef


@csrf_exempt
def chefRequest(request, chef_id=None):
	return HttpResponse(json.dumps({"success":True}), content_type="application/json")