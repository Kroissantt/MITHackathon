<!DOCTYPE html>
<html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- labels tab -->
  <title> Recipe Receiver </title>
<div style ="background-color: MintCream; background-size:cover; text-align: justify; font-family: sans-serif; font-style: italic;"
</head>

<body>
<h1> Welcome to the Recipe Receiver!</h1>
<p>Enter the ingredients that you wish to use!</p>

  <form method="post">
    <div>
      <input type="text" name="i1" placeholder="Ingredient 1">
    </div>
    <div>
      <input type="text" name="i2" placeholder="Ingredient 2">
    </div>
    <div>
      <input type="text" name="i3" placeholder="Ingredient 3">
    </div>
    <div class="button">
      <button type="submit">submit</button>
    </div>
  </form>

</body>

<?php
if(isset($_POST['i1'])){
  $data=$_POST ['i1'];
  $data2=$_POST['i2'];
  $fp = fopen('data.txt', 'a');
  fwrite($fp, $data);
  fclose($fp);
}

if(isset($_POST['i1'])){
  $data2=$_POST['i2'];
  $fp = fopen('data.txt', 'a');
  fwrite($fp, $data2);
  fclose($fp);
}

if(isset($_POST['i1'])){
  $data3=$_POST['i3'];
  $fp = fopen('data.txt', 'a');
  fwrite($fp, $data3);
  fclose($fp);
}

if(isset($_POST['i1'])){
  $response="http://www.recipepuppy.com/api/?i=$data,$data2,$data3&format=json";
  $rp_json = json_decode(file_get_contents($response));
  #foreach ($row->$value in $rp_json) P
  echo "Here's a list of recipies with these ingredients! (Just click on any recipes you like!)";

  $res = $rp_json->results;
  $tablestr = "<table>";
  foreach($res as $key=>$val) {
    $tablestr .= "<tr>";
    $tablestr .= "<td> $val->title </td>";
    $tablestr .= "<td> $val->ingredients </td>";
    $tablestr .= "<td> <a href='$val->href'>Click Here for the Recipe!</a> </td>";
    $tablestr .= "</tr>";
    #print_r($val->href);
  }
  $tablestr .= "</table>";
  echo $tablestr;
  //$fp = fopen('response.txt', 'a');
  //fwrite($fp, $response);
  //fclose($fp);

}

?>
</html>
