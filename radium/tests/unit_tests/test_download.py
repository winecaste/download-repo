import os

import aiohttp
import pytest

from radium.src.main import download_repo


@pytest.mark.asyncio
async def test_download_repo(tmpdir):
    url = "https://gitea.radium.group/radium/project-configuration/archive/master.zip"
    dir_path = str(tmpdir)
    file_path = await download_repo(url, dir_path, "test")
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)
    assert os.path.getsize(file_path) > 0

@pytest.mark.asyncio
async def test_download_repo_invalid_url(tmpdir):
    url = "https://example.com/nonexistent"
    dir_path = str(tmpdir)
    with pytest.raises(aiohttp.ClientResponseError):
        await download_repo(url, dir_path, "test")

