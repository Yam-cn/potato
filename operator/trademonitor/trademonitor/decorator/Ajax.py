#coding=utf-8
import datetime
import decimal

from django.http import Http404, HttpResponse, JsonResponse
import json
from django.utils.timezone import is_aware
from django.db import models
from django.core.serializers import serialize
from json import dumps, loads
from django.db.models.query import QuerySet,ValuesQuerySet
from django.utils.functional import curry
from django.forms.models import model_to_dict
from django.db import connection,connections
import traceback
from django.core.cache import cache
#from django.utils import simplejson
import json
from _random import Random
import time
import re
from trademonitor import settings

from django.utils.text import compress_sequence, compress_string

from django.utils.text import compress_sequence, compress_string
from django.utils.cache import patch_vary_headers
from django.http.request import HttpRequest
class DjangoJSONEncoder(json.JSONEncoder):
    """
        JSONEncoder subclass that knows how to encode date/time and decimal types.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o,ValuesQuerySet):
            return list(o)
        elif isinstance(o, QuerySet):
            return loads(serialize('json', o))
        elif isinstance(o, models.Model):
            return str(o)
            #return dict([(attr, getattr(o, attr)) for attr in [f.name for f in o._meta.fields]])
        else:
            return super(DjangoJSONEncoder, self).default(o)


dumps = curry(dumps, cls=DjangoJSONEncoder)

import cPickle as p 
import os

def Ajax(fn):
    def wrapper(*args, **kv):
        request = args[0]
        if not  settings.DEBUG and\
        not request.is_ajax():
            raise Http404
        result= fn(*args, **kv)
        #list =  request.GET.has_key("list")
        result=dumps(result)
            
        resposne = compressResult(result)

        return resposne
    return wrapper


def compressResult(result):
    #response = HttpResponse(result,mimetype="application/json")
    response = JsonResponse(result,safe=False)
    #response['Access-Control-Allow-Origin'] = '*'

    compressed_content = compress_string(response.content)
    if len(compressed_content) >= len(response.content):
        return response
    response.content = compressed_content
    response['Content-Length'] = str(len(response.content))
    response['Content-Encoding'] = 'gzip'
    return response
