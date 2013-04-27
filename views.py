from django.http import HttpResponse
from  django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import httplib2,MySQLdb,re
from urllib import urlencode
from admin.models import *

def index(request):
    return render_to_response('index.html')

@csrf_exempt
def add_task(request):
    url = request.POST["store_url"]
    mail = request.POST["mail_address"]
    rule = re.compile(r"(?:http://)?([^/]*)")
    url = rule.match(url)
    if url:
        url = url.group(1)
    else:
        return HttpResponse("{'stat':'error'}")
    http = httplib2.Http()
    data={'project':"dirbot","spider":"taobao"}
    header={'Content-Type': 'application/x-www-form-urlencoded'}
    Q = Queue(url=url,mail=mail)
    Q.save()
    s,c = http.request("http://localhost:6800/schedule.json","POST",urlencode(data),headers=header)
    return HttpResponse(c)
