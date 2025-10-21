import QtQuick

ListModel {

    Component.onCompleted: {
        for (var i = 0; i < 5; ++i) {
            var randomValue = Math.floor(Math.random() * 10) + 1;
            append({ value: randomValue });
        }
    }

    function refresh() {
        for (var i = 0; i < 5; ++i) {
            var randomValue = Math.floor(Math.random() * 10) + 1;
            set(i, {value: randomValue});
        }
    }
}
