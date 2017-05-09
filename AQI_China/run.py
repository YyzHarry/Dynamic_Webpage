#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from app import automate
import click


automate.dbcity_init()

@click.command()
@click.option("--city", "-c", default=["南京"], multiple=True, help="Name of cities")
@click.option("--month", "-m", default=["201312"], multiple=True, help="list of monthes")
@click.option('--allcities', is_flag=False)
@click.option('--allmonths', is_flag=False)
def main(city, month, allcities, allmonths):

    if all([allcities, allmonths]):
        automate.collect_all()
    elif allcities:
        raise NotImplementedError
    elif allmonths:
        for c in city:
            automate.collect_one_city_async(c)
    else:
        for c in city:
            for m in month:
                automate.scrape_parse(c,m)

    
if __name__ == '__main__':
    main()