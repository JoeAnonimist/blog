import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {

    visible: true
    width: 200
    height: 700
    title: "Type conversions"
    
    property int intValue
    property real floatValue
    property bool boolValue
    property string strValue
    property var byteValue
    property var listValue
    property var tupleValue
    property var dictValue
    property var noneValue
    property color qcolorValue
    property var qpointValue
    property date qdateValue
    property date qdatetimeValue
    property var qtimeValue
    property url qurlValue
    property var setValue
    property var bytesValue
    property var rangeValue
    property var complexValue
    
    Component.onCompleted: {
        console.log("intValue:", intValue, typeof intValue)
        console.log("floatValue:", floatValue, typeof floatValue)
        console.log("boolValue:", boolValue, typeof boolValue)
        console.log("strValue:", strValue, typeof strValue)
        console.log("byteValue:", Object.prototype.toString.call(byteValue).slice(8, -1))
        console.log("listValue:", listValue, Object.prototype.toString.call(listValue).slice(8, -1))
        console.log("tupleValue:", tupleValue, Object.prototype.toString.call(tupleValue).slice(8, -1))
        console.log("dictValue:", dictValue, Object.prototype.toString.call(dictValue).slice(8, -1))
        console.log("noneValue:", typeof noneValue)
        console.log("qcolorValue:", qcolorValue, typeof qcolorValue)
        console.log("qpointValue:", qpointValue, typeof qpointValue)
        console.log("qdateValue:", qdateValue.toString(), typeof qdateValue)
        console.log("qdatetimeValue:", qdatetimeValue.toString(), typeof qdatetimeValue)
        console.log("qtimeValue:", qtimeValue.toString(), typeof qtimeValue)
        console.log("qurlValue:", qurlValue.toString(), typeof qurlValue)
        console.log("setValue:", setValue, Object.prototype.toString.call(setValue).slice(8, -1))
        console.log("bytesValue:", Object.prototype.toString.call(bytesValue).slice(8, -1))
        console.log("rangeValue:", rangeValue, Object.prototype.toString.call(rangeValue).slice(8, -1))
        console.log("complexValue:", complexValue, typeof complexValue)
    }
    
    ColumnLayout {
    
        anchors.fill: parent
        anchors.margins: 4
    
        RowLayout {
            Text {text: intValue}
            Text {text: typeof intValue}
        }
        RowLayout {
            Text {text: floatValue}
            Text {text: typeof floatValue}
        }
        RowLayout {
            Text {text: boolValue}
            Text {text: typeof boolValue}
        }
        RowLayout {
            Text {text: strValue}
            Text {text: typeof strValue}
        }
        RowLayout {
            Text {
                text: {
                    var uint8Array = new Uint8Array(byteValue);
                    var values = [];
                    for (var i = 0; i < uint8Array.length; i++) {
                        values.push(uint8Array[i]);
                    }
                    return "[" + values.join(", ") + "]";
                }
            }
            Text {text: Object.prototype.toString.call(byteValue).slice(8, -1)}
        }
        RowLayout {
            Text {
                text: {
                    var values = [];
                    for (var i = 0; i < listValue.length; i++) {
                        values.push(listValue[i]);
                    }
                    return "[" + values.join(", ") + "]";
                }
            }
            Text {text: Object.prototype.toString.call(listValue).slice(8, -1)}
        }
        RowLayout {
            Text { text: tupleValue.toString()}
            Text {text: Object.prototype.toString.call(tupleValue).slice(8, -1)}
        }
        RowLayout {
            Text {
                text: {
                    var value = ""
                    Object.keys(dictValue).forEach((key) => {
                        value += key + ": " + dictValue[key] + ", "
                    })
                    return value
                }
            }
            Text {text: Object.prototype.toString.call(dictValue).slice(8, -1)}
        }
        RowLayout {
            //Text {text: noneValue}
            Text {text: typeof noneValue}
        }
        RowLayout {
            Text {text: qcolorValue; color: qcolorValue}
            Text {text: typeof qcolorValue}
        }
        RowLayout {
            Text {text: "{" + qpointValue.x + ", " + qpointValue.y + "}"}
            Text {text: typeof qpointValue}
        }
        RowLayout {
            Text {text: qdateValue.toString()}
            Text {text: typeof qdateValue}
        }
        RowLayout {
            Text {text: qdatetimeValue.toString()}
            Text {text: typeof qdatetimeValue}
        }
        RowLayout {
            Text {text: qtimeValue.toString()}
            Text {text: typeof qtimeValue}
        }
        RowLayout {
            Text {text: qurlValue.toString()}
            Text {text: typeof qurlValue}
        }
        RowLayout {
            Text {
                text: {
                    var values = [];
                    for (var i = 0; i < setValue.length; i++) {
                        values.push(setValue[i]);
                    }
                    return "[" + values.join(", ") + "] (unordered)"
                }
            }
            Text {text: Object.prototype.toString.call(setValue).slice(8, -1)}
        }
        RowLayout {
            Text {
                text: {
                    var uint8Array = new Uint8Array(bytesValue);
                    var values = [];
                    for (var i = 0; i < uint8Array.length; i++) {
                        values.push(uint8Array[i]);
                    }
                    return "[" + values.join(", ") + "]";
                }
            }
            Text {text: Object.prototype.toString.call(bytesValue).slice(8, -1)}
        }
        RowLayout {
            Text {
                text: {
                    var values = [];
                    for (var i = 0; i < rangeValue.length; i++) {
                        values.push(rangeValue[i]);
                    }
                    return "[" + values.join(", ") + "]"
                }
            }
            Text {text: Object.prototype.toString.call(rangeValue).slice(8, -1)}
        }
        RowLayout {
            Text {text: complexValue.toString()}
            Text {text: typeof complexValue}
        }
    }
}