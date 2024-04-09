import asyncio
import hashlib
import os
from tempfile import TemporaryDirectory

import aiohttp


async def download_repo(url: str, dir_path: str, postfix: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise aiohttp.ClientResponseError(response.request_info, response.history, status=response.status,
                                                  message="Failed to download")
            filename = os.path.splitext(os.path.basename(url))
            repo_name = filename[0] + '_' + postfix + filename[1]
            file_path = os.path.join(dir_path, repo_name)
            with open(file_path, "wb") as f:
                async for data in response.content.iter_chunked(4096):
                    f.write(data)
            return file_path


async def calculate_hash(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


async def main():
    url = 'https://gitea.radium.group/radium/project-configuration'
    new_url = f"{url}/archive/master.zip"

    with TemporaryDirectory() as dir_path:

        tasks = [download_repo(new_url, dir_path, str(task_number)) for task_number in range(3)]
        result_download = await asyncio.gather(*tasks)

        hash_tasks = [calculate_hash(file_path) for file_path in result_download]
        result_hashes = await asyncio.gather(*hash_tasks)

        for file_path, file_hash in zip(result_download, result_hashes):
            print(f"File: {file_path}, Hash: {file_hash}")


if __name__ == '__main__':
    asyncio.run(main())
