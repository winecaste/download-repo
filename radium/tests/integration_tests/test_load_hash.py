import pytest

from unittest.mock import patch, AsyncMock

from radium.src.main import main


@pytest.mark.asyncio
async def test_main():
    with patch('radium.src.main.download_repo', new_callable=AsyncMock) as mock_download, \
         patch('radium.src.main.calculate_hash', new_callable=AsyncMock) as mock_hash:
        mock_download.return_value = '/tmp/test_0.zip'
        mock_hash.return_value = 'test_hash'

        await main()

        assert mock_download.call_count == 3
        assert mock_hash.call_count == 3
        mock_hash.assert_called_with('/tmp/test_0.zip')