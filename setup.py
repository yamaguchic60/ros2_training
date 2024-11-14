from setuptools import find_packages, setup

package_name = 'hello'

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
    maintainer='tk',
    maintainer_email='tkmcbo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_node = hello.hello_node:main',
            'hello_world_node = hello_world_pkg.hello_world_node:main',
            'happy_publisher_node=hello.happy_publisher_node:main',
            'happy_subscriber_node=hello.happy_subscriber_node:main'
        ],
    },
)
