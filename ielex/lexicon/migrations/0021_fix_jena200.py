# -*- coding: utf-8 -*-
# Inspired by:
# https://docs.djangoproject.com/en/1.9/ref/migration-operations/#runpython
# http://clld.org/2015/11/13/glottocode-to-isocode.html
from __future__ import unicode_literals

from django.db import migrations, models

import ielex.lexicon.models as models

# 0013_meaningLists for Jena200
meanings = [{'id': 208, 'name': 'ant'},
            {'id': 4, 'name': 'ashes'},
            {'id': 6, 'name': 'back'},
            {'id': 7, 'name': 'bad'},
            {'id': 8, 'name': 'bark'},
            {'id': 10, 'name': 'belly'},
            {'id': 11, 'name': 'big'},
            {'id': 12, 'name': 'bird'},
            {'id': 13, 'name': 'bite'},
            {'id': 215, 'name': 'bitter'},
            {'id': 14, 'name': 'black'},
            {'id': 15, 'name': 'blood'},
            {'id': 16, 'name': 'blow'},
            {'id': 17, 'name': 'bone'},
            {'id': 18, 'name': 'breast'},
            {'id': 19, 'name': 'breathe'},
            {'id': 20, 'name': 'burn'},
            {'id': 220, 'name': 'carry'},
            {'id': 21, 'name': 'child'},
            {'id': 226, 'name': 'claw'},
            {'id': 22, 'name': 'cloud'},
            {'id': 23, 'name': 'cold'},
            {'id': 24, 'name': 'come'},
            {'id': 25, 'name': 'count'},
            {'id': 223, 'name': 'cry'},
            {'id': 26, 'name': 'cut'},
            {'id': 27, 'name': 'day'},
            {'id': 28, 'name': 'die'},
            {'id': 29, 'name': 'dig'},
            {'id': 30, 'name': 'dirty'},
            {'id': 224, 'name': 'do-make'},
            {'id': 31, 'name': 'dog'},
            {'id': 32, 'name': 'drink'},
            {'id': 33, 'name': 'dry'},
            {'id': 35, 'name': 'dust'},
            {'id': 36, 'name': 'ear'},
            {'id': 37, 'name': 'earth'},
            {'id': 38, 'name': 'eat'},
            {'id': 39, 'name': 'egg'},
            {'id': 40, 'name': 'eye'},
            {'id': 41, 'name': 'fall'},
            {'id': 42, 'name': 'far'},
            {'id': 43, 'name': 'fat'},
            {'id': 44, 'name': 'father'},
            {'id': 45, 'name': 'fear'},
            {'id': 46, 'name': 'feather'},
            {'id': 48, 'name': 'fight'},
            {'id': 49, 'name': 'fingernail'},
            {'id': 50, 'name': 'fire'},
            {'id': 51, 'name': 'fish'},
            {'id': 52, 'name': 'five'},
            {'id': 55, 'name': 'flower'},
            {'id': 56, 'name': 'fly'},
            {'id': 211, 'name': 'fly_N'},
            {'id': 57, 'name': 'fog'},
            {'id': 58, 'name': 'foot'},
            {'id': 59, 'name': 'four'},
            {'id': 60, 'name': 'freeze'},
            {'id': 61, 'name': 'fruit'},
            {'id': 62, 'name': 'full'},
            {'id': 63, 'name': 'give'},
            {'id': 218, 'name': 'go'},
            {'id': 64, 'name': 'good'},
            {'id': 65, 'name': 'grass'},
            {'id': 66, 'name': 'green'},
            {'id': 225, 'name': 'grind'},
            {'id': 67, 'name': 'guts'},
            {'id': 68, 'name': 'hair'},
            {'id': 69, 'name': 'hand'},
            {'id': 216, 'name': 'hard'},
            {'id': 71, 'name': 'head'},
            {'id': 72, 'name': 'hear'},
            {'id': 73, 'name': 'heart'},
            {'id': 74, 'name': 'heavy'},
            {'id': 75, 'name': 'here'},
            {'id': 222, 'name': 'hide'},
            {'id': 76, 'name': 'hit'},
            {'id': 78, 'name': 'horn'},
            {'id': 214, 'name': 'house'},
            {'id': 79, 'name': 'how'},
            {'id': 80, 'name': 'hunt'},
            {'id': 82, 'name': 'I'},
            {'id': 83, 'name': 'ice'},
            {'id': 86, 'name': 'kill'},
            {'id': 87, 'name': 'knee'},
            {'id': 88, 'name': 'know'},
            {'id': 89, 'name': 'lake'},
            {'id': 90, 'name': 'laugh'},
            {'id': 91, 'name': 'leaf'},
            {'id': 92, 'name': 'left'},
            {'id': 93, 'name': 'leg'},
            {'id': 94, 'name': 'lie'},
            {'id': 95, 'name': 'live'},
            {'id': 96, 'name': 'liver'},
            {'id': 97, 'name': 'long'},
            {'id': 98, 'name': 'louse'},
            {'id': 99, 'name': 'man'},
            {'id': 101, 'name': 'meat'},
            {'id': 102, 'name': 'moon'},
            {'id': 103, 'name': 'mother'},
            {'id': 104, 'name': 'mountain'},
            {'id': 105, 'name': 'mouth'},
            {'id': 106, 'name': 'name'},
            {'id': 107, 'name': 'narrow'},
            {'id': 210, 'name': 'navel'},
            {'id': 108, 'name': 'near'},
            {'id': 109, 'name': 'neck'},
            {'id': 110, 'name': 'new'},
            {'id': 111, 'name': 'night'},
            {'id': 112, 'name': 'nose'},
            {'id': 113, 'name': 'not'},
            {'id': 114, 'name': 'old'},
            {'id': 115, 'name': 'one'},
            {'id': 117, 'name': 'person'},
            {'id': 118, 'name': 'play'},
            {'id': 119, 'name': 'pull'},
            {'id': 120, 'name': 'push'},
            {'id': 121, 'name': 'rain'},
            {'id': 122, 'name': 'red'},
            {'id': 123, 'name': 'right'},
            {'id': 124, 'name': 'rightside'},
            {'id': 125, 'name': 'river'},
            {'id': 127, 'name': 'root'},
            {'id': 129, 'name': 'rotten'},
            {'id': 130, 'name': 'round'},
            {'id': 219, 'name': 'run'},
            {'id': 132, 'name': 'salt'},
            {'id': 133, 'name': 'sand'},
            {'id': 134, 'name': 'say'},
            {'id': 135, 'name': 'scratch'},
            {'id': 136, 'name': 'sea'},
            {'id': 137, 'name': 'see'},
            {'id': 138, 'name': 'seed'},
            {'id': 139, 'name': 'sew'},
            {'id': 213, 'name': 'shadow'},
            {'id': 140, 'name': 'sharp'},
            {'id': 141, 'name': 'short'},
            {'id': 142, 'name': 'sing'},
            {'id': 143, 'name': 'sit'},
            {'id': 144, 'name': 'skin'},
            {'id': 145, 'name': 'sky'},
            {'id': 146, 'name': 'sleep'},
            {'id': 147, 'name': 'small'},
            {'id': 148, 'name': 'smell'},
            {'id': 149, 'name': 'smoke'},
            {'id': 150, 'name': 'smooth'},
            {'id': 151, 'name': 'snake'},
            {'id': 152, 'name': 'snow'},
            {'id': 154, 'name': 'spit'},
            {'id': 158, 'name': 'stand'},
            {'id': 159, 'name': 'star'},
            {'id': 160, 'name': 'stick'},
            {'id': 161, 'name': 'stone'},
            {'id': 162, 'name': 'straight'},
            {'id': 164, 'name': 'sun'},
            {'id': 217, 'name': 'sweet'},
            {'id': 165, 'name': 'swell'},
            {'id': 166, 'name': 'swim'},
            {'id': 167, 'name': 'tail'},
            {'id': 221, 'name': 'take_away'},
            {'id': 168, 'name': 'that'},
            {'id': 169, 'name': 'there'},
            {'id': 170, 'name': 'they'},
            {'id': 171, 'name': 'thick'},
            {'id': 209, 'name': 'thigh'},
            {'id': 172, 'name': 'thin'},
            {'id': 173, 'name': 'think'},
            {'id': 174, 'name': 'this'},
            {'id': 175, 'name': 'thou'},
            {'id': 176, 'name': 'three'},
            {'id': 177, 'name': 'throw'},
            {'id': 178, 'name': 'tie'},
            {'id': 179, 'name': 'tongue'},
            {'id': 180, 'name': 'tooth'},
            {'id': 181, 'name': 'tree'},
            {'id': 182, 'name': 'turn'},
            {'id': 183, 'name': 'two'},
            {'id': 184, 'name': 'vomit'},
            {'id': 185, 'name': 'walk'},
            {'id': 186, 'name': 'warm'},
            {'id': 187, 'name': 'wash'},
            {'id': 188, 'name': 'water'},
            {'id': 189, 'name': 'we'},
            {'id': 190, 'name': 'wet'},
            {'id': 191, 'name': 'what'},
            {'id': 192, 'name': 'when'},
            {'id': 193, 'name': 'where'},
            {'id': 194, 'name': 'white'},
            {'id': 195, 'name': 'who'},
            {'id': 196, 'name': 'wide'},
            {'id': 198, 'name': 'wind'},
            {'id': 199, 'name': 'wing'},
            {'id': 201, 'name': 'with'},
            {'id': 202, 'name': 'woman'},
            {'id': 203, 'name': 'woods'},
            {'id': 204, 'name': 'worm'},
            {'id': 205, 'name': 'you'},
            {'id': 206, 'name': 'year'},
            {'id': 207, 'name': 'yellow'},
            {'id': 212, 'name': 'yesterday'}]


def forwards_func(apps, schema_editor):
    MeaningList = models.MeaningList

    # Removing -alpha list:
    remove = 'Jena200-alpha'
    try:
        ml = MeaningList.objects.get(name=remove)
        ml.delete()
        print("Removed MeaningList ", remove)
    except:
        print("Couldn't remove '", remove, "' - maybe it doesn't exist?")

    # Cleaning default list:
    print("Now cleaning up ", MeaningList.DEFAULT)
    wanted = set([m['id'] for m in meanings])
    try:
        ml = MeaningList.objects.get(name=MeaningList.DEFAULT)
        for m in ml.meanings.all():
            if m.id not in wanted:
                print("Removing Meaning from List: ", m.gloss)
                ml.remove(m)
    except Exception, e:
        print("Exception while cleaning up ", MeaningList.DEFAULT, e)


def reverse_func(apps, schema_editor):
    print('Reverse of 0021_fix_jena200 does nothing.')


class Migration(migrations.Migration):

    dependencies = [('lexicon', '0020_language_languageBranches')]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]