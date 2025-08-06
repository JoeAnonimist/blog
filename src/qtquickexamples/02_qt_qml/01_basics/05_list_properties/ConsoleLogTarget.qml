import QtQml

LogTarget {
    function write(severity, message) {
        console.log(severity, message)
    }
}