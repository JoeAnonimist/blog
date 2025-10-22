import QtQuick

ListModel {

    enum Type {
        File,
        Folder
    }

    ListElement {name: "File 1"; type: Model.Type.File}
    ListElement {name: "Folder 1"; type: Model.Type.Folder}
    ListElement {name: "File 2"; type: Model.Type.File}
    ListElement {name: "File 3"; type: Model.Type.File}
    ListElement {name: "File 4"; type: Model.Type.File}
    ListElement {name: "Folder 2"; type: Model.Type.Folder}
    ListElement {name: "File 5"; type: Model.Type.File}
    ListElement {name: "File 6"; type: Model.Type.File}
    ListElement {name: "Folder 3"; type: Model.Type.Folder}
    ListElement {name: "File 7"; type: Model.Type.File}
}
