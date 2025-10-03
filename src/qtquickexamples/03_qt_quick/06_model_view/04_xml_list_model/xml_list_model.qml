import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml.XmlListModel

ApplicationWindow {
    visible: true
    width: listView.implicitWidth
    height: listView.implicitHeight
    title: "XmlListModel"
    
    XmlListModel {
        id: xmlModel
        
        source: "data.xml"
        query: "/organization/person"
        
        XmlListModelRole {
            name: "id"
            elementName: ""
            attributeName: "id"
        }
        
        XmlListModelRole {
            name: "firstname"
            elementName: "firstname"
        }
        
        XmlListModelRole {
            name: "lastname"
            elementName: "lastname"
        }
        
        XmlListModelRole {
            name: "profession"
            elementName: "profession"
        }
    }

    ListView {
        id: listView
        
        anchors.fill: parent
        model: xmlModel
        
        implicitWidth: 400
        implicitHeight: count * 40
        
        focus: true
        highlightFollowsCurrentItem: true
        highlight: Rectangle {
            color: "orange"
            opacity: 0.2
        }
        
        delegate: Rectangle {
            width: listView.width
            height: 40
            color: index % 2 === 0 ? "#f0f0f0" : "white"
            
            RowLayout {
                anchors.fill: parent
                anchors.margins: 8
                
                Text {
                    text: model.firstname + " " + model.lastname
                    font.bold: true
                    Layout.fillWidth: true
                }
                
                Text {
                    text: "- " + model.profession
                    color: "gray"
                }
            }
            
            MouseArea {
                anchors.fill: parent
                onClicked: listView.currentIndex = index
            }
        }
        
        ScrollBar.vertical: ScrollBar {}
    }
}