#coding:utf-8
from django.http import HttpResponse
from  django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from settings import VERSION,LAST
import httplib2,re
from urllib import urlencode
import json
from admin.models import *
def common(request):
    return {
        'VERSION': VERSION,
        'LAST': LAST,
    }
def index(request):
    return render_to_response('index.html',context_instance = RequestContext(request,processors=[common]))


@csrf_exempt
def add_task(request):
    from forms import TaskForm
    form = TaskForm(request.POST)
    scrapy_error = False
    if form.is_valid():
        data = form.cleaned_data['data']
        print data
        mail = data['address']
        task_list = data['urls']
        http = httplib2.Http()
        data={'project':"dirbot","spider":"taobao"}
        header={'Content-Type': 'application/x-www-form-urlencoded'}
        for item in task_list:
            Q = Queue(url=item,mail=mail)
            Q.save()
            try:
                s,c = http.request("http://localhost:6800/schedule.json","POST",urlencode(data),headers=header)
            except Exception:
                c = {'status':'error','msg':'爬虫服务器连接失败'}
                scrapy_error = True
    else:
        return HttpResponse(json.dumps({'status':'error','msg':form['data'].errors}))
    if scrapy_error:
        return HttpResponse(json.dumps(c,ensure_ascii=False))
    return HttpResponse(c)

