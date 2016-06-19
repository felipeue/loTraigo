from django.test import TestCase
from ltApp.models import *
import nose.tools as nt
from django.contrib.auth.models import User


class InsertTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='feli',
                                                email='feli@almacencooperativo.cl',
                                                first_name='felipe',
                                                last_name='rios')

    def test_user(self):
        nt.assert_equal(self.usuario.username, "feli")
        nt.assert_equal(self.usuario.email, "feli@almacencooperativo.cl")
        nt.assert_equal(self.usuario.first_name, "felipe")
        nt.assert_equal(self.usuario.last_name, "rios")