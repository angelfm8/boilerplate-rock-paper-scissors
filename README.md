# boilerplate-rock-paper-scissors
Proyecto "Rock, Paper, Scissors" del curso de Machine Learning with Python de FreeCodeCamp

El proyecto consiste en crear un bot que derrote a los otros bots al menos un 60% de las veces

El bot en cuestión se encuentra en el archivo RPS.py
Su funcionamiento consiste en recoger el historial de movimientos del oponente y agruparlo en paquetes de 6 (número elegido por ser el óptimo en este caso). Se va añadiendo mas valor a medida que los paquetes de 6 se repiten y se escoge como predicción el paquete que tenga mas probabilidad de aquellos en los cuales coinciden las 5 primeras letras con los 5 ultimos movimientos del oponente. La predicción será la 6 letra y en función de esta predicción el bot juega el opuesto.
