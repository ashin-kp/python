<?php 
echo "Rno : ".$_POST['rno']."<br>";
echo "name : ".$_POST['name']."<br>";
 
$name = $_POST['name'];
$rno = $_POST['rno'];

$con=mysqli_connect('localhost','root','','student');
if($con)
    echo "connection successfull!";
else
    echo "connection failed!";
$sq = "INSERT INTO stud values($rno,'$name')"; 
if(mysqli_query($con,$sq))
    echo "<script>alert('inserted');</script>";
else
    echo "failed";
?>