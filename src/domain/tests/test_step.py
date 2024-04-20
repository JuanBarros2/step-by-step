from datetime import datetime, timedelta

from domain.step import Algorithm, AlgorithmInfo
from domain.tests.factories import AlgorithmFactory


class TestAlgorithmInfo:
    def test_creating_basic_entity(self, algorithm_info):
        assert isinstance(algorithm_info, AlgorithmInfo)


class TestAlgorithm:
    def test_creating_basic_entity(self, algorithm):
        assert isinstance(algorithm, Algorithm)

    def test_sorting_entities_based_on_algorithm_info(
        self,
        algorithm_factory: AlgorithmFactory,
    ):
        now = datetime.now()
        first_algorithm = algorithm_factory(info__created_at=now - timedelta(days=3))
        second_algorithm = algorithm_factory(info__created_at=now - timedelta(days=2))
        third_algorithm = algorithm_factory(info__created_at=now - timedelta(days=1))

        unsorted_list = [third_algorithm, first_algorithm, second_algorithm]
        ordered_list = sorted(unsorted_list)

        assert ordered_list == [first_algorithm, second_algorithm, third_algorithm]


class TestUser:
    def test_creating_basic_entity(self):
        pass
