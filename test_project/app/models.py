from django.db import models

from typeid_field import TypeidField


class Test(models.Model):
    id = TypeidField(primary_key=True, editable=False)
    override = TypeidField(prefix="pfx")
