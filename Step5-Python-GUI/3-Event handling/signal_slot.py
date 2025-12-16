"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


# Filename: signals_slots.py

"""Signals and slots example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def show_msg():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Show Message')
btn.clicked.connect(show_msg)  # Connect clicked to show_msg()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())