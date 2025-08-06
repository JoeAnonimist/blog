import QtQml

QtObject {

    property string message
    property list<QtObject> targets
    
    property QtObject details: QtObject {
        property int severity
        property string filename
    }

    function log (message) {
        targets.forEach(target =>
            target.write(details.severity, message))
    }
}