from django.shortcuts import render
from django.db.models import Avg,Count,Min,Sum
from .models import *

import requests as req
import json
import pandas as pd


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

def avg_sale_of_each_product_for_2_years(request):
    data = Data.objects.all().values('year','sale','country','product')
    data = pd.DataFrame(list(data))
   
    data['year'] = pd.to_datetime(data['year'], format = '%Y')
    final_df = data.groupby(['product', pd.Grouper(key = 'year', freq = '2Y', closed = 'left')]).agg(
                    {'year': lambda x: '-'.join((str(min(x.dt.year)), str(max(x.dt.year)))),
                    'sale':'mean',
                    
                    },data['sale']).reset_index(level= 0).reset_index(drop=True)
    
    html=final_df.to_html(border=1,table_id='design',col_space=125)
    context={
        'result':html,
    }
    return render(request,'avgSale.html',context)

def least_sale_year(request):
    data=Data.objects.filter(sale__gt=0).values('product').annotate(min_sale=Min('sale'))
    final_data = Data.objects.filter(sale__in=data.values('min_sale'))
    context={
        'result':final_data,
    }
    return render(request,'minSale.html',context)