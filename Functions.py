
def di (tp):
    return [obj for obj in dir(tp) if not obj.startswith("__")]

