from __future__ import annotations

import pytest

import comictalker.comiccacher
from testing.comicdata import search_results


def test_create_cache(options, mock_version):
    settings, definitions = options
    comictalker.comiccacher.ComicCacher(settings.runtime_config.user_cache_dir, mock_version[0])
    assert (settings.runtime_config.user_cache_dir).exists()


def test_search_results(comic_cache):
    comic_cache.add_search_results(
        "test",
        "test search",
        search_results,
    )
    assert search_results == comic_cache.get_search_results("test", "test search")


@pytest.mark.parametrize("series_info", search_results)
def test_series_info(comic_cache, series_info):
    comic_cache.add_series_info(series_record=series_info, source_name="test")
    vi = series_info.copy()
    del vi["description"]
    del vi["image_url"]
    cache_result = comic_cache.get_series_info(series_id=series_info["id"], source_name="test")
    del cache_result["description"]
    del cache_result["image_url"]
    assert vi == cache_result
