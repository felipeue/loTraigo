"""
All the test for our loTraigo application
"""
# === Imports ===
from django.test import TestCase
from ltApp.models import *
import nose.tools as nt
from django.contrib.auth.models import User
from amazon.api import AmazonAPI


# === Test insert all models whit respective relations ===
class InsertTest(TestCase):
    # Set user for test
    def setUp(self):
        self.usuario = User.objects.create_user(username="feli",
                                                email='feli@almacencooperativo.cl',
                                                first_name='felipe',
                                                last_name='rios')

    # ===Test insert UserLt Model===
    def test_models(self):
        # Test insert UserLt model
        usuariolt = UserLt.objects.create(userOrigin=self.usuario,
                                          address="Isla de maipo sapbe",
                                          phone='+56971397675',
                                          rut='7552796-9')

        nt.assert_equal(usuariolt.userOrigin, self.usuario)
        nt.assert_equal(usuariolt.address, "Isla de maipo sapbe")
        nt.assert_equal(usuariolt.phone, "+56971397675")
        nt.assert_equal(usuariolt.rut, "7552796-9")
        # ===Test insert Flight model===
        # create new user
        uViajero = User.objects.create_user(username='viajero',
                                            email='feli@almacencooperativo.cl',
                                            first_name='viajero',
                                            last_name='viaje')

        # create new UserLt, this time is a Traveller user
        usuarioLtV = UserLt.objects.create(userOrigin=uViajero,
                                           address='Isla de maipo sapbe',
                                           phone='+56971397675',
                                           rut='18346436-1')
        # ===Insert Flight data===
        vuelo = Flight.objects.create(traveller=usuarioLtV,
                                      origin='NZ',
                                      destiny='AF',
                                      dateFly='2015-11-10',
                                      dateReturn='2015-11-20')

        nt.assert_equal(vuelo.traveller, usuarioLtV)
        nt.assert_equal(vuelo.origin, "NZ")
        nt.assert_equal(vuelo.destiny, "AF")
        nt.assert_equal(vuelo.dateFly, "2015-11-10")
        nt.assert_equal(vuelo.dateReturn, "2015-11-20")

        # ===Test insert Quotation model===
        cotizacion = Quotation.objects.create(userLtQ=usuariolt,
                                              orderNumber='123456789',
                                              totalPrice='100000',
                                              date='2015-11-10',
                                              description='Compra test')

        nt.assert_equal(cotizacion.userLtQ, usuariolt)
        nt.assert_equal(cotizacion.orderNumber, "123456789")
        nt.assert_equal(cotizacion.totalPrice, "100000")
        nt.assert_equal(cotizacion.date, "2015-11-10")
        nt.assert_equal(cotizacion.description, "Compra test")

        # ===Test insert Publication model===
        publicacion = Publication.objects.create(quotation=cotizacion,
                                                 state=True,
                                                 benefit='15000')

        nt.assert_equal(publicacion.quotation, cotizacion)
        nt.assert_equal(publicacion.state, True)
        nt.assert_equal(publicacion.benefit, "15000")

        # ===Test insert Product model===
        # add credentials of Amazon API and load data of product
        amazon = AmazonAPI('AKIAIYBKV2XTJIHFPCXQ', 'ipwqJAnuEiIv89t5OZEttmvrKb6X1qa+TwisgExh', 'lotraigo-21')
        product = amazon.lookup(ItemId="B00G2TK76A")
        price = product.price_and_currency[0]
        pricetotal = price + 1000
        url = product.offer_url
        urlimage = product.large_image_url
        title = product.title
        category = product.binding
        dimensions = product.get_attributes(
            ['ItemDimensions.Width', 'ItemDimensions.Height', 'ItemDimensions.Length', 'ItemDimensions.Weight'])
        width = dimensions.values()[0]
        weigth = dimensions.values()[3]
        length = dimensions.values()[2]
        heigth = dimensions.values()[1]
        # Insert data from Amazon API in a Model
        producto = Product.objects.create(quotation=cotizacion,
                                          price=price,
                                          priceTotal=pricetotal,
                                          url=url,
                                          urlImage=urlimage,
                                          title=title,
                                          category=category,
                                          widthProduct=width,
                                          weigthProduct=weigth,
                                          lengthProduct=length,
                                          heigthProduct=heigth,
                                          location='USA')
        # Validate
        nt.assert_equal(producto.quotation, cotizacion)
        nt.assert_equal(producto.price, price)
        nt.assert_equal(producto.priceTotal, pricetotal)
        nt.assert_equal(producto.url, url)
        nt.assert_equal(producto.urlImage, urlimage)
        nt.assert_equal(producto.title, title)
        nt.assert_equal(producto.category, category)
        nt.assert_equal(producto.widthProduct, width)
        nt.assert_equal(producto.weigthProduct, weigth)
        nt.assert_equal(producto.lengthProduct, length)
        nt.assert_equal(producto.heigthProduct, heigth)
        nt.assert_equal(producto.location, "USA")

        # ===Test insert Sale model===
        venta=Sale.objects.create(quotation=cotizacion,
                                  numberSale='123456789',
                                  date='2015-11-10',
                                  traveller=usuarioLtV)

        nt.assert_equal(venta.quotation, cotizacion)
        nt.assert_equal(venta.numberSale, "123456789")
        nt.assert_equal(venta.date, "2015-11-10")
        nt.assert_equal(venta.traveller, usuarioLtV)