# Simple HTTP Server

![screenshot](screenshot.png)

一个支持文件上传下载和临时文本保存的 HTTP 服务器。

安装：`pip3 install httpserver4u`

运行：`python3 -m httpserver4u`

不需安装运行：`python src/httpserver4u/server.py` [代码](https://github.com/jerrylususu/simple_http_server_py/blob/main/src/httpserver4u/server.py)（单脚本即可执行）

无三方库依赖。适用于 Python 3.6 及以上版本。

基于 [UniIsland 的 Gist](https://gist.github.com/UniIsland/3346170) 和 [Tallguy297/SimpleHTTPServerWithUpload](https://github.com/Tallguy297/SimpleHTTPServerWithUpload) 的代码，稍作修改：
1. 移除了图标
2. 解决了 Ctrl-C 退出后立刻重启，提示 `port already in use` 的问题
3. 增加文本保存功能
4. 完全 UTF-8 化（除二进制文件下载/上传外）

- 适用：临时、局域网内、小文件
- 不适用：长时间运行、大文件量、高并发、面向外部网络开放、需要安全性保证
---

A simple HTTP server with file upload/download and quick text save function.

Install：`pip3 install httpserver4u`

Run：`python3 -m httpserver4u`

Run without install：`python src/httpserver4u/server.py`[source code](https://github.com/jerrylususu/simple_http_server_py/blob/main/src/httpserver4u/server.py) (This script contains all functionality.)

No third-party dependency. Python 3.6 or newer version required.

Based on code of [UniIsland's Gist](https://gist.github.com/UniIsland/3346170) and [Tallguy297/SimpleHTTPServerWithUpload](https://github.com/Tallguy297/SimpleHTTPServerWithUpload), with slight modification for my own use case:
1. Removes the icons
2. Fix the bug that if the script is stopped using Ctrl-C and immediately restarted, it will fail with `port already in use`
3. Add the ability to quickly save text to a text file
4. Enable UTF-8 encoding everywhere (beside actual binary file download / upload)

- For: temporary, local lan network, small files
- Not for: long term, large file, high concurrency, exposed to external network, security needed