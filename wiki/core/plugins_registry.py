from django.utils.importlib import import_module
_cache = {}

_settings_forms = []

class BasePlugin(object):
    #settings_form = YourForm
    pass

def register(PluginClass):
    """
    Register a plugin class. This function will call back your plugin's
    constructor.
    """
    if PluginClass in _cache.keys():
        raise Exception("Plugin class already registered")
    _cache[PluginClass] = PluginClass()
    
    settings_form = getattr(PluginClass, 'settings_form', None)
    if settings_form:
        if isinstance(settings_form, basestring):
            klassname = settings_form.split(".")[-1]
            modulename = ".".join(settings_form.split(".")[:-1])
            form_module = import_module(modulename)
            settings_form = getattr(form_module, klassname)
        _settings_forms.append(settings_form)
        