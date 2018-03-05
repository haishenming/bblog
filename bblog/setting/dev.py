from .default import *


# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bblog',
        'USER': 'root',
        'PASSWORD': 'Haishen',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}