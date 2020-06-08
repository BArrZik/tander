from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import json

from comment.views import get_region_by_id


def stat(request):
    context = {
        'statistics': get_stat(),
    }
    return render(request, 'comment_stat/_stat.html', context)


def get_stat():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("""select region.Region as name, region.ID as regId, form.Region, count(form.Region) as cnt
                    from region
                        join form on region.ID = form.region
                    group by region.Region""")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        if row[3] > 5:
            result.append(
                {
                    "Region": row[0],
                    "id": row[1],
                    "Count": row[3],
                })
    conn.commit()
    conn.close()
    return result


def get_region_stat(request, region_id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('''select city.City as name, city.Region_ID as regId, form.City, count(form.City) as cnt
                    from city
                        join form on city.ID = form.city
                    group by city.City''')
    rows = cursor.fetchall()
    conn.close()
    result = []
    for row in rows:
        if row[1] == region_id:
            result.append(
                {
                    "city": row[0],
                    "count": row[3],
                }
            )
    context = {
        "statistics": result,
        "region_name": get_region_by_id(region_id)
    }
    return render(request, 'comment_stat/region_stat.html', context)
