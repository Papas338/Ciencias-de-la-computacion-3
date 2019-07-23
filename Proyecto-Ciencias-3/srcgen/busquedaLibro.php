<!DOCTYPE html>
<head>

    <title>Libro</title>
    <!-- Bootstrap Core CSS -->
    <?php
    $link = new PDO('mysql:host=localhost;dbname=restaurante', 'root', '12345');

  ?>
    <link rel="stylesheet" type="text/css" href="estiloLibro.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                </ul>
                    <div class="flexsearch">
                        <div class="flexsearch--wrapper">
                            <form class="flexsearch--form" action="#" method="post">
                            </form>
                        </div>
                    </div>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>
    <!-- Page Content -->

    <div class="container">
        <div class="row">
            <div class="col-md-3">
                <p class="lead">Tipo Libro</p>
                <input type="text" id="myInput" onkeyup="FuncionTipo()" placeholder="Tipo especifico..."><!--Buscador de tipo de comida-->
                <p class="lead">Precio Libro</p>
                <input type="text" id="myInput2" onkeyup="FuncionPrecio()" placeholder="precio especifico..."><!--Buscador de precio de comida-->

                <!--<div class="list-group">
                    <input type="button" value="Entrada" id="myInput" onkeyup="myFunction()" class="list-group-item">
                    <input type="button" value="Plato Fuerte" id="myInput" onkeyup="myFunction()" class="list-group-item">
                    <input type="button" value="Bebida" id="myInput" onkeyup="myFunction()" class="list-group-item">
                </div>-->
            </div>

<div class="table-responsive">
    <table id="source" class="table table-bordered table-hover">
        <thead>
            <tr class="encabezado">
                    <th style="width:1%;">Id</th>
                    <th style="width:1%;">Nombre</th>
                    <th style="width:1%;">Genero</th>
                    <th style="width:1%;">Accion</th>
            </tr>
        </thead>
        <tbody>
          <?php foreach ($link->query('SELECT * from Libros') as $row){ // busqueda de platos. ?> 
            <tr>
                        <td><p align="center"><?php echo $row['id'] ?></p></td>
                        <td><img src="imagenes\<?php echo $row['id'] ?>.jpg" alt=""><br><br/><p align="center"><?php echo $row['nombre'] ?></p></td>
                        <td><p align="center"><?php echo $row['genero'] ?></p></td>
                        <td><button onclick="add(this)" class="btn btn-primary btn-xs"> Agregar Libro
                          </button>
                        </td>
            </tr>
            <?php
            }
          ?>
        </tbody>
    <tfoot>
    </tfoot>
</table>
</div>
<div class="container">
  <!-- Page Content -->
  <h1 class="row">Listado de Compras</h1>
  <table id="target" class="table table-bordered table-hover">
      <thead>
          <tr>                
            <th>NOMBRE</th>
              <th>TIPO</th>
              <th>PRECIO (PESOS $)</th>
              <th>CANTIDAD</th>
              <th>ACCIONES</th>
          </tr>
      </thead>
      <tbody>
      </tbody>
      <tfoot>
<tr class="total">
      <td>TOTAL: </td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
      </tfoot>
      
  </table> 

 </div>    
 <input type="button" class="btn btn-primary btn-xs" onclick="tableToExcel('target', 'name', 'Recibo.xls')" value="  Imprimir Recibo Libro  ">      
               
    <!-- /.container -->

    <div class="container">
        <hr>
        <!-- Footer -->
        <footer>
            <div class="row" style="text-align: right; margin-right:50px; margin-top:17%;">
                <div class="col-lg-12">
                    <p>Copyright &copy; Daniel Vargas - Jhonathan Rojas - David Garces - 2019</p>
                </div>
            </div>
        </footer>
    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>
 
    <!-- Script de la tabla -->
<script>
      
      function add(button) {
  var row = button.parentNode.parentNode;
  var cells = row.querySelectorAll('td:not(:last-of-type)');
  addToCartTable(cells);
  $(document).ready(function() {

 CalcularTotal();

});
}

function remove() {
  var row = this.parentNode.parentNode;
    document.querySelector('#target tbody')
            .removeChild(row);
    $(document).ready(function() {

 CalcularTotal();

});
}

function addToCartTable(cells) {
   var code = cells[1].innerText;
   var name = cells[2].innerText;
   var price = cells[3].innerText;
   
   var newRow = document.createElement('tr');
   newRow.setAttribute('data-price', price.substring(0));

   newRow.appendChild(createCell(code));
   newRow.appendChild(createCell(name));
   newRow.appendChild(createCell(price));
   var cellInputQty = createCell();
   cellInputQty.appendChild(createInputQty());
   newRow.appendChild(cellInputQty);
   var cellRemoveBtn = createCell();
   cellRemoveBtn.appendChild(createRemoveBtn())
   newRow.appendChild(cellRemoveBtn);
   
   document.querySelector('#target tbody').appendChild(newRow);

   $(document).ready(function() {

   CalcularTotal();

  });
  }

  function createInputQty() {
    var inputQty = document.createElement('input');
    inputQty.type = 'number';
    inputQty.required = 'true';
    inputQty.className = 'form-control'
    inputQty.min = 1;
    inputQty.onchange = onQtyChange;
    return inputQty;

    $(document).ready(function() {

   CalcularTotal();

  });
  }

  function createRemoveBtn() {
    var btnRemove = document.createElement('button');
    btnRemove.className = 'btn btn-xs btn-danger';
    btnRemove.onclick = remove;
    btnRemove.innerText = 'Descartar';
    return btnRemove;

    $(document).ready(function() {

   CalcularTotal();

  });
  }

  function createCell(text) {
    var td = document.createElement('td');
    if(text) {
      td.innerText = text;
    }
    return td;

    $(document).ready(function() {

   CalcularTotal();

  });
  }
  function onQtyChange(e) {
    var row = this.parentNode.parentNode;
    var cellPrice = row.querySelector('td:nth-child(3)');
    var prevPrice = Number(row.getAttribute('data-price'));
    var newQty = Number(this.value);
    var total = prevPrice * newQty;
    cellPrice.innerText = total;
    $(document).ready(function() {

   CalcularTotal();

  });
  }

  function CalcularTotal()
  {
  var totals = [ ,0, ];
   var $filas= $("#target tr:not('.total, .encabezado')");

    $filas.each(function() {
      $(this).find('td').each(function(i) {
        if (i != 0)
          totals[i - 1] += parseInt($(this).html());
      });
    });
    $(".total td").each(function(i) {
      if (i != 0)
        $(this).html(totals[i - 1]);
    });
  }

function FuncionTipo() {
          // Declare variables 
          var input, filter, table, tr, td, i, txtValue;
          input = document.getElementById("myInput");
          filter = input.value.toUpperCase();
          table = document.getElementById("source");
          tr = table.getElementsByTagName("tr");

          // Loop through all table rows, and hide those who don't match the search query
          for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[2];
            if (td) {
              txtValue = td.textContent || td.innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }
            } 
          }
        }
        function FuncionPrecio() {
          // Declare variables 
          var input, filter, table, tr, td, i, txtValue;
          input = document.getElementById("myInput2");
          filter = input.value.toUpperCase();
          table = document.getElementById("source");
          tr = table.getElementsByTagName("tr");

          // Loop through all table rows, and hide those who don't match the search query
          for (i = 0; i < tr.length; i++) {
            td = tr[i].getElementsByTagName("td")[3];
            if (td) {
              txtValue = td.textContent || td.innerText;
              if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
              } else {
                tr[i].style.display = "none";
              }
            } 
          }
        }
function tableToExcel(table, name, filename) {
        let uri = 'data:application/vnd.ms-excel;base64,', 
        template = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><title></title><head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta http-equiv="content-type" content="text/plain; charset=UTF-8"/></head><body><table>{table}</table></body></html>', 
        base64 = function(s) { return window.btoa(decodeURIComponent(encodeURIComponent(s))) },         format = function(s, c) { return s.replace(/{(\w+)}/g, function(m, p) { return c[p]; })}
        
        if (!table.nodeType) table = document.getElementById(table)
        var ctx = {worksheet: name || 'Worksheet', table: table.innerHTML}

        var link = document.createElement('a');
        link.download = filename;
        link.href = uri + base64(format(template, ctx));
        link.click();
}
</script>
 

</body>

</html>