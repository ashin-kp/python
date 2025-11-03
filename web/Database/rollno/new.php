<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form>
        <select>
            Rollno:
 <?php
$con=mysqli_connect("localhost","root","","student");
if($con)
{
    echo "connection successfull";
}
$sq="select rollno from stud";
$result=mysqli_query($con,$sq);
if(mysqli_num_rows($result)>0)
{  
    while($row=mysqli_fetch_assoc($result))
    {
    echo "<option value=".$row['rollno'].">". $row['rollno'] ."</option>";
    }
}
else{
    echo "<option>"."rollno not found"."</option>";
}
?>
</select>
</form>
</body>
</html>
