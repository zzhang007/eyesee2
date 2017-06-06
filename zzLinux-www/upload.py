<?php
$size0 = 1956;
$size1 = 1934;
      
$img = basename($_FILES["fileToUpload"]["name"]);
$upload_dir = "/tmp-eyesee/uploads/";
$upload_ff = $upload_dir.$img;
$result_dir = "/tmp-eyesee/result/";
$result_ff = $result_dir.$img.'.txt';
$uploadOk = 1;
$imageFileType = pathinfo($upload_ff,PATHINFO_EXTENSION);
       
echo "starting at : ";
$dd = new DateTime();
echo $dd->format('Y-m-d-H-i-s');
echo "<hr>";
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
       if($check[0] == $size0 && $check[1] == $size1) {          
          $uploadOk = 1;
        }else{
          echo "Image size or type incorrect<hr>";    
          $uploadOk = 0;
        }    
    } else {
        echo "File is not an image<hr>";
        $uploadOk = 0;
    }
}      
        
// Check if file already exists
if (file_exists($upload_ff)) {
    echo "Sorry, file already exists<hr>";
    $uploadOk = 0;
} 

// Check file size
if ($_FILES["fileToUpload"]["size"] > 3000000) {
    echo "Your file is too large, limited to <3G ! <hr>";
    $uploadOk = 0;
}

if($imageFileType != "jpg" && $imageFileType != "jpeg" 
   && $imageFileType != "JPG" && $imageFileType != "JPEG"   ) {
    echo "Only JPG, JPEG files are allowed<hr>";
    $uploadOk = 0;
}

if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded<hr>";
} else {
    echo "<hr>Good image, file size=".$_FILES["fileToUpload"]["size"] .
         ";  image size = ".$check[0]." X ".$check[1]."<hr>";       
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], 
                           $upload_ff)) {
        echo "The file ". 
        basename( $_FILES["fileToUpload"]["name"]). 
                " has been uploaded<hr>";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}

if($uploadOk==1) {
while (!file_exists ( $result_ff) ) {
}

sleep(1);
echo "result obtained from computing server <br>".$result_ff."<br>";
$ff = fopen($result_ff,"r") or die("Unable to open file!");
$ll= fgets($ff);   
$ll= fgets($ff);
echo "diagnosis result : ".$ll."<hr>";
fclose($ff);
  echo "ending at : ";
  $dd = new DateTime();
  echo $dd->format('Y-m-d-H-i-s');
}
echo "<h2>Return to  <a href='index.html'> image upload page </a></h2>";

?>
