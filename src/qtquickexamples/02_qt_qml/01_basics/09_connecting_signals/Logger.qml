import QtQml

QtObject {

    property string message
    property int severity
    property string filename
    
    signal detailsChanged(name: string, value: var)
    
    function log () {
        console.log("Log: ",
            severity, message, filename)
            logged(new Date())
    }
}