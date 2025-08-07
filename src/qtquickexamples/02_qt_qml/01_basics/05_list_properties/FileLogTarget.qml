import QtQml

LogTarget {
    function write(severity, message, filename) {
        console.log("Logging to a file: ", 
            "Severity: ", severity, message, filename)
    }
}