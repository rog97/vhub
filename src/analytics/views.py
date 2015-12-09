from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
import requests
from requests.exceptions import HTTPError
import ibis
import pandas
import sklearn
import matplotlib.pyplot as plt
import numpy as np
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "crunchbase.db")
# Create your views here.

def activate_db():
    ibis.options.interactive = True
    con = ibis.sqlite.connect('crunchbase.db')
    return con

def analysis(request):
    ibis.options.interactive = True
    con = ibis.sqlite.connect('crunchbase.db')
    template = "analysis.html"
    context = {
        "funding_rounds": funding_rounds(),
        "great_vcs": great_vcs(),
    }
    return render(request, template, context)

# print(con.list_tables())
def funding_rounds():
    con = activate_db()
    rounds = con.table('rounds')
    # print(rounds.info())
    #
    # print(rounds.funding_round_type.value_counts())

    companies = con.table('companies')

    expr = companies.funding_total_usd.mean()

    expr.execute()

    funded_at = rounds.funded_at.cast('timestamp')
    funded_at.year().value_counts()

    year = funded_at.year().name('year')

    expr = (rounds[(rounds.funding_round_type == 'venture') &
                   year.between(2001, 2014) &
                   rounds.funding_round_code.notnull()]
            .group_by([year, 'funding_round_code'])
            .size())

    results = expr.execute()
    results[:10]

    pivoted = (results.set_index(['year', 'funding_round_code'])
               .unstack('funding_round_code')
               .fillna(0))

    pivoted_html = pivoted.to_html()
    return pivoted_html

def great_vcs():
    con = activate_db()

    i = con.table('investments')
    c = con.table('companies')

    clean_name = i.investor_name.fillna('NO INVESTOR').name('investor_name')
    num_investments = c.permalink.nunique()

    exited = c.status.isin(['ipo', 'acquired']).ifelse(c.permalink, ibis.NA)
    num_exits = exited.nunique()

    stats = (c.left_join(i, c.permalink == i.company_permalink)
             .group_by(clean_name)
             .aggregate(num_investments=num_investments,
                        num_exits=num_exits))

    stats = (stats.mutate(succ_rate=(stats.num_exits /
                                    stats.num_investments.cast('float'))))
    stats.limit(10)

    great_success = (stats
                     [stats.num_investments > 100]
                     .sort_by(ibis.desc('succ_rate')))

    top50 = great_success.limit(50)
    top50_dataframe = top50.execute()
    top50_html = top50_dataframe.to_html()
    # print(top20_view)
    # print(type(top20_view))
    return top50_html
