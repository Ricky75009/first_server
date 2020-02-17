#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

v_name= form.getvalue('name')


print('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>LOVE the best</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
  </head>  
  <style>

  <body>
    <h1>Hello %s!</h1>
    
    <p>
      Look how nice you are, look at what you are  <a href="https://giphy.com/gifs/lamborghini-lambo-countach-l3UcrZHrGW2CjHXqM/fullscreen">Cool GIF</a>!
    </p>
  </body>
</html>'''% v_name)
