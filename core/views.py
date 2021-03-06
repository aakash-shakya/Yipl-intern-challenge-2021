from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Min, Sum
from .models import *

import pandas as pd


def dataView(request):
    context = {
        "overall_sale_by_country": Data.objects.all().order_by("year"),
    }
    return render(request, "index.html", context)


def overall_sale_by_country(request):
    context = {
        "result": Data.objects.filter(sale__gt=0)
        .values("country", "product")
        .annotate(Sum("sale"))
        .order_by("country")
    }
    return render(request, "overallSale.html", context)


def avg_sale_of_each_product_for_2_years(request):
    data = Data.objects.all().values("year", "sale", "country", "product")
    data = pd.DataFrame(list(data))

    data["year"] = pd.to_datetime(data["year"], format="%Y")
    final_df = (
        data.groupby(["product", pd.Grouper(key="year", freq="2Y", closed="left")])
        .agg(
            {
                "year": lambda x: "-".join((str(min(x.dt.year)), str(max(x.dt.year)))),
                "sale": "mean",
            },
            data["sale"],
        )
        .reset_index(level=0)
        .reset_index(drop=True)
    )

    html = final_df.to_html(border=1, table_id="design", col_space=125)
    context = {
        "result": html,
    }
    return render(request, "avgSale.html", context)


def least_sale_year(request):
    data = (
        Data.objects.filter(sale__gt=0).values("product").annotate(min_sale=Min("sale"))
    )
    final_data = Data.objects.filter(sale__in=data.values("min_sale"))
    context = {
        "result": final_data,
    }
    return render(request, "minSale.html", context)


class Find:
    def getData(self, request):
        if request.method == "GET":
            year = request.GET.get("year")
            product = request.GET.get("product")
            country = request.GET.get("country")

            data = get_object_or_404(
                Data, year=year, product=product, country=country
            )

            return data
        else:
            pass


year = [2007,2008,2009,2010,2011,2012,2013,2014]
country = ['USA','Saudi Arabia','Russia','Isereal']
product = ['Kerosene','Diesel','Petrol','Furnace Oil','LPG in MT','Light Diesel Oil','Aviation Turbine Fuel','Mineral Turpentine Oil']

def landing(request):
    if request.method == "GET":
        if 'getData' in request.GET:
            try:
                s = Find()
                result = s.getData(request)
                context = {
                    "result": result,
                    "year":year,
                    "country":country,
                    "product":product,
                }
            except Http404 as e:
                err = e
                context = {
                    "error": err,
                    "year":year,
                    "country":country,
                    "product":product,
                }
        else:
            context={
                "result":False,
                "error":False,
                "year":year,
                "country":country,
                "product":product,
            }  
    return render(request, "landing.html", context)
