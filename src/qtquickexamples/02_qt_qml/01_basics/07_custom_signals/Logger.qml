import QtQml

QtObject {

    property string message
    property int severity
    property string filename
    
    signal logged(at: date)
    
    function log () {
        console.log("Log: ",
            severity, message, filename)
            logged(new Date())
    }
}