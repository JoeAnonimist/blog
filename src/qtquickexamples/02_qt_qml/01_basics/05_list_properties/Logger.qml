import QtQml

QtObject {

    property string message
    property list<LogTarget> targets

    component Details: QtObject {
        property int severity
        property string filename
    }
    
    property Details details: Details {}

    function log (severity, message, filename) {
        targets.forEach(target =>
            target.write(severity, message, filename))
    }
}