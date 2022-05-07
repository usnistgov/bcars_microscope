# from .file import fcn

from ._version import __version__

dark_style_sheet = ('QWidget {background-color: rgb(53,53,53); font: 11pt "Arial";}\n'
                    'QLabel {color: white}\n'
                    'QPushButton {background-color: rgb(53,53,53); color: rgb(255,255,255)}\n'
                    'QPushButton:disabled {color: rgb(100,100,100)}\n'
                    'QAbstractSpinBox {background-color: rgb(255,255,255)}\n'
                    'QCheckBox {color: red; background-color: white; width: 0; height: 0; spacing: 0px}\n'
                    'QCheckBox::indicator {color: red; width: 25; height: 25}\n'
                    'QRadioButton {color:white}\n'
                    'QRadioButton::indicator {width:20; height: 20; color: black; border-radius: 10px}\n'
                    'QRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\n'
                    'QRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}\n'
                    'QDoubleSpinBox {font: 11pt "Arial";}\n'
                    'QGroupBox {color: white}\n'
                    'QFrame {color: white}\n'
                    'QTabBar {color: white}\n'
                    'QLineEdit {background-color: white}\n'
                    'QComboBox {color: white}\n')

# QRadioButton { color: white}\nQRadioButton::indicator { width: 50; height: 50; border-radius: 20px}\nQRadioButton::indicator:checked {background-color: rgb(85, 255, 0); border: 2px solid white}\nQRadioButton::indicator:unchecked {background-color: rgb(100,100,100); border: 2px solid white}

# __all__ = ['fcn']

# 'QCheckBox::indicator { width: 25; height: 25; color:rgb(0,0,0); background-color:rgb(200,255,255)}\n'
#                     'QCheckBox::indicator:disabled { background-color:rgb(100,100,100); color:rgb(0,0,0); }\n'
                    