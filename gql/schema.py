from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoConnectionField
from .persons.mutations import PersonCreate, PersonDelete

from people.models import Person
from .persons.types import PersonType


class Query(ObjectType):
    persons = DjangoConnectionField(PersonType)
    person = Field(PersonType, id=Argument(ID, required=True))

    def resolve_notes(root, info, **kwargs):
        return Person.objects.all()

    def resolve_note(root, info, **kwargs):
        return Person.objects.get(id=kwargs.get('id'))


class Mutation(ObjectType):
    person_create = PersonCreate.Field()
    person_delete = PersonDelete.Field()


schema = Schema(query=Query, mutation=Mutation)