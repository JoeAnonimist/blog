import QtQuick

QtObject {
    id: root

    property ListModel listModel: ListModel {}

    property StateGroup stateGroup: StateGroup {
        id: stateGroup
        states: [
            State { name: "waiting" },
            State {
                name: "updating"
                StateChangeScript {
                    name: "update"
                    script: refresh();
                }
            }
        ]
    }

    Component.onCompleted: {
        for (var i = 0; i < 5; ++i) {
            var randomValue = Math.floor(Math.random() * 100) + 1;
            listModel.append({ value: randomValue });
        }
        //stateGroup.state = "waiting"
    }

    function refresh() {
        //stateGroup.state = "updating"
        for (var i = 0; i < listModel.count; ++i) {
            var randomValue = Math.floor(Math.random() * 100) + 1;
            listModel.set(i, {value: randomValue});
        }
        Qt.callLater(() => stateGroup.state = "waiting")
        //stateGroup.state = "waiting"
    }
}
