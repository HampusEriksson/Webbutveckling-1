
document.addEventListener("DOMContentLoaded", function() {


    let loopList = document.getElementById("loopList");

    for (let i = 1; i <= 5; i++) {
        let listItem = document.createElement("li");
        listItem.innerText = "Count: " + i;
        loopList.appendChild(listItem);
    }
});

var EventHandlers = (function() {
    function initialize() {

        var loopList = document.getElementById("loopList");
        var loopList2 = document.getElementById("loopList2");
        var loopList3 = document.getElementById("loopList3");

    }

    return {
        initialize: initialize
    };
})();
