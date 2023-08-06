# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_automata',
 'manim_automata.mobjects',
 'manim_automata.mobjects.automata_dependencies']

package_data = \
{'': ['*']}

install_requires = \
['xmltodict>=0.13.0,<0.14.0']

entry_points = \
{'manim.plugins': ['manim_automata = manim_automata']}

setup_kwargs = {
    'name': 'manim-automata',
    'version': '0.2.14',
    'description': 'A Manim implementation of automata',
    'long_description': 'MANIM AUTOMATA\n==============\nA Manim plugin that allows you to generate scenes with Finite State Machines and their inputs. The plugin will automatically generate these animations with minimal setup from the user.\n\nThis plugin has been funded by the University of Leeds.\n\nYOUTUBE VIDEO EXAMPLE\n=====================\n[![Finite State Machine in Manim](https://img.youtube.com/vi/beKkjIGdeQc/0.jpg)](https://youtu.be/beKkjIGdeQc)\n[![Nondeterminstic Finite State Machine in Manim](https://img.youtube.com/vi/woaldsYmsHM/0.jpg)](https://youtu.be/woaldsYmsHM)\n\nNotes\n=====\nThe manim-automata plugin currently relies on JFLAP files, future updates will enable the user to create automata without JFLAP.\n[JFLAP](https://www.jflap.org) is software for experimenting with formal languages topics.\n\nInstallation\n============\nTo install manim-automata plugin run:\n\n   pip install manim-automata\n\nTo see which version of manim-automata you have:\n\n    manim-automata\n\nor\n\n    pip list\n\n\nImporting\n=========\nTo use manim-automata in your project, you can:\n\n* Add ``from manim_automata import *`` to your script.\nOnce manim-automata has been imported, you can use the ManimAutomata class to create automata.\n\n\nHow To Use\n==========\n```python\nclass Automaton(MovingCameraScene):\n    def construct(self):\n        manim_automaton = ManimAutomaton(xml_file=\'your_jff_file.jff\')\n        \n        #Adjust camera frame to fit ManimAutomaton in scene\n        self.camera.frame_width = manim_automaton.width + 10\n        self.camera.frame_height = manim_automaton.height + 10\n        self.camera.frame.move_to(manim_automaton) \n\n\n        #Create an mobject version of input for the manim_automaton\n        automaton_input = manim_automaton.construct_automaton_input("110011")\n\n        #Position automaton_input on the screen to avoid overlapping.\n        automaton_input.shift(LEFT * 2)\n        automaton_input.shift(UP * 10)\n\n        self.play(\n                DrawBorderThenFill(manim_automaton),\n                FadeIn(automaton_input)\n            )\n\n        # Play all the animations generate from .play_string()\n        for sequence in manim_automaton.play_string(automaton_input):\n            for step in sequence:\n                self.play(step, run_time=1)\n```\nTo run the code and generate the video, run:\n\n* manim -pql <name_of_script.py> Automaton\n\nrun with -pqh instead of -pql to have highquality version\n\n\nExamples\n========\nThe Github page for this plugin has a directory called manim_automata_examples. You can download these and play around with them.\n\nYou can run each file using these commands:\n\n* manim -pql examples.py FiniteStateAutomatonExample\n* manim -pql examples.py NonFiniteStateAutomatonExample\n* manim -pql examples.py PushDownAutomatonExample\n\n\nWriting Custom Animations\n=========================\nCreate a new file called custom_manim_animations.py (can be called anything).\nIn this file write:\n```python\nimport Manim\nfrom manim_automata import ManimAnimations\n\nclass CustomManimAnimations(ManimAnimations):\n    \n    def __init__(self) -> None:\n        super().__init__()\n\n```\n\nIn your manim-automaton file create an instance of your new custom manim animations class, like so:\n\n```python\nimport Manim\nfrom .custom_manim_animations import CustomManimAnimations\n\nclass Automaton(MovingCameraScene):\n    def construct(self):\n        manim_animations_instance = CustomManimAnimations()\n\n        manim_automaton = ManimAutomaton(xml_file=\'example_machine.jff\', manim_animations=manim_animations_instance)\n        ...\n```\n\nNow that everything is setup, you\'ll be able to override the methods in ManimAnimations in your own class.\nGo to the github repository of this project, then to custom_animations_help to find a file that has all the animation methods that can be overriden.',
    'author': 'Sean Nelson',
    'author_email': 'snelson01010@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SeanNelsonIO/manim-automata',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
