<!DOCTYPE html>
<html>

<head>
  <title>HW07</title>
</head>

<body>
  <h1>HW07 - Uploading Files</h1>

  <form action="upload.php" method="post" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload Image" name="submit">
  </form>
</body>

</html>