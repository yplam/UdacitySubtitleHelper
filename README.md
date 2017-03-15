# UdacitySubtitleHelper

Udacity 字幕翻译助手

自己用的一个非常简陋的 python 脚本，用来加快 Udacity 字幕翻译速度，提供两个基本功能：

* translate 子命令读取字幕文件，调用 Google 翻译 api 将每行翻译成中文，并且将原文附加在每行译文后面
* format 子命令读取你翻译完的文件，将上一步附加在后面的原文删除，输出最终文件

此脚本依赖下面两个库，需要提前安装

```

sudo pip install pysrt google-api-python-client

```

**配置**

```

config = {
    'proxy_host' : '127.0.0.1',
    'proxy_port' : 1080,
    'api_key' : 'your key here'
}

```

因为需要调用 Google 翻译 api，所以需要配置 Google 的 api key，需要自行申请，并且修改配置文件

对于 CN 用户，还需要配置一个 socks5 代理，用于 FQ 调用接口

正如前面所言，此脚本仅是个人使用，因此没有做任何错误处理，请避免在字幕源文件目录运行，否则可能会导致覆盖掉源文件

如果您有任何建议，请给我反馈 yplam#yplam.com
