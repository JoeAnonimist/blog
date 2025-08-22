# https://stackoverflow.com/questions/14780517/toggle-switch-in-qt

import sys
from PySide6.QtCore import Qt, QAbstractTableModel, QRect, QSize, QModelIndex
from PySide6.QtGui import QColor, QPainter, QBrush, QMouseEvent, QPalette
from PySide6.QtWidgets import QApplication, QTableView, QStyledItemDelegate, QWidget, QVBoxLayout
from PySide6.QtTest import QAbstractItemModelTester

class CsvModel(QAbstractTableModel):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.header = ['Indicator', 'Value (%)', 
            'Aggregate', 'Include in report']
        self.csv_data = [
            ['GDP', 3, 1, True],
            ['CPI', 6, 1, True],
            ['Jobs', 5, 0, True],
            ['Confidence', 75, 0, True],
            ['Industry', 92, 0, True],
            ['Retail', 4, 1, True],
        ]

    def rowCount(self, parent=QModelIndex()):
        return len(self.csv_data)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.header)
    
    def data(self, index, role):
        
        value = self.csv_data[index.row()][index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return value
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                return value == 1
            else:
                return value
    
    def setData(self, index, value, role):
        
        if role == Qt.ItemDataRole.EditRole:
            if index.column() == 2:
                value = 1 if value else 0
            if self.csv_data[index.row()][index.column()] != value:
                self.csv_data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index)
                return True
            return False
        return False
    
    def flags(self, index):
        flags = Qt.ItemFlags.ItemIsSelectable | \
            Qt.ItemFlags.ItemIsEnabled | \
            Qt.ItemFlags.ItemIsEditable
        return flags

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal:
            if role == Qt.ItemDataRole.DisplayRole:
                return self.header[section]


class SwitchDelegate(QStyledItemDelegate):
    
    def createEditor(self, parent, option, index):
        return None
    
    def paint(self, painter, option, index):
        
        value = index.model().data(index, Qt.ItemDataRole.DisplayRole)

        rect = option.rect
        switch_width = 40
        switch_height = 16
        margin_y = (rect.height() - switch_height) // 2
        margin_x = (rect.width() - switch_width) // 2
        switch_rect = QRect(
            rect.x() + margin_x, rect.y() + margin_y,
            switch_width, switch_height)

        bg_color = option.palette.color(QPalette.ColorRole.Mid)
        thumb_color = option.palette.color(
            QPalette.ColorRole.Accent) if value else option.palette.color(QPalette.ColorRole.Button)

        # Thumb larger than switch height
        thumb_diameter = switch_height + 4  # Thumb is 4 pixels larger than switch_height
        thumb_y = switch_rect.y() - (thumb_diameter - switch_height) // 2  # Center thumb vertically
        if value:
            thumb_x = switch_rect.right() - thumb_diameter
        else:
            thumb_x = switch_rect.left()
        thumb_rect = QRect(thumb_x, thumb_y, thumb_diameter, thumb_diameter)

        painter.save()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setBrush(QBrush(bg_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(switch_rect, switch_height / 2, switch_height / 2)

        painter.setBrush(QBrush(thumb_color))
        painter.drawEllipse(thumb_rect)

        painter.restore()

    def sizeHint(self, option, index):
        return QSize(50, 30)

    def editorEvent(self, event, model, option, index):
        if event.type() == QMouseEvent.MouseButtonRelease:
            if option.rect.contains(event.position().toPoint()):
                current_value = index.model().data(index, Qt.ItemDataRole.EditRole)
                model.setData(index, not current_value, Qt.ItemDataRole.EditRole)
                return True
        return False

class Window(QWidget):
    
    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        model = CsvModel()
        QAbstractItemModelTester(model)

        delegate = SwitchDelegate()
        
        view = QTableView()
        view.setModel(model)
        
        view.setItemDelegateForColumn(3, delegate)
        
        view.resizeColumnsToContents()
        layout.addWidget(view)
        
        model.dataChanged.connect(self.on_data_changed)
        
    def on_data_changed(self, topLeft, bottomRight, roles):
        for row in topLeft.model().csv_data:
            print(row)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = Window()
    main_window.show()

    sys.exit(app.exec())


