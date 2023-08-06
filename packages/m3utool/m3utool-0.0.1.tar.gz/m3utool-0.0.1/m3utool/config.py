# 浏览器用户代理
USER_AGENT = "Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.110 Mobile Safari/537.36"

# M3U8请求超时时间
REQUEST_TIMEOUT = 5

# 异步请求连接时间
ASYNC_TIMEOUT = 20

# 异步aiohttp限制 limit
ASYNC_REQUEST_LIMIT = 256

# 请求重定向
FOLLOW_REDIRECTS = True

# 全部请求方式
REQUEST_METHOD_LIST = ("GET", "POST", "DELETE", "PATCH", "HEAD", "PUT", "OPTIONS")

# 下载保存文件夹
FILE_PATH = "/storage/emulated/0/m3u8"
