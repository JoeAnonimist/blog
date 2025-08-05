import QtQuick
import QtQuick.Controls

ApplicationWindow {

    id: appWindow

    visible: true
    width: 300
    height:200
    title: "QML object properties"
    
	property list<color> colors: [
	    "mistyrose",
	    "honeydew",
	    "aliceblue",
	    "coral",
	    "mediumslateblue"
	]

    Rectangle {
    
        id: backgroundRect

        width: appWindow.width
        height: appWindow.height
        color: appWindow.colors[0]
        
        Button {
        
            text: appWindow.title + " example"
            
            x: (appWindow.width - width) / 2
            y: (appWindow.height - height) / 2
            
            width: implicitWidth + 10
            height: 50
            
            onClicked: {
                let index = Math.floor(Math.random() 
                    * appWindow.colors.length)
                print(index) 
                backgroundRect.color = appWindow.colors[index]
                    
            }
        }
    }
}

/*
| Use case                 | Type of list                | Benefit                                        |
| ------------------------ | --------------------------- | ---------------------------------------------- |
| Group multiple QML items | `list<Item>`                | Batch control (show/hide, enable/disable)      |
| Manage animations        | `list<Animation>`           | Coordinated start/stop                         |
| UI component children    | `list<Item>`                | Flexible child management                      |
| Bind to C++ objects      | `list<MyQObject>`           | Expose C++ data to QML seamlessly              |
| Data collections (small) | `list<string>`, `list<int>` | Simple static lists without ListModel overhead |
*/