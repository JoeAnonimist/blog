import QtQuick

QtObject {

    id: root

    property ListModel model: ListModel {}
    property int currentIndex: 0
    property int originalValue

    signal selected(int index)

    function selectItem(index) {
        if (index >= 0 && index < model.count) {
            currentIndex = index
            selected(index)
        }
    }
    
    function updateValue(value) {
        model.setProperty(currentIndex, "value", value)
        console.log(model.get(currentIndex))
    }
}