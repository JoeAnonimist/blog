import QtQml
import QtQuick.Dialogs

LogTarget {

    function write(severity, message) {
        console.log("Message box: ", severity, message)
    }
}