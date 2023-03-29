<?php

session_start();

if (isset($_SESSION["user_id"])) {
    
    $mysqli = require __DIR__ . "/database.php";
    
    $sql = "SELECT * FROM user
            WHERE id = {$_SESSION["user_id"]}";
            
    $result = $mysqli->query($sql);
    
    $user = $result->fetch_assoc();
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Weather App</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
    
    <?php if (isset($user)): ?>
        <div class="container">
            <div class="title">
                <p>Weather App<img src="cloud.png" id="icon"></p>
                <p style="font-size: 20px;">Hello <?= htmlspecialchars($user["name"]) ?></p>
            </div>
            <div class="input">
                <input type="text" id="city" placeholder="Loaction ...">
                <input type="button" value="Get" id="submit">
            </div>
            <div class="info">
                <h3>Weather for <span id="cityName"></span></h3>
                <div class="temp">Temperature: <span id="temp"></span><span id="c">&#8451;</span></div>
                <div class="humidity">Humidity: <span id="humidity"></span>%</div>
                <div class="wind_speed">Wind: <span id="wind_speed"></span> km/hr</div>
                <p style="text-align: center;"><br><br><a href="logout.php">Log out</a></p>
            </div>
        </div>
        <script src="script.js"></script>
    <?php else: ?>
        <div class="container">
            <div class="title">
                <p>Home</p>
            </div>
            <div style="text-align: center;">
                <p ><a href="login.php">Log in</a></p>
                <p> or</p>
                <p> <a href="signup.html">sign up</a></p>
            </div>
        </div>
    <?php endif; ?>
    
</body>
</html>
    
    
    
    
    
    
    
    
    
    
    