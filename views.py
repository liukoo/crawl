#coding:utf-8
from django.http import HttpResponse
from  django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import httplib2,MySQLdb,re
from urllib import urlencode
import json
from admin.models import *

def index(request):
    return render_to_response('index.html')

@csrf_exempt
def add_task(request):
    url = request.POST["store_url"]
    mail = request.POST["mail_address"]
    rule = re.compile(r"(?:http://)?([^/]+)")
    rule2 = re.compile(r"\w+(?:\.\w+)?@\w+\.\w+")
    url = rule.match(url)
    if url:
        url = url.group(1)
    else:
        msg = {'stat':'error','msg':'店铺地址错误'}
        return HttpResponse(json.dumps(msg,ensure_ascii=False))
    if not rule2.match(mail):
        msg = {'stat':'error','msg':'邮箱格式错误'}
        return HttpResponse(json.dumps(msg,ensure_ascii=False))
    http = httplib2.Http()
    data={'project':"dirbot","spider":"taobao"}
    header={'Content-Type': 'application/x-www-form-urlencoded'}
    Q = Queue(url=url,mail=mail)
    Q.save()
    s,c = http.request("http://localhost:6800/schedule.json","POST",urlencode(data),headers=header)
    return HttpResponse(c)
