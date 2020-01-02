# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/29
# Email: gq4350lu@hotmail.com

import re
# def fun_var_args_call(arg1, arg2, arg3):
#     print ("arga:", arg1 )
#     print ("argb:", arg2 )
#     print ("argc:", arg3 )
#
# kwargs = {"arg3": 3, "arg2": 2}
#
# fun_var_args_call(1, **kwargs)

ss='shutil.copy(:)的效果“dot-com”部分（技术上称为“顶级域'
regex=re.compile(r'[^a-zA-Z0-9()\.:_\u4e00-\u9fa5]')
text=regex.sub('_', ss)
print(text)