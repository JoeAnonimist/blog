import QtQml

QtObject {

    property string message
    
    property QtObject details: QtObject {
        property int severity
        property string filename
    }
}