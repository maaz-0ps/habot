import os

# ... other settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Adjust for your database type
        'NAME': os.environ.get('habot'),
        'USER': os.environ.get('habot'),
        'PASSWORD': os.environ.get('123456'),
        'HOST': os.environ.get('34.28.159.132'),
        'PORT': os.environ.get('3376'),
    }
}