import typing_extensions

from chain_app_client_sdk.apis.tags import TagValues
from chain_app_client_sdk.apis.tags.main_pool_api import MainPoolApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.MAIN_POOL: MainPoolApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.MAIN_POOL: MainPoolApi,
    }
)
