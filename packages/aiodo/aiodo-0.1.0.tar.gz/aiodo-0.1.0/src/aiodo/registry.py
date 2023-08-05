from importlib.metadata import entry_points


def devices():
    return entry_points(group="aiodo.device")


def device(name):
    return devices()[name]
