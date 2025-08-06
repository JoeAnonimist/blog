import QtQml

LogTarget {
    function write(severity, message) {
        console.log("Logging to console: ", 
            "Severity: ", severity, message)
    }
}