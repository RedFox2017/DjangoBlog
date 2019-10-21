# 在类中定义中间件预留函数
# __init__  服务器响应第一个请求时调用
# process_request  产生request对象，进行url匹配之前
# process_view  url匹配之后，调用视图函数之前
# process_response  视图调用之后，内容返回浏览器之前
# process_exception  视图出现异常调用
# 最后在settings.py中的MIDDLEWARE_CLASSES注册中间件类
