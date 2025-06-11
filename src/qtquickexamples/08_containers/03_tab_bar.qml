import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 250
    height:160
    title: "TabBar"
    
    ColumnLayout {
        
        anchors.fill: parent
        anchors.margins: 10
        
        TabBar {
            
            id: tabbar

            TabButton {
                text: "Styles"
                width: 60
            }

            TabButton {
                text: "Margins"
                width: 60
            }
        }

        StackLayout {

            Layout.fillWidth: true
            Layout.fillHeight: true

            currentIndex: tabbar.currentIndex
            
            Pane {

	            ColumnLayout {
	            
	                spacing: 10
	
	                CheckBox {
	                    text: "Heading"
	                }
	                CheckBox {
	                    text: "Paragraph"
	                }
	                CheckBox {
	                    text: "List"
	                }
	                Item {
	                    Layout.fillHeight: true
	                }
	            }
            }

            Pane {
            
	            ColumnLayout {
	            
	                spacing: 10
	
	                RadioButton {
	                    text: "Normal"
	                }
	                RadioButton {
	                    text: "Wide"
	                }
	                RadioButton {
	                    text: "Narrow"
	                }
	                Item {
	                    Layout.fillHeight: true
	                }
	            }
	        }
        }
    }
}