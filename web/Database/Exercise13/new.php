<?php
$rno = $_POST['rno']; 
$name = $_POST['name']; 
$gender = $_POST['gender']; 
$mark1= $_POST['mark1']; 
$mark2 = $_POST['mark2']; 
$total = $mark1 + $mark2;

$con = mysqli_connect('localhost','root','','student');
if($con)
    echo "connection established successfully";
else
    echo "connection error";

$sq="select rollno from biodata where rollno=$rno";
$result=mysqli_query($con,$sq);
if(mysqli_num_rows($result)>0)
{
    echo "<script>alert('Roll no already exist'); document.location='Biodata.php';</script>";
}
else{
$sq = "INSERT INTO biodata values ($rno,'$name','$gender',$mark1,$mark2,$total)";

if(mysqli_query($con,$sq))
    echo "<script>alert('inserted successfully'); document.location ='Biodata.php';</script>";
else
    echo "insertion error";
}



?>