import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '/cloudsql/YOUR_PROJECT_ID:YOUR_INSTANCE_REGION:YOUR_INSTANCE_NAME',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'NAME': os.environ.get('DB_NAME'),
    }
}
