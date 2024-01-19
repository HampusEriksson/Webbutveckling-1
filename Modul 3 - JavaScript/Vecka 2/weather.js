let temperatureSlider = document.getElementById("temperatureSlider");
let selectedTemperatureElement = document.getElementById("selectedTemperature");
let weatherMessageElement = document.getElementById("weatherMessage");

// Initial display of selected temperature
selectedTemperatureElement.innerText = temperatureSlider.value + "°C";

// Initial update of weather message based on the default temperature
updateWeatherMessage(temperatureSlider.value);

// Event listener for slider change
temperatureSlider.addEventListener("input", function() {
    // Update the displayed temperature
    selectedTemperatureElement.innerText = temperatureSlider.value + "°C";

    // Update the weather message based on the selected temperature
    updateWeatherMessage(temperatureSlider.value);
});

// Function to update the weather message
function updateWeatherMessage(temperature) {
    if (temperature > 30) {
        weatherMessageElement.innerText = "It's a hot day!";
        weatherMessageElement.style.color = "red";
    } else if (temperature <= 30 && temperature >= 20) {
        weatherMessageElement.innerText = "The weather is pleasant.";
        weatherMessageElement.style.color = "green";
    } else {
        weatherMessageElement.innerText = "It's a bit chilly.";
        weatherMessageElement.style.color = "blue";
    }
}

