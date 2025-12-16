"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import sys
# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())