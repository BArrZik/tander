from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import json


# Create your views here.

def comment(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS "form" (	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	"Surname"	TEXT NOT NULL,	"Name"	TEXT NOT NULL,	"Patronymic"	TEXT,	"Region"	TEXT,	"City"	TEXT,	"Phone"	TEXT,	"E-mail"	TEXT,	"Comment"	TEXT NOT NULL);')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS "region" (	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	"Region"	TEXT NOT NULL UNIQUE);')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS "city" (	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	"Region_ID"	INTEGER NOT NULL,	"City"	TEXT NOT NULL UNIQUE,	FOREIGN KEY("Region_ID") REFERENCES "region"("ID"));')
    cursor.execute('INSERT OR IGNORE INTO "main"."region" ("ID", "Region") VALUES (1, "Краснодарский край");')
    cursor.execute('INSERT OR IGNORE INTO "main"."region" ("ID", "Region") VALUES (2, "Ростовская область");')
    cursor.execute('INSERT OR IGNORE INTO "main"."region" ("ID", "Region") VALUES (3, "Ставропольский край");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (1, 1, "Краснодар");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (2, 1, "Кропоткин");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (3, 1, "Славянск");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (4, 2, "Ростов");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (5, 2, "Шахты");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (6, 2, "Батайск");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (7, 3, "Ставрополь");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (8, 3, "Пятигорск");')
    cursor.execute('INSERT OR IGNORE INTO "main"."city" ("ID", "Region_ID", "City") VALUES (9, 3, "Кисловодск");')
    conn.commit()
    # cursor.execute('SELECT City FROM "main"."city" WHERE Region_ID = 2;')
    # results = cursor.fetchall()
    # context = {'results': results}
    # cursor.execute('SELECT ID,Region FROM "main"."region"')
    # results = dict(cursor.fetchall())
    # html_result = ''
    # for id,region in results.items():
    #     html_result += f'<option value="{id}">{region}</option>'
    # print(html_result)
    conn.close()
    answer = None

    if request.method == 'POST':
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute(
            f'INSERT OR IGNORE INTO "main"."form" ("Surname", "Name", "Patronymic", "Region", "City", "Phone", "E-mail", "Comment") VALUES ("{request.POST["surname"]}", "{request.POST["name"]}", "{request.POST["patronymic"]}", "{request.POST["region"]}", "{request.POST["city"]}", "{request.POST["phone"]}", "{request.POST["e-mail"]}", "{request.POST["comment"]}");')
        conn.commit()
        conn.close()
        answer = 'Форма отправлена'

    context = {
        'regions': regions_load(),
        'response': f'<p>{answer}</p>',
        'where': request.path,
    }

    return render(request, 'comment/comment.html', context)


def regions_load():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT ID, Region FROM "main"."region"')
    regions = dict(cursor.fetchall())

    return regions


def get_city_by_region_id(request, region_id=1):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(f'SELECT ID, City FROM `main`.`city` WHERE `Region_ID` = {region_id}')
    citys = dict(cursor.fetchall())
    data = json.dumps(citys)

    return HttpResponse(data, content_type='application/json')
