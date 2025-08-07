import QtQml
import QtQuick.Dialogs

LogTarget {

    function write(severity, message, filename) {
        console.log("Message box: ", 
        "Severity: ", severity, message, filename)
    }
}