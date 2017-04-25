#coding=utf-8
import datetime
import decimal

from django.http import Http404, HttpResponse
import json
from django.utils.timezone import is_aware
from django.db import models

from django.core.serializers import serialize
from json import dumps, loads
from django.db.models.query import QuerySet, ValuesQuerySet
from django.utils.functional import curry
from django.forms.models import model_to_dict
from django.db import connection
import traceback

def Ajax(fn):
    def wrapper(*args, **kv):
        request = args[0]
        #if not  settings.DEBUG and\
        #not request.is_ajax():
        #    raise Http404
        result= fn(*args, **kv)
        result=dumps(result)
        return HttpResponse(result,mimetype="application/json")
    return wrapper

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
        else:
            return super(DjangoJSONEncoder, self).default(o)
dumps = curry(dumps, cls=DjangoJSONEncoder)

