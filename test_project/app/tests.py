from django.test import TestCase
from test_project.app.models import Test


class TypeidFieldTest(TestCase):
    def test_simple(self):
        t1 = Test.objects.create()
        self.assertEqual(
            26, len(t1.id)
        )  # default length, e.g. 2x4y6z8a0b1c2d3e4f5g6h7j8k
        self.assertEqual(
            30, len(t1.override)
        )  # with prefix, e.g. pfx_2x4y6z8a0b1c2d3e4f5g6h7j8k

        t2 = Test.objects.create()
        self.assertNotEqual(t1.id, t2.id)
        self.assertNotEqual(t1.override, t2.override)

        self.assertRegex(t1.override, "pfx_[0-9a-z]{26}")
        self.assertRegex(t2.override, "pfx_[0-9a-z]{26}")
