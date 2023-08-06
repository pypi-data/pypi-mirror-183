import typing_extensions

from chain_app_client_sdk.paths import PathValues
from chain_app_client_sdk.apis.paths.main_pool_get_pool_size_history import MainPoolGetPoolSizeHistory

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.MAIN_POOL_GET_POOL_SIZE_HISTORY: MainPoolGetPoolSizeHistory,
    }
)

path_to_api = PathToApi(
    {
        PathValues.MAIN_POOL_GET_POOL_SIZE_HISTORY: MainPoolGetPoolSizeHistory,
    }
)
