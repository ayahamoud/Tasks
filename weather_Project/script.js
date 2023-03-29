const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': '70b817d22bmsh1840d1c71ea584ep1aa09fjsn32ade13c5985',
        'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
    }
};
const getWeather = (city) => {
    cityName.innerHTML = city
    fetch('https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=' + city, options)
        .then(response => response.json())
        .then((response) => {
            console.log(response)
            humidity.innerHTML = response.humidity
            temp.innerHTML = response.temp
            wind_speed.innerHTML = response.wind_speed
        })
        .catch(err => console.error(err));
}

submit.addEventListener("click", (e) => {
    e.preventDefault()
    getWeather(city.value)
})

getWeather("Haifa")