import re

from mext.provider import Provider

from .p_asurascans_com import AsuraScansCom
from .p_mangadex_org import MangadexOrg
from .p_reaperscans_com import ReaperScansCom


ALL_PROVIDERS = [
    {
        "name": "AsuraScans",
        "regex": r".*(asura\.gg|asurascans\.com).*",
        "class": AsuraScansCom
    },
    {
        "name": "ReaperScans",
        "regex": r".*(reaperscans\.com).*",
        "class": ReaperScansCom
    },
    {
        "name": "MangaDex",
        "regex": r".*(mangadex\.org).*",
        "class": MangadexOrg
    }
]


def get_provider_instance(name=None, netloc=None) -> Provider:
    for provider_info in ALL_PROVIDERS:
        if (name and provider_info['name'] == name) or \
                (netloc and re.search(provider_info['regex'], netloc)):
            ProviderClass = provider_info['class']
            return ProviderClass(
                name=provider_info['name'],
                siteUrl=netloc,
            )
    raise ValueError("No provider for provided netloc {}".format(netloc))


__all__ = [
    get_provider_instance
]
