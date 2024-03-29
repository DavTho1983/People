from graphene import Boolean, Field, ID, InputObjectType, Mutation, String
from rest_framework import serializers
from people.models import Person
from .types import PersonType


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'address'
        )


class PersonInputType(InputObjectType):
    first_name = String()
    last_name = String()
    address = String()


class PersonCreate(Mutation):
    class Arguments:
        input = PersonInputType(required=True)
    person = Field(PersonType)

    @classmethod
    def mutate(cls, root, info, **data):
        serializer = PersonSerializer(data=data.get('input'))
        serializer.is_valid(raise_exception=True)
        return PersonCreate(person=serializer.save())


class PersonEdit(Mutation):
    class Arguments:
        id = ID(required=True)
        input = PersonInputType(required=True)
    ok = Boolean()

    @classmethod
    def mutate(cls, root, info, **data):
        serializer = PersonSerializer(data=data.get('input'))
        serializer.is_valid(raise_exception=True)
        person = Person.objects.get(id=data.get('id'))
        person.first_name = serializer.data['first_name']
        person.last_name = serializer.data['last_name']
        person.address = serializer.data['address']
        person.save()
        return PersonEdit(ok=True)


class PersonDelete(Mutation):
    class Arguments:
        id = ID(required=True)
    ok = Boolean()

    @classmethod
    def mutate(cls, root, info, **data):
        person = Person.objects.get(id=data.get('id'))
        person.delete()
        return PersonDelete(ok=True)