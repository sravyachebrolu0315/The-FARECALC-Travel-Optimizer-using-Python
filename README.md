# The-FARECALC-Travel-Optimizer_Python

<h3>Business Case:</h3>
<p>A ride-sharing startup, "CityCab," needs a backend script to calculate fares. The fare isn't flat; it changes based on the time of day (Peak Hours) and the type of vehicle requested.</p>

<h3>Problem Statement:</h3>
<p>Write a script that calculates the final "Ride Estimate" based on distance, vehicle type, and a "Surge Pricing" multiplier.</p>

<h3>Student Tasks:</h3>
<ul>
<li> <b>Dictionary Mapping:</b> Store rates in a dictionary: {'Economy': 10, 'Premium': 18, 'SUV': 25} (rates per km). </li>
<li> <b>Surge Logic:</b> Ask the user for the "Hour of Day" (0-23). If the hour is between 17 and 20 (5 PM - 8 PM), apply a 1.5x Surge Multiplier to the total.</li>
<li> <b>Function Definition:</b> Create a function calculate_fare(km, type, hour) that returns the final price.</li>
<li> <b>Error Handling:</b> If the user enters a vehicle type not in your dictionary, use a try-except block or an if-in check to provide a "Service Not Available" message.</li>
</ul>

<h3>Deliverable: </h3>
<p>A .py script that takes user input and prints a formatted "Price Receipt."</p>
