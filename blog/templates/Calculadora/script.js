window.onload = function(e){

var calculo="";
     
     
     
function borrar(){
    var borro = document.a.display.value;
    var nuevo = borro.substring(0,borro.length -1);
    document.getElementById("display").value = nuevo;
    
}     
     
     
     
function borrotodo(){
    
    
document.getElementById("display").value = "";
}     
     
function numeros(e){
    
key = e.keycode || e.which;
    
    teclado = String.fromCharCode (key);
    
    nums = "123456789/*-+0";
    
    if (nums.indexOf(teclado) == -1){
        return false;
    }
    
    
    
    
}

 function mostrar(id){       
  
var operacion = document.a.display.value;


document.getElementById("display").value = operacion + id;
     
console.log(operacion);
    
}    
    
function resultado(){
   
    calculo = document.a.display.value;
    document.getElementById("display").value=calculo;
    
    eval(calculo);
    
    document.a.display.value = eval(calculo);
    
} 
    
}