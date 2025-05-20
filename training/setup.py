from setuptools import find_packages, setup

package_name = 'training'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Akshay_Arjun',
    maintainer_email='aakshay1114@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = training.service:main',
            'talker = training.publisher:main',
            'listener = training.subscriber:main',
            'client = training.client:main',
        ],
    },
)
