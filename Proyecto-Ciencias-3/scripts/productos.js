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