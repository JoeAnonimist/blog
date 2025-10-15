import sys
from PySide6.QtCore import QStringListModel
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def on_data_changed(topLeft, bottomRight):
    print('Data changed: ', end='')
    print(topLeft.model().data(topLeft))
    
def on_rows_inserted(parent, first, last):
    print('Rows inserted: ', first, last)
    
def on_rows_removed(parent, first, last):
    print('Rows removed: ', first, last)


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    
    string_list_model = QStringListModel(
        ['Item 1', 'Item 2', 'Item 3',
         'Item 4', 'Item 5', 'Item 6'])
    
    string_list_model.dataChanged.connect(on_data_changed)
    string_list_model.rowsInserted.connect(on_rows_inserted)
    string_list_model.rowsRemoved.connect(on_rows_removed)
    
    engine.setInitialProperties({'stringListModel': string_list_model})
    
    engine.load('Main.qml')

    sys.exit(app.exec())