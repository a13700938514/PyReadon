from PyQt5.QtWidgets import QScrollArea, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

class MyArea(QScrollArea):
    def init(self, widget):
        self.widget = widget
        self.init_action()
        
    def init_action(self):
        zoom_minus = QShortcut(QKeySequence("Ctrl+-"), self)
        zoom_minus.activated.connect(self.minus)       
        zoom_plus = QShortcut(QKeySequence("Ctrl+="), self)
        zoom_plus.activated.connect(self.plus) 
        
        switch_left = QShortcut(QKeySequence(Qt.Key_Left), self)
        switch_left.activated.connect(self.left)       
        switch_right = QShortcut(QKeySequence(Qt.Key_Right), self)
        switch_right.activated.connect(self.right) 
    
    # 鼠标左键翻页
    def mousePressEvent(self, event):
        pos = event.pos().x()
        width = self.size().width()
        if event.button() == Qt.LeftButton:
            if pos > width * 2 / 3:
                self.right()
            elif pos < width / 3:
                self.left()
            
    # 放大
    def plus(self):
        self.widget.zoom_book(plus=True)
    
    # 缩小
    def minus(self):
        self.widget.zoom_book(plus=False)
     
    # 下一页
    def right(self):
        self.widget.switch_page(right=True)
    
    # 前一页
    def left(self):
        self.widget.switch_page(right=False)
        
