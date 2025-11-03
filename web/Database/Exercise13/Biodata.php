<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <style>
        body{
            margin:0;
            align-items:center;
            justify-content:center;
            font-family:Poppins;
            
        }
        form{
            border:1px solid black;
            height:80vh;
            display:flex;
            flex-direction:column;
            padding:80px;
            background:lightblue;
        }

    </style>
</head>
<body>
    <form action="new.php" method="POST">
        Rollno:<input type="number" name="rno">
        <br>
        Name: <input type="text" name="name" >
         <br>
        Gender:<br><br><div id="gen"><input type="radio" name="gender" value="male">Male
              <input type="radio" name="gender" value="female">Female</div>
                <br>
                <br>
        Mark1: <input type="number" name="mark1">
         <br>
        Mark2: <input type="number" name="mark2">
         <br>
        <input type="submit" value="Save">
         <br>
        <input type="reset" value="reset">

   </form>
    </body>
</html>