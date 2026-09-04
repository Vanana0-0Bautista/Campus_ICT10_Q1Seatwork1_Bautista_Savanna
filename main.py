from pyscript import document, display, HTML

display("Welcome to My Introduction Page", target="me_output")

# string
name = "Savanna"

# integer
age = 15

# float
height123 = 160.0

# list
three_countries = [
    "Japan",
    "Australia",
    "Vietnam"
]

# boolean
student_type = True

# dict
student_info = {
    "color": "pink",
    "car_brand": "Toyota",
    "shoe_size": 6,
    "best_friend": "Sam"
}

# set
favorite_fruits = {
    "Mango",
    "Banana",
    "Watermelon",
    "Grapes",
    "Apple"
}

# tuple
days_of_the_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

info_html = f"""
<p><strong>Name:</strong> {name}</p>

<p><strong>Age:</strong> {age}</p>

<p><strong>Height (cm):</strong> {height123}</p>

<p><strong>Countries to Visit:</strong> {three_countries}</p>

<p><strong>Student Type (New Student?):</strong> {student_type}</p>

<p><strong>Student Info:</strong> {student_info}</p>

<p><strong>Favorite Fruits:</strong> {favorite_fruits}</p>

<p><strong>Days of the Week:</strong> {days_of_the_week}</p>
"""

display(HTML(info_html), target="me_output")

