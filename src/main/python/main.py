from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QLabel
import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()
    label = QLabel('Hello World!')
    label.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)