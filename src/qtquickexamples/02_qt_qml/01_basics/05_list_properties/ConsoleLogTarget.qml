import QtQml

LogTarget {
    function write(severity, message, filename) {
        console.log("Logging to console: ", 
            "Severity: ", severity, message, filename)
    }
}