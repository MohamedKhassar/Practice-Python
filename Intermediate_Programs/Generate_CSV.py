import pandas as pd
import random
import datetime

languages = ["Python", "JavaScript", "Java", "C++", "Ruby", "Go", "Rust", "Swift", "Kotlin", "PHP"]
problems = {
    "Python": [
        "Print 'Hello, world'",
        "Create a function to add two numbers",
        "Write a script to read a file",
        "Generate a random number",
        "Make an HTTP request using requests library"
    ],
    "JavaScript": [
        "Print 'Hello, world' to the console",
        "Create a function to add two numbers",
        "Manipulate the DOM",
        "Make an AJAX request",
        "Create a promise"
    ],
    "Java": [
        "Print 'Hello, world' to the console",
        "Create a method to add two numbers",
        "Read a file using FileReader",
        "Generate a random number",
        "Make an HTTP request using HttpClient"
    ],
    "C++": [
        "Print 'Hello, world' to the console",
        "Create a function to add two numbers",
        "Read a file using fstream",
        "Generate a random number",
        "Make an HTTP request using libcurl"
    ],
    "Ruby": [
        "Print 'Hello, world' to the console",
        "Create a method to add two numbers",
        "Read a file",
        "Generate a random number",
        "Make an HTTP request using Net::HTTP"
    ],
    "Go": [
        "Print 'Hello, world' to the console",
        "Create a function to add two numbers",
        "Read a file using os package",
        "Generate a random number",
        "Make an HTTP request using net/http"
    ],
    "Rust": [
        "Print 'Hello, world' to the console",
        "Create a function to add two numbers",
        "Read a file using std::fs",
        "Generate a random number",
        "Make an HTTP request using reqwest"
    ],
    "Swift": [
        "Print 'Hello, world' to the console",
        "Create a function to add two numbers",
        "Read a file using FileManager",
        "Generate a random number",
        "Make an HTTP request using URLSession"
    ],
    "Kotlin": [
        "Print 'Hello, world' to the console",
        "Create a function to add two numbers",
        "Read a file using File",
        "Generate a random number",
        "Make an HTTP request using HttpURLConnection"
    ],
    "PHP": [
        "Print 'Hello, world'",
        "Create a function to add two numbers",
        "Read a file using fopen",
        "Generate a random number",
        "Make an HTTP request using cURL"
    ]
}

data=[]


for i in range(400):
    random_lang=random.choice(languages)
    data.append({
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Language": random_lang,
        "Problem": random.choice(problems[random_lang]),
    })

dt=pd.DataFrame(data)

dt.to_csv("./favorites.csv",index=False)