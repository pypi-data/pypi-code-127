from django.apps import AppConfig

__title__ = (
    "fobi.contrib.plugins.form_elements.fields." "hidden_model_object.apps"
)
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2014-2021 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"
__all__ = ("Config",)


class Config(AppConfig):
    """Config."""

    name = "fobi.contrib.plugins.form_elements.fields.hidden_model_object"
    label = "fobi_contrib_plugins_form_elements_fields_hidden_model_object"
