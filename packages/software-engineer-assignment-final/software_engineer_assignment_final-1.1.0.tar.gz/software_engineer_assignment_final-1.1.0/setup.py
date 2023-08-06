# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['software_engineer_assignment']

package_data = \
{'': ['*']}

install_requires = \
['pyqt5>=5.15.7,<6.0.0', 'pyqtgraph>=0.13.1,<0.14.0', 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'software-engineer-assignment-final',
    'version': '1.1.0',
    'description': 'Software Engineering assignment for job interview.',
    'long_description': "# Software-engineer-assignment\n+ Python project for software engineer job interview. \n\n### Author\n+ Martin P.\n\n### Purpose of the Package\n+ Purpose of test assignment is \nto develeop a simple GUI application for connecting and gathering data from encoder device.\n\n### Dependencies\n+ serial\n+ PyQt5\n+ pyqtgraph\n\n\n### Modules\n+ main_app.py - contains main method for the application\n+ gui_main.py - contains main gui class \n+ gui_components.py - contains gui component classes for used PyQt widgets\n+ gui_alarm_module.py - contains class for logging encoder alarms in to the file\n+ encoder_interface.py - contains interface class for encoder\n+ serial_interface.py - contains basic class for serial interface\n\n### Main Method/Usage\n+ Start the application by calling App() method from main_app.py in your main.py script.\n\n+ Example:\n\n\tfrom software_engineer_assignment import app\n\n\tif __name__ == '__main__':\n\t    app()\n\n\n",
    'author': 'MartinP96',
    'author_email': 'porenta.martin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MartinP96/software_engineer_assignment',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
