from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout,
    QVBoxLayout, QPushButton, QStackedWidget, QLabel
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Productivity Dashboard")
        self.setMinimumSize(1200, 750)

        # root widget
        root = QWidget()
        self.setCentralWidget(root)

        layout = QHBoxLayout(root)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # sidebar on the left
        layout.addWidget(self._build_sidebar())

        # page switcher on the right
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        self._load_pages()

    def _build_sidebar(self):
        sidebar = QWidget()
        sidebar.setFixedWidth(210)
        sidebar.setObjectName("sidebar")

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # app title
        title = QLabel("📊 My Dashboard")
        title.setObjectName("sidebarTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # nav buttons — (label, page index)
        nav_items = [
            ("🏠  Home",       0),
            ("📚  Courses",    1),
            ("✅  Tasks",      2),
            ("📅  Reports",    3),
        ]

        for label, index in nav_items:
            btn = QPushButton(label)
            btn.setObjectName("navBtn")
            btn.setCheckable(True)
            btn.clicked.connect(lambda _, i=index: self._switch_page(i))
            layout.addWidget(btn)
            
        layout.addStretch()
        return sidebar

    def _switch_page(self, index):
        self.stack.setCurrentIndex(index)

    def _load_pages(self):
        # temporary placeholders — we'll replace these one by one
        for name in ["Home", "Courses", "Tasks", "Reports"]:
            placeholder = QWidget()
            layout = QVBoxLayout(placeholder)
            label = QLabel(f"{name} page coming soon...")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
            self.stack.addWidget(placeholder)