from setuptools import setup


with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='ami2rabbitmq',
    version='0.0.1',
    license='MIT License',
    author='Tatianno Alves',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='tferreiraalves@gmail.com',
    keywords='asterisk ami rabbitmq producer',
    description=u'Producer Events Asterisk Manager Interface (AMI) for RabbitMQ Broker',
    packages=['ami2rabbitmq'],
    install_requires=[
        'async-timeout',
        'certifi',
        'charset-normalizer',
        'idna',
        'pika',
        'pyst2',
        'redis',
        'requests',
        'six',
        'urllib3',
    ],
)