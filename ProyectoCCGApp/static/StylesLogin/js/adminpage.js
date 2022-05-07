(function(){
   let input,filtro,table,tr,td,txtValue;

   //Variables inicializadas
   input = document.querySelector('.input-search');
   filter =  input.value.toUpperCase();
   table = document.querySelector('.table-users');
   tr = table.getElementsByTagName('tr');

   for(let i = 0; i<tr.length; i++){
       td = tr[i].getElementsByTagName('td')[0];
       if(td){
           txtValue = td.textContent || td.innerText;
           if(txtValue.toUpperCase().indexOf(filtro)> -1){
               tr[i].style.display = '';
           }else{
               tr[i].style.display = 'none';
           }
       }
   }
})();