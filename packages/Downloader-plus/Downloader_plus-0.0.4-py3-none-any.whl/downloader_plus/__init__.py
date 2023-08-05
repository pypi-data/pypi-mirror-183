"""
The download_plus module: Support for Download or crawler with progress bar

At large scale, the structure of the module is following:

* downloader_plus.Get: Get a single file.

ExitCodes:

* ExitCode = 1: Download not successfully
* ExitCode = 0: Download result unknown

Warning: This Package only has "Get" a Module.
"""
import requests
from tqdm import tqdm

"""Warning: This Package uses and depends on requests and tqdm."""


def Get(url: str, filepath: str, desc: str, unit: str) -> str:
    """
    Get a single file.

    Usage: Get(url: str,filepath: str):

    * url: Designated download URL.
    * filepath: Specifies the path to the downloaded file.
    * desc: Specifying a prefix.
    * unit: Designated unit. (Support Byte,Kib,Mib.)
    """
    url = str(url)
    response = requests.get(url, stream=True)
    if unit == 'Mib':
        data_size = round(int(response.headers['Content-Length']) / 1024 / 1024, 2)
    elif unit == 'Kib':
        data_size = round(int(response.headers['Content-Length']) / 1024, 2)
    elif unit == 'Byte':
        data_size = round(int(response.headers['Content-Length']), 2)
    else:
        raise TypeError(f'Unsupported unit:{unit}')
    with open(filepath, 'wb') as f:
        for data in tqdm(iterable=response.iter_content(1024 * 1024), total=data_size, desc=desc,
                         unit=unit):
            f.write(data)


