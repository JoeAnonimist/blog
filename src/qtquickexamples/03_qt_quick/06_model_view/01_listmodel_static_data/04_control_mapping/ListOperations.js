
function addItem(model, listView) {
    model.append({ name: "New Item", value: 0 });
    listView.currentIndex = model.count - 1;
    listView.positionViewAtIndex(listView.currentIndex, ListView.End);
}

function removeCurrentItem(model, listView) {
    const idx = listView.currentIndex;
    if (idx >= 0 && idx < model.count) {
        model.remove(idx, 1);
        listView.currentIndex = Math.min(idx, model.count - 1);
    }
}

function updateItem(model, listView, idx, newName, newValue) {
    if (idx >= 0 && idx < model.count) {
        if (newName !== model.get(idx).name) {
            model.setProperty(idx, "name", newName);
        }
        if (newValue !== model.get(idx).value) {
            model.setProperty(idx, "value", newValue);
        }
        listView.forceActiveFocus();
    }
}