from setuptools import find_packages, setup
import glob
import os

package_name = 'my_camera'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
            glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param',
            glob.glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='addinedu',
    maintainer_email='khyoo0825@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = my_camera.img_publisher:main',
            'canny_edge_filter = my_camera.canny_edge_filter:main',
            'red_filter = my_camera.red_filter:main',
            'green_filter = my_camera.green_filter:main',
            'blue_filter = my_camera.blue_filter:main',
            'red_canny_edge_filter = my_camera.red_canny_edge_filter:main',
            'camera_control = my_camera.camera_control:main',
            'camera_control_client = my_camera.camera_control_client:main'
        ],
    },
)
