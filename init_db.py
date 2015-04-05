#!/user/bin/env python

# Initialize django
import os
import sys
import datetime
from decimal import Decimal
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'colonial.settings'
django.setup()

import app_base.models as bmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess

# DROP DATABASE, RECREATE IT, THEN MIGRATE IT #

__author__ = 'Group1-3'
cursor = connection.cursor()
cursor.execute("PRAGMA writable_schema = 1;")
cursor.execute("delete from sqlite_master where type in ('table', 'index', 'trigger');")
subprocess.call([sys.executable, "manage.py", "migrate"])


#           CREATE PERMISSIONS/GROUPS           #

for data in [{'codename': 'manager_rights', 'name': 'Has Manager Rights'},
             {'codename': 'customer_rights', 'name': 'Has Customer Rights'},
             {'codename': 'admin_rights', 'name': 'Has Administrator Rights'}]:
    p = Permission()
    for k, v in data.items():
        setattr(p, k, v)
        p.content_type = ContentType.objects.get(id=2)
    p.save()

for data in [{'name': 'Customer'}, {'name': 'Manager'}, {'name': 'Admin'}]:
    g = Group()
    for k, v in data.items():
        setattr(g, k, v)
        g.save()
        if k == 'name':
            p = Permission.objects.get(codename=v.lower() + '_rights')
            g.permissions.add(p)


print('Permissions initialized')


#           CREATE ADRESSES        #

for data in [
    {'address1':    '89 E 200 N',
     'city':        'Orem',
     'state':       'UT',
     'zip_code':    '84602'},
    {'address1':    '143 Ethyl Ct. #3',
     'city':        'Milpitas',
     'state':       'CA',
     'zip_code':    '95035'},
    {'address1':    '79 E 300 N',
     'city':        'Provo',
     'state':       'UT',
     'zip_code':    '84606'},
    {'address1':    '930 N American Dr.',
     'city':        'Provo',
     'state':       'UT',
     'zip_code':    '84606'},
    {'address1':    '1330 N American Dr.',
     'city':        'Provo',
     'state':       'UT',
     'zip_code':    '84606'}
]:

    a = bmod.Address()
    for k, v in data.items():
        setattr(a, k, v)
    a.save()

print('Addresses initialized')


#           CREATE PHOTOS          #

for data in [
    ["Wand", "/static/app_store/media/wand.jpg"],
    ["GoveRobes", "/static/app_store/media/gove.jpg"],
    ["Quill", "/static/app_store/media/quill.jpg"],
    ["Cards", "/static/app_store/media/cards.jpg"],
    ["Drum", "/static/app_store/media/drum.jpg"],
    ["Fife", "/static/app_store/media/fife.jpg"],
    ["Gun", "/static/app_store/media/gun.jpg"],
    ["Handkerchief", "/static/app_store/media/handkerchief.jpg"],
    ["Map", "/static/app_store/media/map.jpg"],
    ["Teapot", "/static/app_store/media/teapot.jpg"],
    ["Top", "/static/app_store/media/top.jpg"],
    ["Wallet", "/static/app_store/media/wallet.jpg"],
    ["Lavender Water", "/static/app_store/media/water.jpg"],
    ["Mayflower", "/static/app_store/media/mayflower.jpg"],
    ["Towel", "/static/app_store/media/flagtowel.jpg"],
    ["Dill", "/static/app_store/media/pickles.jpg"],
    ["Okra", "/static/app_store/media/okra.jpg"],
    ["Syrup", "/static/app_store/media/syrup.jpg"]
]:
    # Create new Sale Item
    p = bmod.Photograph()

    # Assign product attributes
    p.description = data[0]
    p.image = data[1]
    p.save()

print('Photos initialized')


#           CREATE USERS           #

for data in [
    {'username':        'TyCool4School',
     'email':           'ty@ty.com',
     'first_name':      'Ty',
     'last_name':       'Anderson'},
    {'username':        'CodyingAllNight',
     'email':           'cdy@cdy.com',
     'first_name':      'Cody',
     'last_name':       'Booher'},
]:

    u = bmod.User()
    for k, v in data.items():
        setattr(u, k, v)
    u.set_password('Password1')
    u.address_id = bmod.Address.objects.get(address1='79 E 300 N').id
    u.save()
    Group.objects.get(name='Customer').user_set.add(u)

print('Users initialized')


#           CREATE EMPLOYEES            #

for data in [
    {'username':        'Kevbo',
     'email':           'pedantfool@gmail.com',
     'first_name':      'Kevin',
     'last_name':       'Gardner',
     'is_superuser':    'TRUE',
     'date_hired':      datetime.datetime.now(),
     'salary':          65400.00},
    {'username':        'Reverend',
     'email':           'r@k.com',
     'first_name':      'Rebecca',
     'last_name':       'Gardner',
     'is_superuser':    'FALSE',
     'date_hired':      datetime.datetime.now(),
     'wage':            32.45}
]:

    e = bmod.Employee()
    for k, v in data.items():
        setattr(e, k, v)
    e.set_password('Password1')
    e.address_id = bmod.Address.objects.get(address1='143 Ethyl Ct. #3').id
    e.save()
    if e.username == 'Kevbo':
        Group.objects.get(name='Admin').user_set.add(e)
    else:
        Group.objects.get(name='Manager').user_set.add(e)

print('Employees initialized')


#           CREATE VENDORS            #

for data in [
    {'username':        '2Tyler2Quit',
     'email':           'tyler@ty.ty',
     'first_name':      'Tyler',
     'last_name':       'White',
     'SSN':             '234-45-6789',
     'EIN':             '12-3456789',
     'UTTaxID':         'AF-2345'},
    {'username':        'GoveByDaPound',
     'email':           'gove@love.com',
     'first_name':      'Gove',
     'last_name':       'Allen',
     'SSN':             '224-45-6789',
     'EIN':             '12-3456789',
     'UTTaxID':         'AF-2345'}
]:

    ven = bmod.Vendor()
    for k, v in data.items():
        setattr(ven, k, v)
    ven.set_password('Password1')
    ven.address_id = bmod.Address.objects.get(address1='89 E 200 N').id
    ven.save()

print('Vendors initialized')


#           CREATE TRANSACTIONS           #

for data in [
    {'date':                    datetime.date.today() - datetime.timedelta(2),
     'phone':                   '801-263-9250',
     'date_packed':             datetime.date.today() - datetime.timedelta(1),
     'date_shipped':            datetime.date.today(),
     'tracking_number':         '12324356u5634',
     'customer':                bmod.User.objects.get(username='2Tyler2Quit'),
     'shipped_by':              bmod.User.objects.get(username='Reverend'),
     'handled_by':              bmod.User.objects.get(username='Reverend'),
     'ships_to':                bmod.User.objects.get(username='2Tyler2Quit').address,
     'payment_processed_by':    bmod.User.objects.get(username='Reverend')},
    {'date':                    datetime.date.today() - datetime.timedelta(3),
     'phone':                   '801-245-5678',
     'customer':                bmod.User.objects.get(username='CodyingAllNight'),
     'payment_processed_by':    bmod.User.objects.get(username='Reverend')},
    {'date':                    datetime.date.today() - datetime.timedelta(3),
     'phone':                   '801-456-6456',
     'customer_id':             bmod.User.objects.get(username='Kevbo').id,
     'payment_processed_by':    bmod.User.objects.get(username='Kevbo')},
    {'date':                    datetime.date.today() - datetime.timedelta(4),
     'phone':                   '801-345-1122',
     'customer':                bmod.User.objects.get(username='TyCool4School'),
     'payment_processed_by':    bmod.User.objects.get(username='Kevbo')},
    {'date':                    datetime.date.today(),
     'phone':                   '801-345-1122',
     'customer':                bmod.User.objects.get(username='TyCool4School'),
     'payment_processed_by':    bmod.User.objects.get(username='Kevbo')}

]:

    t = bmod.Transaction()
    for k, v in data.items():
        setattr(t, k, v)
    t.save()

print('Transactions initialized')


#              CREATE CATEGORIES            #

for data in [{'name': 'Toys'}, {'name': 'Housewares'}, {'name': 'Clothing'}]:

    c = bmod.Category()
    for k, v in data.items():
        setattr(c, k, v)
    c.save()

print('Categories initialized')


#          CREATE CLOTHING DETAILS        #

for data in [{'size': 'Large', 'gender': 'M', 'color': 'Periwinkle'}]:

    cd = bmod.Clothing_Detail()
    for k, v in data.items():
        setattr(cd, k, v)
    cd.save()

print('Clothing Details initialized')


#           CREATE ITEMS            #

for data in [
    {'name':                "Model Mayflower",
     'description':         "A scale model of the goodship Mayflower.",
     'serial_number':       "M0001",
     'value':               4000.00,
     'creator':             bmod.User.objects.get(username='TyCool4School'),
     'photo_id':            14}
]:

    i = bmod.Item()
    for k, v in data.items():
        setattr(i, k, v)
    i.save()

print('Items initialized')


#           CREATE Sale ItemS            #

for data in [
    {'quantity_on_hand':    "30",
     'shelf_location':      "C-7.1",
     'price':               4.99,
     'manufacturer':        "Maker Inc.",
     'name':                "Quill",
     'description':         "A fine feathered font-formatting device.",
     'serial_number':       "C4111",
     'value':               0.99,
     'photo_id':            3},
    {'quantity_on_hand':    "40",
     'shelf_location':      "T-32.1",
     'price':               7.00,
     'manufacturer':        "Fine and Sons",
     'name':                "Playing Cards",
     'description':         "Colonial cards with a variety of alligorical faces.",
     'serial_number':       "T4445",
     'value':               2.50,
     'photo_id':            4},
    {'quantity_on_hand':    "15",
     'shelf_location':      "T-33.1",
     'price':               35.00,
     'manufacturer':        "Fine and Sons",
     'name':                "Child's Drum",
     'description':         "A fine continental drum that is modeled after those used by the revolutionaries.",
     'serial_number':       "T4345",
     'value':               10.00,
     'photo_id':            5},
    {'quantity_on_hand':    "50",
     'shelf_location':      "M-12.1",
     'price':               23.00,
     'manufacturer':        "Fine and Sons",
     'name':                "Virginia Map",
     'description':         "A map drawn up in 1734 showing the coast of colonial Virigina.",
     'serial_number':       "M3949",
     'value':               3.00,
     'photo_id':            9},
    {'quantity_on_hand':    "4",
     'shelf_location':      "M-23.1",
     'price':               129.00,
     'manufacturer':        "Fine and Sons",
     'name':                "China Teapot",
     'description':         "A piece of fine china created to celebrate the colonist's definace.",
     'serial_number':       "M5278",
     'value':               20.00,
     'photo_id':            10},
    {'quantity_on_hand':    "100",
     'shelf_location':      "T-28.9",
     'price':               7.50,
     'manufacturer':        "Fine and Sons",
     'name':                "Wooden Top",
     'description':         "A colonial toy designed for hours of fun.",
     'serial_number':       "T2050",
     'value':               0.50,
     'photo_id':            11},
    {'quantity_on_hand':    "15",
     'shelf_location':      "C-34.2",
     'price':               125.50,
     'manufacturer':        "Fine and Sons",
     'name':                "Fine Wallet",
     'description':         "A woman's wallet with a finely hand-stitched pattern.",
     'serial_number':       "C3050",
     'value':               30.00,
     'photo_id':            12},
    {'quantity_on_hand':    "20",
     'shelf_location':      "C-34.2",
     'price':               12.50,
     'manufacturer':        "MusicMan Tunes",
     'name':                "Martial Fife",
     'description':         "A fife designed using the pattern of those played in the continental army. Downright musical.",
     'serial_number':       "C3050",
     'value':               5.00,
     'photo_id':            6},
    {'quantity_on_hand':    "15",
     'shelf_location':      "C-34.2",
     'price':               25.50,
     'manufacturer':        "Fine and Sons",
     'name':                "Lavendar Water",
     'description':         "A variety of bath scent that has been used since the founding of our nation. Wash up and smell like a rebel!",
     'serial_number':       "C3050",
     'value':               2.00,
     'photo_id':            13},
]:

    sp = bmod.Sale_Item()
    for k, v in data.items():
        setattr(sp, k, v)
    sp.save()

print('Sale Items initialized')


#           CREATE Custom ItemS            #

for data in [
    {'production_time':     "13",
     'price':               35.00,
     'name':                "Embroidered Handkerchief",
     'description':         "A finely made cotton hankerchief that can be decorated with a monogram or message.",
     'serial_number':       "C9349",
     'value':               4.00,
     'creator':             bmod.Vendor.objects.get(username='2Tyler2Quit'),
     'required_info':       'The message to be sewn into the hankerchief',
     'photo_id':            8}
]:

    cp = bmod.Custom_Item()
    for k, v in data.items():
        setattr(cp, k, v)
    cp.save()

print('Custom Items initialized')


#           CREATE ORDER FORMS            #

for data in [
    {'customer_info':
        'I admire you deeply and enjoy our long walks together on the beach. May this hankerchief ever remind you of me.'}
]:

    of = bmod.Order_Form()
    for k, v in data.items():
        setattr(of, k, v)
    of.save()

print('Order Forms initialized')


#           CREATE SALE           #

for data in [
    {'transaction':  bmod.Transaction.objects.get(customer_id=bmod.User.objects.get(username='CodyingAllNight')),
     'amount':          35.00,
     'quantity':        1,
     'sale_item':       bmod.Custom_Item.objects.first(),
     'order_form':      bmod.Order_Form.objects.first()},
    {'transaction':     bmod.Transaction.objects.get(customer_id=bmod.User.objects.get(username='2Tyler2Quit')),
     'amount':          15.00,
     'quantity':        3,
     'sale_item':       bmod.Sale_Item.objects.get(name='Quill')}
]:

    si = bmod.Sale()
    for k, v in data.items():
        print(k,v)
        setattr(si, k, v)
    si.save()

print('Sales initialized')


#           CREATE Rental ItemS          #

for data in [
    {'quantity_on_hand':    "1",
     'shelf_location':      "D-5.1",
     'name':                "Robes of Sir Gove",
     'description':         "Professor Gove's very own robe.",
     'serial_number':       "R4516",
     'value':               20.99,
     'owner':               bmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            2,
     'clothing_detail_id':  bmod.Clothing_Detail.objects.first().id,
     'price_per_day':       5.99},
    {'quantity_on_hand':    "0",
     'shelf_location':      "C-3.1",
     'name':                "Colonial Musket",
     'description':         "Authentic. Appears to have been dropped. Never fired.",
     'serial_number':       "R3256",
     'value':               2304.00,
     'owner':               bmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            7,
     'price_per_day':       20.99},
    {'quantity_on_hand':    "0",
     'shelf_location':      "C-4.5",
     'name':                "Pickle Jar",
     'description':         "Taste that sweet dill goodness. Do not consume.",
     'serial_number':       "R5678",
     'value':               12.00,
     'owner':               bmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            16,
     'price_per_day':       15.00},
    {'quantity_on_hand':    "0",
     'shelf_location':      "C-3.5",
     'name':                "Okra Jar",
     'description':         "Taste that sweet okra goodness. Do not consume.",
     'serial_number':       "R8905",
     'value':               12.00,
     'owner':               bmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            17,
     'price_per_day':       1.00},
    {'quantity_on_hand':    "0",
     'shelf_location':      "C-3.5",
     'name':                "Pumpkin Syrup",
     'description':         "Actually disgusting. Should have been thrown out a long time ago.",
     'serial_number':       "R7890",
     'value':               15.00,
     'owner':               bmod.User.objects.get(username='GoveByDaPound'),
     'photo_id':            18,
     'price_per_day':       16.00}
]:

    ra = bmod.Rental_Item()
    for k, v in data.items():
        setattr(ra, k, v)
    ra.save()

print('Rental Items initialized')


#           CREATE RENTALS         #

for data in [
    {'transaction_id':          bmod.Transaction.objects.get(customer_id=bmod.User.objects.get(username='Kevbo')).id,
     'amount':                  bmod.Rental_Item.objects.get(serial_number='R3256').price_per_day*4,
     'rental_item':             bmod.Rental_Item.objects.get(serial_number='R3256'),
     'checkout_by_date':        bmod.Transaction.objects.get(customer_id=bmod.User.objects.get(username='Kevbo')).date + datetime.timedelta(14),
     'checkout_price':          0,
     'date_out':                bmod.Transaction.objects.get(customer_id=bmod.User.objects.get(username='Kevbo')).date,
     'date_due':                datetime.date.today() - datetime.timedelta(1),
     'duration':                4,
     'discount_percent':        1.00},
    {'transaction_id':          bmod.Transaction.objects.get(date=datetime.date.today()).id,
     'amount':                  bmod.Rental_Item.objects.get(serial_number='R4516').price_per_day*6,
     'rental_item':             bmod.Rental_Item.objects.get(serial_number='R4516'),
     'checkout_by_date':        bmod.Transaction.objects.get(date=datetime.date.today() - datetime.timedelta(4)).date + datetime.timedelta(14),
     'checkout_price':          0,
     'date_out':                bmod.Transaction.objects.get(date=datetime.date.today() - datetime.timedelta(4)).date,
     'date_due':                datetime.date.today() - datetime.timedelta(2),
     'duration':                6,
     'discount_percent':        0.25},
    {'transaction_id':          bmod.Transaction.objects.get(date=datetime.date.today()).id,
     'amount':                  bmod.Rental_Item.objects.get(serial_number='R5678').price_per_day*2*Decimal('0.20'),
     'rental_item':             bmod.Rental_Item.objects.get(serial_number='R5678'),
     'checkout_by_date':        datetime.date.today() - datetime.timedelta(100) + datetime.timedelta(14),
     'checkout_price':          bmod.Rental_Item.objects.get(serial_number='R5678').price_per_day*2*Decimal('0.80'),
     'date_out':                datetime.date.today() - datetime.timedelta(99),
     'date_due':                datetime.date.today() - datetime.timedelta(97),
     'duration':                2,
     'discount_percent':        0},
    {'transaction_id':          bmod.Transaction.objects.get(date=datetime.date.today()).id,
     'amount':                  bmod.Rental_Item.objects.get(serial_number='R8905').price_per_day*1*Decimal('0.20'),
     'rental_item':             bmod.Rental_Item.objects.get(serial_number='R8905'),
     'checkout_by_date':        datetime.date.today() - datetime.timedelta(70) + datetime.timedelta(14),
     'checkout_price':          bmod.Rental_Item.objects.get(serial_number='R8905').price_per_day*1*Decimal('0.80'),
     'date_out':                datetime.date.today() - datetime.timedelta(65),
     'date_due':                datetime.date.today() - datetime.timedelta(64),
     'duration':                1,
     'discount_percent':        0},
    {'transaction_id':          bmod.Transaction.objects.get(customer_id=bmod.User.objects.get(username='Kevbo')).id,
     'amount':                  bmod.Rental_Item.objects.get(serial_number='R7890').price_per_day*1*Decimal('0.20'),
     'rental_item':             bmod.Rental_Item.objects.get(serial_number='R7890'),
     'checkout_by_date':        datetime.date.today() - datetime.timedelta(40) + datetime.timedelta(14),
     'checkout_price':          bmod.Rental_Item.objects.get(serial_number='R7890').price_per_day*1*Decimal('0.80'),
     'date_out':                datetime.date.today() - datetime.timedelta(33),
     'date_due':                datetime.date.today() - datetime.timedelta(32),
     'duration':                1,
     'discount_percent':        0},
]:

    ri = bmod.Rental()
    for k, v in data.items():
        setattr(ri, k, v)
    ri.amount = ri.amount * Decimal((1-ri.discount_percent))
    ri.save()

print('Rentals initialized')


#           CREATE RENTAL RETURNS           #

for data in [
    {'rental':              bmod.Rental.objects.get(date_due=datetime.date.today() - datetime.timedelta(2)),
     'date_returned':       datetime.date.today() - datetime.timedelta(1),
     'return_condition':    'It looks like someone lit it on fire.',
     'handled_by':          bmod.Employee.objects.get(username='Reverend')}
]:

    rr = bmod.Rental_Return()
    for k, v in data.items():
        setattr(rr, k, v)
    rr.save()

print('Rental Returns initialized')


#           CREATE FEES           #

delta = bmod.Rental_Return.objects.first().date_returned - bmod.Rental.objects.get(id=bmod.Rental_Return.objects.first().rental.id).date_due

for data in [
    {'transaction':     bmod.Transaction.objects.get(date=datetime.date.today()),
     'rental_return':   bmod.Rental_Return.objects.first(),
     'days_late':       delta.days}
]:
    lf = bmod.Late_Fee()
    for k, v in data.items():
        setattr(lf, k, v)
    lf.amount = bmod.Rental_Item.objects.get(serial_number='R4516').price_per_day*lf.days_late
    lf.save()

for data in [
    {'transaction':     bmod.Transaction.objects.get(date=datetime.date.today()),
     'rental_return':   bmod.Rental_Return.objects.first(),
     'amount':          400.34,
     'description':     'The back seems to have a symbol burned into it. Who knows what it means.'}
]:

    df = bmod.Damage_Fee()
    for k, v in data.items():
        setattr(df, k, v)
    df.save()

print('Fees initialized')


#           CREATE EVENTS            #

for data in [
    {'name':                "The Continental Feast",
     'description':         "An earthy afternoon where you can kick back and enjoy some of the finest period food and drink.",
     'start_date':          datetime.datetime.now(),
     'end_date':            datetime.date.today() + datetime.timedelta(2),
     'map_file_name':       "/static/app_events/media/map-1.jpg",
     'venue_name':          "Century Park",
     'discount_code':       "",
     'address_id':          4,
     'public_event_id':     1},
    {'name':                "Rebels and Redcoats!",
     'description':         "Come one, come all! See the armies of the Colonies and the Empire parade in all of their finery.",
     'start_date':          datetime.date.today() + datetime.timedelta(52),
     'end_date':            datetime.date.today() + datetime.timedelta(57),
     'map_file_name':       "/static/app_events/media/map-2.png",
     'venue_name':          "Table-Rock Park",
     'discount_code':       "",
     'address_id':          5,
     'public_event_id':     1},
]:

    i = bmod.Event()
    for k, v in data.items():
        setattr(i, k, v)
    i.save()

print('Events initialized')


#           CREATE AREAS            #

for data in [
    {'name':             "Food",
     'description':      "Delicious eats, made fresh for you.",
     'place_number':     1,
     'coordinator_id':   1,
     'event_id':         1,
     'supervisor_id':    3},
    {'name':             "Drink",
     'description':      "A sampling of all of the non-alcoholic specialties of the era.",
     'place_number':     2,
     'coordinator_id':   1,
     'event_id':         1,
     'supervisor_id':    2},
    {'name':             "Arm Yourselves!",
     'description':      "An exhibit displaying the variety of weaponry employed by both sides in the colonial conflict.",
     'place_number':     1,
     'coordinator_id':   1,
     'event_id':         2,
     'supervisor_id':    3},
    {'name':             "The Forge",
     'description':      "Demonstrations of the various techniques used in creating the different instruments of battle.",
     'place_number':     3,
     'coordinator_id':   1,
     'event_id':         2,
     'supervisor_id':    3},
]:

    i = bmod.Area()
    for k, v in data.items():
        setattr(i, k, v)
    i.save()

print('Areas initialized')

#           CREATE EXPECTED SALE ITEM            #

for data in [
    {'name':            "Pickled Dill Slices",
     'description':     "Garden-fresh taste with the perfect crunch.",
     'low_price':       8.35,
     'high_price':      15.45,
     'photo_id':        16,
     'event_id':        1},
    {'name':            "Pickled Okra",
     'description':     "Garden-fresh and blemish-free okra is pickled to perfection with a crispy, light, and spicy taste.",
     'low_price':       9.95,
     'high_price':      11.00,
     'photo_id':        17,
     'event_id':        1},
    {'name':            "Pumpkin Spice Syrup",
     'description':     "Make a splash at your table this year with delicious pumpkin spice syrup.",
     'low_price':       15.25,
     'high_price':      18.99,
     'photo_id':        18,
     'event_id':        1}
]:

    i = bmod.Expected_Sale_Item()
    for k, v in data.items():
        setattr(i, k, v)
    i.save()

print('Expected Sale Item(s) initialized')

transaction = bmod.Transaction.objects.get(date=datetime.date.today())

print(transaction.customer.get_full_name())

for line_item in transaction.rental_set.all():
    print(line_item.rental_item.name)
    print(line_item.amount)

for line_item in transaction.sale_set.all():
    print(line_item.sale_item.name)
    print(line_item.amount)

for line_item in transaction.damage_fee_set.all():
    print(line_item.rental_return.rental.rental_item.name)
    print(line_item.amount)
