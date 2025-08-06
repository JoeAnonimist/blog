import QtQml

LogTarget {
    function write(severity, message) {
        console.log("Logging to a file: ", 
            "Severity: ", severity, message)
    }
}