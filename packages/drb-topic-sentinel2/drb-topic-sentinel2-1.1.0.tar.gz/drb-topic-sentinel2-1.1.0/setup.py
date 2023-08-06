import versioneer
from setuptools import setup, find_namespace_packages


with open('requirements.txt', 'r') as file:
    REQUIREMENTS = file.readlines()

with open('README.md', 'r') as file:
    long_description = file.read()


setup(
    name='drb-topic-sentinel2',
    description='sentinel-2 topic for DRB Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='GAEL Systems',
    author_email='drb-python@gael.fr',
    url='https://gitlab.com/drb-python/topics/sentinel2',
    python_requires='>=3.8',
    install_requires=REQUIREMENTS,
    packages=find_namespace_packages(include=['drb.*']),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={
        'drb.topics.sentinel2': ['cortex.yml'],
        'drb.topics.sentinel2.user': ['cortex.yml'],
        'drb.topics.sentinel2.pdi': ['cortex.yml'],
        'drb.topics.sentinel2.pdi.datastrip': ['cortex.yml'],
        'drb.topics.sentinel2.pdi.granule': ['cortex.yml'],
        'drb.topics.sentinel2.aux': ['cortex.yml']
    },
    data_files=[('.', ['requirements.txt'])],
    entry_points={
        'drb.topic': [
            'sentinel2=drb.topics.sentinel2',
            'sentinel2_user=drb.topics.sentinel2.user',
            'sentinel2_pdi=drb.topics.sentinel2.pdi',
            'sentinel2_ds=drb.topics.sentinel2.pdi.datastrip',
            'sentinel2_gs=drb.topics.sentinel2.pdi.granule',
            'sentinel2_aux=drb.topics.sentinel2.aux'
        ]
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
