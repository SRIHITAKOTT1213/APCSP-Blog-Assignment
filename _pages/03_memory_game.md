---
layout: page
permalink: /memorygame
title: Memory Game
---

<style>
    {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
    }
    body {
        background-color: #ffcc66;
    }
    .wrapper{
        box-sizing: border-box;
        width: 26.87em;
        padding: 2.5em 3em;
        background-color: #ffffff;
        position: absolute;
        transform: translate(-50%, -50%);
        left: 50%;
        top: 50%;
        border-radius: 0.6em;
        box-shadow: 0 0.9em 2.8em rgba(86, 66, 0, 0.2);

    }
    .game-container {}
</style>

<!DOCTYPE html>
<html lang="en">
<body>
<div class="wrapper">
    <div class="stats-container">
        <div id="moves-count"></div>
        <div id="time"></div>
    </div>
    <div class="game-container"></div>
    <button id="stop" class="hide">Stop Game</button>
</div>
<div class="controls-container">
    <p id="result"></p>
    <button id="start">Start Game</button>
</div>
</body>
</html>