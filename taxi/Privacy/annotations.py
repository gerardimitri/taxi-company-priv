from django.db import models
from rest_framework.utils import model_meta

def get_default_field_names(model_info):
        """
        Helper class for getting model field names
        """
        return (
            [model_info.pk.name] +
            list(model_info.fields) +
            list(model_info.forward_relations)
        )
def get_model_fields(model:models.Model):
    """
    Returns a list that contains the name of each field of the model, sorted.
    Example:
    
    class Dog(models.Model):
        name = ...
        color = ...
    
    >field_names= get_model_fields(Dog)
    >['id','name','color']
    Remember, that Django by default creates a id field in each model :)
    """
    l =get_default_field_names(model_meta.get_field_info(model))
    l.sort()
    return l

class PrivacyAnnotation:
    @classmethod
    def get_fields(cls):
          """
          Returns a list that contains the name of each field in the class
          """
          l = [a for a in cls.__dict__ if "__" not in a]
          l.sort()
          return l
