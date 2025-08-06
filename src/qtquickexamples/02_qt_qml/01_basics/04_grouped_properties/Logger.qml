import QtQml

QtObject {

    property string message
    
    component Details: QtObject {
        property int severity
        property string filename
    }
    
    property Details details: Details {}
}