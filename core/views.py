from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render,HttpResponse
from django.db.models import Avg,Count,Min,Sum
from .models import *

import requests as req
import json
import pandas as pd


def dataView(request): 
    context ={
        'overall_sale_by_country':Data.objects.all().order_by('year'),
    }
    return render(request, 'index.html',context)


def overall_sale_by_country(request):
    context={
        'result':Data.objects.filter(sale__gt=0).values('country','product').annotate(Sum('sale')).order_by('country')
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



class Find:
    def post(self, request):
        if request.method == "POST":
            year = request.POST.get('year')
            product = request.POST.get('product')
            country = request.POST.get('country')
            
            data = get_list_or_404(Data,year=year,product__icontains=product,country__icontains=country)
            
            return data
        else:
            pass
        



def landing(request):
    s = Find()
    try:
        result = s.post(request)
        context={
            'result':result,
        }
    except Http404 as e:
        err=e
        context={
            'error':err,
        }
    return render(request,'landing.html',context)



