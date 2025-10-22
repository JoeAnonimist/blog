import QtQuick

ListModel {

    Component.onCompleted: {
        for (var i = 0; i < 10; ++i) {
            addItem();
        }
    }

    function addItem() {
        var randomValue = Math.floor(Math.random() * 10) + 1;
        append({ value: randomValue })
    }
}
