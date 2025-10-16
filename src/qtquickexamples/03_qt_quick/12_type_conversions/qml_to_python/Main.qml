import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: 100
    title: "Type conversions"
    
    Item {
        id: myItem
        objectName: "myItem"
    }
    
    Item {
        id: anotherItem
        objectName: "anotherItem"
    }
    
    Item {
        id: enumItem
        enum MyEnum { Option1, Option2, Option3 }
    }
    
    ColumnLayout {
    
        anchors.fill: parent
        anchors.margins: 4
    
        Button {
        
            objectName: "button"
            
            signal valuesSent(intValue: int, realValue: real,
                            boolValue: bool, stringValue: string,
                            listValue: list<int>, dateValue: date,
                            colorValue: color, urlValue: url,
                            qobjectValue: QtObject,
                            varValue: var,
                            pointValue: point,
                            sizeValue: size,
                            rectValue: rect,
                            vector2dValue: vector2d,
                            vector3dValue: vector3d,
                            vector4dValue: vector4d,
                            quaternionValue: quaternion,
                            matrix4x4Value: matrix4x4,
                            fontValue: font,
                            regexpValue: regexp,
                            enumValue: int,
                            objectListValue: var,
                            nullValue: var,
                            mixedListValue: list<variant>)
        
            Layout.fillWidth: true
            Layout.fillHeight: true
            text: "Send values to PySide"
            
            onClicked: {
                valuesSent(
                    42,                              // int
                    3.14,                            // real
                    true,                            // bool
                    "Hello",                         // string
                    [1, 2, 3],                       // list<int>
                    "2025-10-16",                    // date
                    "steelblue",                     // color
                    "https://google.com",            // url
                    myItem,                          // QtObject
                    {key: "value"},                  // var (can hold any type)
                    Qt.point(10, 20),                // point
                    Qt.size(100, 50),                // size
                    Qt.rect(0, 0, 100, 100),         // rect
                    Qt.vector2d(1.0, 2.0),           // vector2d
                    Qt.vector3d(1.0, 2.0, 3.0),      // vector3d
                    Qt.vector4d(1.0, 2.0, 3.0, 4.0), // vector4d
                    Qt.quaternion(1, 0, 0, 0),       // quaternion
                    Qt.matrix4x4(),                  // matrix4x4 (identity matrix)
                    Qt.font({family: "Arial", pixelSize: 12}), // font
                    /test\d+/,                       // regexp
                    enumItem.Option2,                // enum (passed as int)
                    [myItem, anotherItem],           // var (list<QtObject>)
                    null,                            // var (null)
                    [1, "two", true]                 // list<variant> (mixed types)
                )
            }
        }
    }
}