<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8">
    <title>MatheMerch</title>
    <meta name="description" content="Kurzbeschreibung">
    <link href="css/design.css" rel="stylesheet">
  </head>
  <body>
    <div id="wrapper">
      <div id="header">
        <?php include("header.php"); ?>
      </div>
      <div id="side_left">
      </div>
      <div id="navi">
        <?php include("nav.php"); ?>
      </div>
      <div id="side_right">
      </div>
      <div id="content">
        <h1>Shop</h1>
        <h2>Mathe - Merch:</h2>
        <table border="0" width="800px" cellpadding="4">
          <tr>
            <td><img src="pictures/gelber_pulli.jpg"></td>
            <td><img src="pictures/pulli_tuerkis.jpg"></td>
            <td><img src="pictures/schwarzer_pulli.jpg"></td>
            <td><img src="pictures/tshirt_weiss.jpg"></td>
            <td><img src="pictures/tshirt_schwarz.jpg"></td>
          </tr>
          <tr>
            <td><a class="hover" href="sw_gelb.php">Sweatshirt unisex (Gelb) </br> 16,99 &euro;</a></td>
            <td><a class="hover" href="sw_tuerkis.php">Sweatshirt unisex (Türkis) </br> 16,99 &euro;</a></td>
            <td><a class="hover" href="sw_schwarz.php">Sweatshirt unisex (Schwarz) </br> 16,99 &euro;</a></td>
            <td><a class="hover" href="tshirt_weiß.php">T-Shirt Herren (Weiß) </br> 7,99 &euro;</a></td>
            <td><a class="hover" href="tshirt_schwarz.php">T-Shirt Herren (Schwarz) </br> 7,99 &euro;</a></td>
          </tr>
        </table>
      </div>
      <div id="footer">
        <?php include("footer.php"); ?>
      </div>
    </div>
  </body>
</html>