



let loopList = document.getElementById("loopList");

for (let i = 1; i <= 5; i++) {
    let listItem = document.createElement("li");
    listItem.innerText = "Count: " + i;
    loopList.appendChild(listItem);
}

let loopList2 = document.getElementById("loopList");

for (let i = 1; i <= 5; i++) {
    loopList2.innerHTML += "<li>Count: " + i + "</li>";
}




    
