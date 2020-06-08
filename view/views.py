from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import json

from comment.views import regions_load, get_city_by_region_id


def view(request):
    return render(request, 'view/view.html')


def get_comments(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "main"."form" '
                   'LEFT JOIN city on form.City=city.ID '
                   'LEFT JOIN region ON form.Region=region.ID')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(
            {
                "id": row[0],
                "Surname": row[1],
                "Name": row[2],
                "Patronymic": row[3],
                "Region": row[13],
                "City": row[11],
                "Phone": row[6],
                "E-mail": row[7],
                "Comment": row[8],
            }
        )
    conn.commit()
    conn.close()
    data = json.dumps(result)
    return HttpResponse(data, content_type='application/json')


def delete_row(request, id):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM "main"."form" WHERE ID = {id}')
    response = dict(cursor.fetchall())
    data = json.dumps(response)
    conn.commit()
    conn.close()
    return HttpResponse(data, content_type='application/json')
