import QtQuick

QtObject {

    id: root

    property ListModel model: ListModel {}
    property int currentIndex: 0

    signal selected(int index)

    function selectItem(index) {
    
        if (index >= 0 && index < model.count) {
            currentIndex = index
            selected(index)
            console.log(
                "Selection changed in ViewModel: Index "
                + index + ", Name: " + model.get(index).name +
                ", Value: " + model.get(index).value)
        }
    }
}