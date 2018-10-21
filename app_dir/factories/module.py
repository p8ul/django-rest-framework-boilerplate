import factory
from faker import Factory
from ..core.loading import get_model

faker = Factory.create()


class ModuleFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('module', 'Module')

    name = faker.name()
    description = faker.text()
