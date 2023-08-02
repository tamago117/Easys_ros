from setuptools import find_packages, setup

package_name = 'Easys_ros'

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
    maintainer='egrt1',
    maintainer_email='egrt1@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Easys_ros = Easys_ros.Easys_ros:main',
            'joy2cmd = Easys_ros.joy2cmd:main',
            'thruster_controller = Easys_ros.thruster_controller:main',
        ],
    },
)
