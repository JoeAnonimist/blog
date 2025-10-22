import QtQuick
import Qt.labs.qmlmodels

TableModel {

    TableModelColumn { display: "col1"; edit: "col1"  }
    TableModelColumn { display: "col2"; edit: "col2"  }

    rows: [
        {col1: "Value 1", col2: "Value 2"},
        {col1: "Value 3", col2: "Value 4"},
        {col1: "Value 5", col2: "Value 6"}
    ]
}
