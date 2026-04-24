import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import sys
from PyQt6.QtWidgets import QApplication
from views.main_window import MainWindow
from database.db_manager import initialize_db

if __name__ == "__main__":
    initialize_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())