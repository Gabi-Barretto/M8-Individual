from setuptools import find_packages, setup

package_name = 'meu_pacote'

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
    maintainer='gabi',
    maintainer_email='gabriela.dias@sou.inteli.edu.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
 	    'pub = meu_pacote_ros.pub:main',
            'subs = meu_pacote_ros.subs:main',        ],
    },
)
