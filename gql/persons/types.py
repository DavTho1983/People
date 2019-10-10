from graphene_django import DjangoObjectType
from people.models import Person


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        only_fields = (
            'id',
            'first_name',
            'last_name',
            'address',
        )
        use_connection = True
