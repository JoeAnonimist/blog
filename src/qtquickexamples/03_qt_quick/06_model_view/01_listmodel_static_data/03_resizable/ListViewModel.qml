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
    
    function append() {
        console.log("in append")
        model.append({"name": getNextItemName(), "value": 0})
    }
    
    function insert() {
        console.log("in insert")
        model.insert(currentIndex, {"name": getNextItemName(), "value": 0})
        selected(currentIndex)
    }
    
    function removeCurrent() {
        console.log("remove curent")
        model.remove(currentIndex)
        if (currentIndex == model.count) {
            currentIndex--;
            selected(currentIndex)
        }
    }
    
    function getNextItemName() {
        if (model.count === 0) return "Item 0";

        var maxNum = -1;
        for (var i = 0; i < model.count; ++i) {
            var itemName = model.get(i).name;
            var match = itemName.match(/Item (\d+)/);
            if (match) {
                var num = parseInt(match[1], 10);
                if (num > maxNum) {
                    maxNum = num;
                }
            }
        }
        console.log(maxNum + 1)
        return "Item " + (maxNum + 1);
    }
}