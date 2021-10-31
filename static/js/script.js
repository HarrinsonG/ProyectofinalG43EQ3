var ind=1;
var transfor=false;
var autoPlayTimer;

window.onload=function(){

    var buttonlist=document.getElementById("button").getElementsByTagName("span");
    for(var i=0;i<buttonlist.length;i++){
        buttonlist[i].onclick=function(){
            if(transfor){
                return;
            }
            var myInd=parseInt(this.getAttribute("ind"));
            var offsetl=-600*(myInd-ind);
            ind=myInd;
            animate(offsetl);
            buttonBtn();
        };
    }

    var prev=document.getElementById("prev");
    var next=document.getElementById("next");
    next.onclick=function(){
        if(transfor){
            return;
        }
        if(ind===5){
            ind=1;
        }else{
            ind++;
        }
        animate(-600);
        buttonBtn();
    };

    prev.onclick=function(){
        if(transfor){
            return;
        }
        if(ind===1){
            ind=5;
        }else{
            ind--;
        } animate(600);
        buttonBtn();
    };

    autoPlayTimer();
    var BOX=document.getElementById("BOX");
    BOX.onmouseover=stop;
    BOX=onmouseout=autoPlay;

}

function animate(offset){

    transfor=true;
    var imgbox=document.getElementById("imgbox");
    var time=300;
    var inteval=10;
    var speed=offset/(time/inteval);
    var newleft=parseInt(imgbox.style.left)+offset;
    function go(){
        if((speed<0&&parseInt(imgbox.style.left)>newleft)||(speed>0&&parseInt(imgbox.style.left)<newleft)){
            imgbox.style.left=parseInt(imgbox.style.left)+speed+"px";
            setTimeout(go,inteval);
        }else{
            imgbox.style.left=newleft+"px";
            if(newleft<5*-600){
                imgbox.style.left=-600+"px";
            }

            if(newleft>-600){
                imgbox.style.left=-5*600+"px";
            }
            transfor=false;
        }
    }go();
}

function buttonBtn(){
    var buttonlist=document.getElementById("button").getElementsByTagName("span");
    for(var R=0;R<buttonlist.length;R++){
        if(buttonlist[R].className==="on"){
            buttonlist[R].className="";
            break;
        }
    }
    buttonlist[ind-1].className="on";
}

function autoPlay(){
    autoPlayTimer=setInterval(function(){
        if(transfor){
            return;
        }
        if(ind===5){
            ind=1;
        }else{
            ind++;
        }
        buttonBtn();
        animate(-600);
    },3000);
}

function stop(){
    clearInterval(autoPlayTimer);
}



function alerta()
    {
    var mensaje;
    var opcion = confirm("Desea eliminar el usuario");
    if (opcion == true) {
        mensaje = "Usuario eliminado correctamente";
	} else {
	    mensaje = "Has clickado Cancelar";
	}
	window.alert(mensaje);
}

function alerta2(){
    window.alert("El usuario a sido creado exitosamente");
}

function alerta3(){

    var vacio=0
    var nom=document.getElementById("nombre").value;
    var apell=document.getElementById("apellido").value;
    var identi=document.getElementById("identificacion").value;
    var user=document.getElementById("usuario").value;
    var email=document.getElementById("correo").value;
    var stado=0;
    var sexo=0;
    var tipo=0;

    var combo = document.getElementById("estado");
    var seleccionado = combo.options[combo.selectedIndex].text;

    var combo2 = document.getElementById("genero");
    var seleccionado2 = combo2.options[combo2.selectedIndex].text;

    var combo3 = document.getElementById("tipo_usuario");
    var seleccionado3 = combo3.options[combo3.selectedIndex].text;
    //alert(seleccionado);

    //genero
    if(seleccionado2=="Masculino"||seleccionado2=="Femenino"){
    //alert("se selecciono activo");
    sexo=1;
    }else{
        alert("Debe seleccionar un genero valido");
    }
    //estado
    if(seleccionado=="Activo"||seleccionado=="Inactivo"){
        //alert("se selecciono activo");
        stado=1;
        }else{
            alert("Debe seleccionar un estado valido");
        }
        //tipo cliente

        if(seleccionado3=="Usuario Final"||seleccionado3=="Administrador"||seleccionado3=="Superadministrador"){
            //alert("se selecciono activo");
            tipo=1;
            }else{
                alert("Debe seleccionar un tipo de cliente valido");
            }


        //vacio
    if (nom.length == 0 || apell.length == 0||identi.length == 0||user.length == 0||email.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }


    /*if(vacio==1&&stado==1&&sexo==1&&tipo==1){
    window.alert("El usuario ha sido modificado exitosamente");
    window.close();
    }*/
}


function alerta4()
    {
    var mensaje;
    var opcion = confirm("Desea eliminar el producto");
    if (opcion == true) {
        mensaje = "Producto eliminado exitosamente";
	} else {
	    mensaje = "Has clickado Cancelar";
	}
	window.alert(mensaje);
}

function alerta5(){

    var vacio=0;
    var gen=0;
    var cat=0;
    var disp=0
    var cod=document.getElementById("codigo").value;
    var nom=document.getElementById("nombre").value;
    var cant=document.getElementById("cantidad").value;

    var combo = document.getElementById("genero");
    var seleccionado = combo.options[combo.selectedIndex].text;

    var combo2 = document.getElementById("categoria");
    var seleccionado2 = combo2.options[combo2.selectedIndex].text;

    var combo3 = document.getElementById("estado");
    var seleccionado3 = combo3.options[combo3.selectedIndex].text;


    if (cod.length == 0 || nom.length == 0||cant.length == 0||seleccionado3.length==0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }

       if(seleccionado=="Femenino"||seleccionado=="Masculino"){
            gen=1;
       }else{
           alert("Seleccione un genero valido");
       }

       if(seleccionado2=="Ropa"||seleccionado2=="Calzados"||seleccionado2=="Bolsos"||seleccionado2=="Accesorios"||seleccionado2=="Ofertas"){
            cat=1;
        }else{
            alert("Seleccione una categoria valida");
        }

        if(seleccionado3=="Disponible"||seleccionado3=="No disponible"){
            disp=1;
        }else{
            alert("Seleccione un estado valido");
    }


  /*  if(vacio==1&&gen==1&&cat==1&&disp==1){
    window.alert("El producto ha sido modificado exitosamente");
    window.close();
}*/
}

function alerta6(){

    var vacio=0;
    var gen=0;
    var cat=0;
    var disp=0
    var cod=document.getElementById("codigo").value;
    var nom=document.getElementById("nombre").value;
    var cant=document.getElementById("cantidad").value;

    var combo = document.getElementById("genero");
    var seleccionado = combo.options[combo.selectedIndex].text;

    var combo2 = document.getElementById("categoria");
    var seleccionado2 = combo2.options[combo2.selectedIndex].text;

    var combo3 = document.getElementById("estado");
    var seleccionado3 = combo3.options[combo3.selectedIndex].text;


    if (cod.length == 0 || nom.length == 0||cant.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }

       if(seleccionado=="Mujer"||seleccionado=="Hombre"){
            gen=1;
       }else{
           alert("Seleccione un genero valido");
       }

       if(seleccionado2=="Ropa"||seleccionado2=="Calzado"||seleccionado2=="Bolsos"||seleccionado2=="Accesorios"){
            cat=1;
        }else{
            alert("Seleccione una categoria valida");
        }

        if(seleccionado3=="Disponible"||seleccionado3=="No Disponible"){
            disp=1;
        }else{
            alert("Seleccione un estado valido");
    }


    if(vacio==1&&gen==1&&cat==1&&disp==1){
        window.alert("El producto ha sido creado exitosamente");

    window.close();
}
}

function alerta7()
    {
    var mensaje;
    var opcion = confirm("Desea eliminar categoria");
    if (opcion == true) {
        mensaje = "Categoria eliminada exitosamente";
	} else {
	    mensaje = "Has clickado Cancelar";
	}
	window.alert(mensaje);
}

function alerta8(){
    var vacio=0;
    var disp=0;
    var nom=document.getElementById("nombre").value;
    var combo3 = document.getElementById("estado");
    var seleccionado3 = combo3.options[combo3.selectedIndex].text;
    
    if ( nom.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }

       if(seleccionado3=="Activo"||seleccionado3=="No activo"){
        disp=1;
    }else{
        alert("Seleccione un estado valido");
}
   
       if(vacio==1&&disp==1){
        window.alert("La categoria ha sido modificada exitosamente");
        window.close();
       }

    
}

function alerta9(){
    var vacio=0;
    var disp=0;
    var nom=document.getElementById("nombre").value;
    var combo3 = document.getElementById("estado");
    var seleccionado3 = combo3.options[combo3.selectedIndex].text;
    
    if ( nom.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }

       if(seleccionado3=="Activo"||seleccionado3=="No activo"){
        disp=1;
    }else{
        alert("Seleccione un estado valido");
}
   
       if(vacio==1&&disp==1){
        window.alert("La categoria agregada exitosamente");
        window.close();
       }

}

function alerta10(){

    if(selLista1.checked){
        cumple=1;
         
    }else{
        alert("Seleccione una lista");
        
    }
    if(cumple==1){
    window.alert("lista de deseos eliminada con exito");
    }
}

function alerta11(){
    var vacio=0
    var nom=document.getElementById("nombre").value;
    var apell=document.getElementById("apellido").value;
    var identi=document.getElementById("identificacion").value;
    var user=document.getElementById("usuario").value;
    var email=document.getElementById("correo").value;
    var stado=0;
    var sexo=0;
    var tipo=0;

    var combo = document.getElementById("estado");
    var seleccionado = combo.options[combo.selectedIndex].text;

    var combo2 = document.getElementById("genero");
    var seleccionado2 = combo2.options[combo2.selectedIndex].text;

    var combo3 = document.getElementById("tipo_usuario");
    var seleccionado3 = combo3.options[combo3.selectedIndex].text;
    //alert(seleccionado);

    //genero
    if(seleccionado2=="Masculino"||seleccionado2=="Femenino"){
    //alert("se selecciono activo");
    sexo=1;
    }else{
        alert("Debe seleccionar un genero valido");
    }
    //estado
    if(seleccionado=="Activo"||seleccionado=="Inactivo"){
        //alert("se selecciono activo");
        stado=1;
        }else{
            alert("Debe seleccionar un estado valido");
        }
        //tipo cliente

        if(seleccionado3=="Administrador"||seleccionado3=="Superadministrador"){
            //alert("se selecciono activo");
            tipo=1;
            }else{
                alert("Debe seleccionar un tipo de cliente valido");
            }


        //vacio
    if (nom.length == 0 || apell.length == 0||identi.length == 0||user.length == 0||email.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }


   /* if(vacio==1&&stado==1&&sexo==1&&tipo==1){
    window.alert("El usuario ha sido agregado exitosamente");
    window.close();
    }*/

}

function alerta12(){
    var ele=document.getElementsByName("terminos");
    var cumple=0;
    if(terminos.checked){
        cumple=1;
         
    }else{
        alert("Debe seleccionar un comentario a eliminar");
        
    }
    if(cumple==1){
    alert("Comentario eliminado con exito");
    window.open("comentarios_productos_usuario2.html","_self");
}
}

function alerta13(){
    var ele=document.getElementsByName("terminos");
    var cumple=0;
    if(terminos.checked){
        cumple=1;
         
    }else{
        alert("Debe seleccionar un comentario a eliminar");
        
    }
    if(cumple==1){
    alert("Comentario eliminado con exito");
    window.open("comentarios_productos_usuario1.html","_self");
}
}

function alerta14(){
    var ele=document.getElementsByName("terminos");
    var cumple=0;
    if(terminos.checked){
        cumple=1;
         
    }else{
        alert("Debe seleccionar un comentario a eliminar");
        
    }
    if(cumple==1){
    alert("Comentario eliminado con exito");
    window.open("comentarios_productos2.html","_self");
}
}


//solo numeros
function soloNumeros(event) {
    if(event.charCode >= 48 && event.charCode <= 57){
      return true;
     }
     return false;        
}

//solo lentras
function soloLetras(e) {
    var key = e.keyCode || e.which,
      tecla = String.fromCharCode(key).toLowerCase(),
      letras = " áéíóúabcdefghijklmnñopqrstuvwxyz",
      especiales = [8, 37, 39, 46],
      tecla_especial = false;

    for (var i in especiales) {
      if (key == especiales[i]) {
        tecla_especial = true;
        break;
      }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
      return false;
    }
  }
  
  //VAlidar Claves

  function validarPasswd() {
   
    var p1 = document.getElementById("passwd").value;
    var p2 = document.getElementById("passwd2").value;
    
    var espacios = false;
    var cont = 0;
    var cumple=0;
    var pass=0;
    var vacio=0;

    var nom=document.getElementById("nombre2").value;
    var apell=document.getElementById("apellido2").value;
    var ced=document.getElementById("cedula2").value;
    var dir=document.getElementById("direccion2").value;
    var user=document.getElementById("usuario2").value;
    var ele=document.getElementsByName("terminos");

    // Este bucle recorre la cadena para comprobar
    // que no todo son espacios
      while (!espacios && (cont < p1.length)) {
          if (p1.charAt(cont) == " ")
              espacios = true;
          cont++;
      }
     
    if (espacios) {
       
     alert ("La contraseña no puede contener espacios en blanco");
     
     return false;
    }
     
    if (p1.length == 0 || p2.length == 0||nom.length == 0||apell.length == 0||ced.length == 0||dir.length == 0||user.length == 0) {
     alert("Los campos no pueden quedar vacios");
     return false;
    }else{
        vacio=1;
    }
    
    

    if (p1 != p2) {
     alert("Las passwords deben de coincidir");
     return false;
     
    } else{
        pass=1;
    }

    if(terminos.checked){
        cumple=1;
         
    }else{
        alert("No acepto las politicas de privacidad");
        
    }
   
   /* if(pass==1&&vacio==1&&cumple==1){
        alert("Todo esta correcto-usuario registrado");
        window.open("pagina2","_self");
        
    }*/

}

   //inicio de sesion

   function inicio_sesion() {
    var user=document.getElementById("username").value;
    var contra=document.getElementById("password").value;
    var vacio=0;
    var cliente='cliente2';
    var administrador="administrador2";
    var superAdminstrador="superAdministrador2"
    var password=12345;

    if (user.length == 0 || contra.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }
       
    /*if(((user=='cliente2')&&contra==password)){
        alert("usuario registrado");
        window.open("pagina6","_self");
        return true;

    }else{

        if(((user=='administrador2')&&contra==password)){
            alert("usuario registrado");
            window.open("administrador_usuarios1.html","_self");
            return true;
    
        } else{
            if(((user=='superAdministrador2')&&contra==password)){
                alert("usuario registrado");
                window.open("superAdministrador_usuarios1.html","_self");
                return true;
        
            }else{
                alert("usuario no registrado");
                window.open("iniciar_sesion.html","_self");
                return false;
            }
        }

    }*/


   }

   //Modificar perfil

   function modificarPerfil(){

    var espacios = false;
    var cont = 0;
    var vacio=0;
    var nom=document.getElementById("nombre2").value;
    var apell=document.getElementById("apellido").value;
    var ced=document.getElementById("cedula2").value;
    var dir=document.getElementById("direccion").value;
    var user=document.getElementById("usuario").value;

    if (nom.length == 0||apell.length == 0||ced.length == 0||dir.length == 0||user.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }
    
       /*if(vacio==1){
        alert("Datos del usuario modificados");
       }*/
    
   }

   //Crear lista de deseos
   function crear(){
    var lista=document.getElementById("crearLista").value;
    var vacio=0;

    if (lista.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
       }else{
           vacio=1;
       }
   
   /*if(vacio==1){
    alert("Lista creada");
    window.open("lista_deseos3.html","_self");
   }*/
   
    }

    function crear2(){
        var lista=document.getElementById("nombre2").value;
        var vacio=0;
    
        if (lista.length == 0) {
            alert("Los campos no pueden quedar vacios");
            return false;
           }else{
               vacio=1;
           }
        }
 

    function crear50(){
    var lista=document.getElementById("nombre").value;
    var vacio=0;

    if (lista.length == 0) {
        alert("Los campos no pueden quedar vacios");
        return false;
        }else{
            vacio=1;
        }
       
       /*if(vacio==1){
        alert("Lista creada");
        window.open("lista_deseos3.html","_self");
       }*/
       
        }



//modificar nombre de la lista
function modificarLista(){

    var cumple=1;
    if(selLista1.checked){
        cumple=1;
         
    }else{
        alert("Seleccione una lista");
        
    }

    if(cumple==1){
        window.open("lista_deseos7.html","_self");
    }
    
}

//cambio de password
function cambioPasswd(){
    
    var espacios = false;
    var cont = 0;
    var vacio=0;
    var noIgual=0;
    var pass=0;
    var espaciado=0;
    var actual=document.getElementById("actual_pas").value;
    var nueva=document.getElementById("nueva_pas").value;
    var confirmar=document.getElementById("confirmar_pas").value;

    while (!espacios && (cont < nueva.length)) {
        if (nueva.charAt(cont) == " ")
            espacios = true;
        cont++;
    }
   
  if (espacios) {
     
   alert ("La contraseña no puede contener espacios en blanco");
   window.open("cambiar_contrasena.html","_self");
   
   return false;
  }else{
      espaciado=1;
  }





    if((actual.length == 0)||(nueva.length == 0)||(confirmar.length == 0)){
        alert("Los campos no pueden quedar vacios");
        return false;
    }else{
        vacio=1;
    }

    if(nueva==actual){
        alert("utilice una contraseña diferente");
        window.open("cambiar_contrasena.html","_self");

    }else{
        noIgual=1;
    }

    if (nueva != confirmar) {
        alert("Las passwords deben de coincidir");
        window.open("cambiar_contrasena.html","_self");
        return false;
        
       } else{
           pass=1;
       }

       /*if(espaciado==1&&pass==1&&noIgual==1&&vacio==1){
        alert("Contraseña cambiada con exito");
        window.open("iniciar_sesion.html","_self");

       }*/

}