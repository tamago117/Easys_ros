from setuptools import find_packages, setup

package_name = 'Easys_ros'
submodule_name = package_name + '/controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodule_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/Easys_control.launch.py',
                                               'launch/remote_control.launch.py',
                                               'launch/yolov8.launch.py',]),
        ('share/' + package_name + '/config', ['config/bno055_params_i2c.yaml']),
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
            'Easys_controller = Easys_ros.Easys_controller:main',
            'thruster_output_converter = Easys_ros.thruster_output_converter:main',
        ],
    },
)
