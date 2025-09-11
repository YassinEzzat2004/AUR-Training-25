from setuptools import find_packages, setup

package_name = 'weather_py'

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
    maintainer='yassin_ezzat',
    maintainer_email='yassin_ezzat@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pressure=weather_py.pressure_node:main',
            'humidity=weather_py.humidity_node:main',
            'temperature=weather_py.temperature_node:main',
            'monitor=weather_py.monitor_node:main'
        ],
    },
)
