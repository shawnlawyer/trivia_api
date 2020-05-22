from envs import env

basedir = env('HOME') + '/backend'


class Config(object):
    """Flask config variables"""

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        env('POSTGRES_USER'),
        env('POSTGRES_PASSWORD'),
        env('POSTGRES_HOST'),
        env('POSTGRES_PORT'),
        env('POSTGRES_DB')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = ('SQLALCHEMY_TRACK_MODIFICATIONS')

    SECRET_KEY = env('APP_SECRET_KEY')

    APPLICATION_ROOT = '/api'
