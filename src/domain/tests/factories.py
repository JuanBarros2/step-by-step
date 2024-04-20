import datetime
import random

import factory

from domain.step import Algorithm, AlgorithmInfo, Library, Step


class StepFactory(factory.Factory):
    class Meta:
        model = Step


class AlgorithmInfoFactory(factory.Factory):
    class Meta:
        model = AlgorithmInfo

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("sentence", nb_words=50)
    created_at = factory.Faker(
        "date",
        end_datetime=datetime.date.today(),
    )


class AlgorithmFactory(factory.Factory):
    class Meta:
        model = Algorithm

    steps = factory.RelatedFactoryList(StepFactory, size=lambda: random.randint(1, 5))
    info = factory.SubFactory(AlgorithmInfoFactory)


class LibraryFactory(factory.Factory):
    class Meta:
        model = Library

    algorithms = factory.RelatedFactoryList(
        AlgorithmInfoFactory, size=lambda: random.randint(1, 5)
    )
