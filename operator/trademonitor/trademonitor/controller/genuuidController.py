'''
Created on 2017-01-21

@author: Chen
'''
import uuid
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import traceback
from trademonitor.decorator.Ajax import *

@csrf_exempt
@Ajax
def genuuid(request):
    rlist = []
    rlist.append(str(uuid.uuid1()))
    return rlist