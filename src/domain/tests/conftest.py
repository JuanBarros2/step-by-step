from pytest_factoryboy import register

from domain.tests import factories

register(factories.AlgorithmInfoFactory)
register(factories.AlgorithmFactory)
register(factories.StepFactory)
