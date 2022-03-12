from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

from actual_repository import ActualRepository
from actual_service import ActualService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    repository = providers.Singleton(ActualRepository)
    service = providers.Factory(ActualService,repository=repository)


@inject
def main(service: ActualService = Provide[Container.service]):
    print('actual value is:' + str(service.get_value()))

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    main()