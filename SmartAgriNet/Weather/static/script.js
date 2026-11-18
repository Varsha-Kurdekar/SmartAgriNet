async function searchTemperature() {

    const cityName =
        document.getElementById("cityInput").value;

    const apiKey =
        "8ad5edd9ef4d8c913b041c552fcf41ba";

    const url =
`https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=metric`;

    try {

        const response = await fetch(url);

        const data = await response.json();

        if (data.cod == "404") {

            alert("City not found");

            return;
        }

        document.getElementById("temp").innerHTML =
            Math.round(data.main.temp) + "°C";

        document.getElementById("city").innerHTML =
            data.name;

        document.getElementById("weather").innerHTML =
            data.weather[0].main;

        document.getElementById("icon").src =
`https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;

    }

    catch(error) {

        alert("Error fetching weather data");

        console.log(error);
    }
}