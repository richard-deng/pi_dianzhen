# coding: utf-8

from handler import (
    ping,
    page,
    xiaoche,
)

urls = (
    # 接口
    ('^/ping$', ping.Ping),
    ('^/xc/qianjin$', xiaoche.QianJin),
    ('^/xc/reverse$', xiaoche.Reverse),
    ('^/xc/left$', xiaoche.Left),
    ('^/xc/right$', xiaoche.Right),
    ('^/xc/start$', xiaoche.Start),
    ('^/xc/stop$', xiaoche.Stop),


    # 页面
    ('^/xc/index.html$', page.Root),

)

