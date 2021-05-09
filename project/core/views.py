from django.shortcuts import render
from django.db.models import Avg,Count,Min,Sum
from .models import *

import requests as req
import json


def dataView(request):
    url = "https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json"
    res = req.get(url).json()

    # try:
    #     for i in res:
    #         info = Data()
    #         info.year=i['year']
    #         info.sale=i['sale']
    #         info.product=i['petroleum_product']
    #         info.country=i['country']
    #         info.save()

    # except Exception as e:
    #     print(e)

    context ={
        'overall_sale_by_country':Data.objects.all(),
    }
    return render(request, 'index.html',context)


def overall_sale_by_country(request):
    context={
        'result':Data.objects.filter(sale__gt=0).values('country','product').annotate(Sum('sale')).order_by()
    }
    return render(request,'overallSale.html',context)