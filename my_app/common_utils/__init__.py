from werkzeug.utils import import_string


class Dict2Obj:
    def __init__(self, **entries):
        self.__dict__.update(entries)


class Object2Dict(dict):
    def __init__(self, defaults=None):
        dict.__init__(self, defaults or {})

    def from_object(self, obj):
        string_types = (str,)
        if isinstance(obj, string_types):
            obj = import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
        return self