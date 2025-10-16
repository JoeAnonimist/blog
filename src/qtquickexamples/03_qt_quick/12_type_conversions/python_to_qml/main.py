import sys
from PySide6.QtCore import QByteArray, QPoint, QDate, QDateTime, QTime, QUrl
from PySide6.QtGui import QGuiApplication, QColor
from PySide6.QtQml import QQmlApplicationEngine


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    
    int_value = 42
    float_value = 3.14
    bool_value = True
    str_value = 'Hello World'
    byte_array_value = QByteArray(bytearray([2, 3, 5, 7]))
    list_value = [2, 3, 5, 7]
    tuple_value = (2, 3, 5, 7)
    dict_value = {'a': 1, 'b': 2, 'c': 3}
    none_value = None
    qcolor_value = QColor('steelblue')
    qpoint_value = QPoint(0, 0)
    qdate_value = QDate(2025, 10, 15)
    qdatetime_value = QDateTime(2025, 10, 15, 0, 0, 0)
    qtime_value = QTime(0, 0, 0)
    qurl_value = QUrl('http://www.google.com')
    set_value = {2, 3, 5, 7}
    bytes_value = b'\x02\x03\x05\x07'
    range_value = range(2, 8, 2)  # Converts to [2, 4, 6]
    complex_value = 3 + 4j
    
    engine.setInitialProperties({
        'intValue': int_value,
        'floatValue': float_value,
        'boolValue': bool_value,
        'strValue': str_value,
        'byteValue': byte_array_value,
        'listValue': list_value,
        'tupleValue': tuple_value,
        'dictValue': dict_value,
        'noneValue': none_value,
        'qcolorValue': qcolor_value,
        'qpointValue': qpoint_value,
        'qdateValue': qdate_value,
        'qdatetimeValue': qdatetime_value,
        'qtimeValue': qtime_value,
        'qurlValue': qurl_value,
        'setValue': set_value,
        'bytesValue': bytes_value,
        'rangeValue': range_value,
        'complexValue': complex_value
    })
    
    engine.load('Main.qml')

    sys.exit(app.exec())