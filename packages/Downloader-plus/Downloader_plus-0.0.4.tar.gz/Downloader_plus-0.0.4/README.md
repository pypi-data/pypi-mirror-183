# downloader_plus<br>
##### The download_plus module: Support for Download or crawler with progress bar

At large scale, the structure of the module is following:

* downloader_plus.Get: Get a single file.

ExitCodes:

* ExitCode = 1: Download not successfully<br>
* ExitCode = 0: Download result unknown

This Package only has "Get" a Module.

Warning: This Package uses and depends on requests and tqdm.

### Get<br>
##### Get a single file.<br>

Usage: Get(url: str,filepath: str):

* url: Designated download URL.<br>
* filepath: Specifies the path to the downloaded file.<br>
* desc: Specifying a prefix.<br>
* unit: Designated unit. (Support Byte,Kib,Mib.)