import sys
from PySide6.QtCore import QObject, QDateTime, QUrl, QRegularExpression
from PySide6.QtGui import QGuiApplication, QColor
from PySide6.QtQml import QQmlApplicationEngine


def on_values_sent(intValue, realValue, boolValue, stringValue, 
                   listValue, dateValue, colorValue, urlValue, qobjectValue,
                   varValue, pointValue, sizeValue, rectValue, vector2dValue,
                   vector3dValue, vector4dValue, quaternionValue, matrix4x4Value,
                   fontValue, regexpValue, enumValue, objectListValue, nullValue,
                   mixedListValue):
    print('sent')
    
    print(f"intValue: {intValue}, Type: {type(intValue).__name__}")
    print(f"realValue: {realValue}, Type: {type(realValue).__name__}")
    print(f"boolValue: {boolValue}, Type: {type(boolValue).__name__}")
    print(f"stringValue: {stringValue}, Type: {type(stringValue).__name__}")
    print(f"listValue: {listValue}, Type: {type(listValue).__name__}")
    print(f"qobjectValue objectName: {qobjectValue.objectName()}, Type: {type(qobjectValue).__name__}")
    print(f"dateValue: {dateValue.toString('yyyy-MM-dd')}, Qt Type: {type(dateValue).__name__}")
    print(f"colorValue: {colorValue.red()}, {colorValue.green()}, {colorValue.blue()}, Qt Type: {type(colorValue).__name__}")
    print(f"urlValue: {urlValue.path()}, Qt Type: {type(urlValue).__name__}")
    print(f"varValue: {varValue}, Type: {type(varValue).__name__}")
    print(f"pointValue: ({pointValue.x}, {pointValue.y}), Type: {type(pointValue).__name__}")
    print(f"sizeValue: ({sizeValue.width}, {sizeValue.height}), Type: {type(sizeValue).__name__}")
    print(f"rectValue: ({rectValue.x}, {rectValue.y}, {rectValue.width}, {rectValue.height}), Type: {type(rectValue).__name__}")
    print(f"vector2dValue: ({vector2dValue.x}, {vector2dValue.y}), Type: {type(vector2dValue).__name__}")
    print(f"vector3dValue: ({vector3dValue.x}, {vector3dValue.y}, {vector3dValue.z}), Type: {type(vector3dValue).__name__}")
    print(f"vector4dValue: ({vector4dValue.x}, {vector4dValue.y}, {vector4dValue.z}, {vector4dValue.w}), Type: {type(vector4dValue).__name__}")
    print(f"quaternionValue: ({quaternionValue.scalar}, {quaternionValue.x}, {quaternionValue.y}, {quaternionValue.z}), Type: {type(quaternionValue).__name__}")
    print(f"matrix4x4Value: {matrix4x4Value}, Type: {type(matrix4x4Value).__name__}")
    print(f"fontValue: {fontValue.family()}, {fontValue.pixelSize()}, Type: {type(fontValue).__name__}")
    print(f"regexpValue: {regexpValue.pattern()}, Type: {type(regexpValue).__name__}")
    print(f"enumValue: {enumValue} (represents MyEnum.Option2), Type: {type(enumValue).__name__}")
    print(f"objectListValue: {objectListValue}, Type: {type(objectListValue).__name__}")
    print(f"nullValue: {nullValue}, Type: {type(nullValue).__name__}")
    print(f"mixedListValue: {mixedListValue}, Type: {type(mixedListValue).__name__}")


if __name__ == '__main__':

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load('Main.qml')
    
    root = engine.rootObjects()[0]
    button = root.findChild(QObject, 'button')
    button.valuesSent.connect(on_values_sent)

    sys.exit(app.exec())