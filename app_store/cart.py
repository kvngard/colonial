from django.db.models import Q
import app_base.models as mod


def save_cart(request, cart):
    request.session['shopping_cart'] = cart.to_json()

    request.session.modified = True


def get_cart(request):
    cart = Cart()

    if 'shopping_cart' not in request.session:
        save_cart(request, cart)
    else:
        cart.from_json(request.session['shopping_cart'])

    return cart


class Cart:
    'Defines various methods and properties of a shopping cart.'

    def __init__(self, json=None):
        self.rentals = {}
        self.sales = {}

        if json is not None:
            pass


    def to_json(self):
        json_string = { 'rentals':[],'sales':[] }

        for r in self.rentals.values():
            json_string['rentals'].append({'duration': r.duration, 'id': r.rental_item.id})

        for s in self.sales.values():
            json_string['sales'].append({'quantity': s.quantity, 'id': s.sale_item.id})

        return json_string


    def from_json(self, json):

        for r in json['rentals']:
            item = mod.Rental_Item.objects.get(id=r['id'])
            rental = mod.Rental.create_rental(item, int(r['duration']))
            self.rentals[item.id] = rental

        for s in json['sales']:
            item = mod.Sale_Item.objects.get(id=s['id'])
            sale = mod.Sale.create_sale(item, int(s['quantity']))
            self.sales[item.id] = sale


    def get_checkout_total(self):
        total = 0

        for rental in self.rentals.values():
            total += rental.amount

        for sale in self.sales.values():
            total += sale.amount

        return total


    def add_to_cart(self, item, quantity=None, duration=None):
        item = mod.Item.cast(item)

        print(item)
        print(duration)

        if duration is '':
            if item.id in self.sales:
                self.sales[item.id].quantity += int(quantity)
            else:
                sale = mod.Sale.create_sale(item, quantity)
                self.sales[item.id] = sale
        else:
            rental = mod.Rental.create_rental(item, duration)
            self.rentals[item.id] = rental

        print(self)


    def delete_from_cart(self, id):

        if id in self.rentals: del self.rentals[id]
        if id in self.sales: del self.sales[id]

        return
