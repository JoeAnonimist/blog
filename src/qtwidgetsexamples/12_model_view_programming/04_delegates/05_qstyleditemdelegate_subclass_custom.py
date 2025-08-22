# https://stackoverflow.com/questions/14780517/toggle-switch-in-qt

import sys
from PySide6.QtCore import Qt, QAbstractTableModel, QRect, QSize, QModelIndex
from PySide6.QtGui import QColor, QPainter, QBrush, QMouseEvent, QPalette
from PySide6.QtWidgets import QApplication, QTableView, QStyledItemDelegate, QWidget, QVBoxLayout


class BooleanSwitchDelegate(QStyledItemDelegate):
    
    def paint(self, painter, option, index):
        
        value = index.model().data(index, Qt.DisplayRole)

        # Switch dimensions
        rect = option.rect
        switch_width = 40
        switch_height = 20
        margin = (rect.height() - switch_height) // 2
        switch_rect = QRect(rect.x() + margin, rect.y() + margin, switch_width, switch_height)

        # Background
        bg_color = option.palette.color(QPalette.ColorRole.Mid)
        thumb_color = option.palette.color(QPalette.ColorRole.Accent) if value else option.palette.color(QPalette.ColorRole.Button)

        # Thumb position
        if value:
            thumb_x = switch_rect.right() - switch_height
        else:
            thumb_x = switch_rect.left()

        thumb_rect = QRect(thumb_x, switch_rect.y(), switch_height, switch_height)

        # Draw switch
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(bg_color))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(switch_rect, switch_height / 2, switch_height / 2)

        painter.setBrush(QBrush(thumb_color))
        painter.drawEllipse(thumb_rect)

        painter.restore()

    def sizeHint(self, option, index):
        return QSize(50, 30)  # Slight padding for visual clarity

    def editorEvent(self, event, model, option, index):
        if event.type() == QMouseEvent.MouseButtonRelease:
            if option.rect.contains(event.position().toPoint()):
                current_value = index.model().data(index, Qt.EditRole)
                model.setData(index, not current_value, Qt.EditRole)
                return True
        return False


class BoolTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = [True, False, True, False, True]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role):
        if role in (Qt.DisplayRole, Qt.EditRole):
            return self._data[index.row()]
        return None

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        table = QTableView()
        model = BoolTableModel()
        table.setModel(model)

        delegate = BooleanSwitchDelegate()
        table.setItemDelegateForColumn(0, delegate)

        layout.addWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


