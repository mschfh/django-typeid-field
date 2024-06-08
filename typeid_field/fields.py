from django.db import models
import re

from typeid import TypeID


class TypeidField(models.CharField):
    def __init__(self, *args, **kwargs) -> None:
        self.prefix = kwargs.pop("prefix", None)
        if self.prefix and len(self.prefix) > 63:
            raise ValueError("Prefix can't be longer than 63 characters.")
        if self.prefix and not re.match(r"^([a-z]([a-z_]{0,61}[a-z])?)?$", self.prefix):
            raise ValueError("Invalid prefix format.")
        kwargs["max_length"] = kwargs.pop(
            "max_length", (len(self.prefix or "") + 1 + 26)
        )  # prefix length + 1 (separator) + 26
        kwargs["default"] = self.typeid

        super(TypeidField, self).__init__(*args, **kwargs)

    def typeid(self):
        return str(TypeID(prefix=self.prefix))

    def get_internal_type(self):
        return "CharField"
