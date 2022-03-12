import pytest
from unittest.mock import MagicMock
from actual_service import ActualService
from actual_repository import ActualRepository

class TestActualService:
    @pytest.fixture
    def repository(self):
        return MagicMock()

    @pytest.fixture   
    def service(self, repository):
        return ActualService(repository)

    def test_get_value(self, service:ActualService):
        # act
        result = service.get_value()
        # assert
        assert result == 1

    def test_get_repository_value_actual(self):
        # arrange
        repository = ActualRepository()
        service = ActualService(repository)
        # act
        result = service.get_repository_value()
        # assert
        assert result == 2
    
    def test_get_repository_value_mock(self, service, repository: ActualRepository):
        # arrange
        mock_get_value = MagicMock(return_value=3)
        repository.get_value = mock_get_value
        # act
        result = service.get_repository_value()
        # assert
        assert result == 3
        mock_get_value.assert_called_once()