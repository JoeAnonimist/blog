import QtQml

QtObject {

    property string message
    property int severity
    property string filename
    
    function log () {
        console.log("Log: ",
            severity, message, filename)
    }
}