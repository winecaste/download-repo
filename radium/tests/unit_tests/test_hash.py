import os

import pytest

from radium.src.main import calculate_hash


@pytest.mark.asyncio
async def test_calculate_hash(tmpdir):
    test_file_path = os.path.join(str(tmpdir), "test_file.txt")
    with open(test_file_path, "wb") as f:
        f.write(b"test data")

    expected_hash = "916f0027a575074ce72a331777c3478d6513f786a591bd892da1a577bf2335f9"

    hash = await calculate_hash(test_file_path)
    assert hash == expected_hash
