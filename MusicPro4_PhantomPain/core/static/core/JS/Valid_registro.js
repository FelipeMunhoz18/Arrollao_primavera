const nombre = document.getElementById("nombre");
const apellidos = document.getElementById("apellido");
const correo = document.getElementById("email");
const celular = document.getElementById("celular");
const contrasenia = document.getElementById("password");
const contrasenia2 = document.getElementById("repeatPassword");
const terminosYcondiciones = document.getElementById("terminos");
const form = document.getElementById("form");
const listInputs = document.querySelectorAll(".form-input");
const msj = document.getElementById("mensajeError")

form.addEventListener("submit",e =>{
    let msjMostrar = "";
    let envioCorrecto = false;

    if(nombre.value.length <4 || nombre.value.length > 20){
        msjMostrar += "The name is too long<br>";
        envioCorrecto = true;
    }

    if(apellidos.value.length <4 || apellidos.value.length > 20){
        msjMostrar += "The nickname is too long<br>";
        envioCorrecto = true;
    }

    if(correo.value.length <4 || correo.value.length > 25){
        msjMostrar += "The E-mail is not valid<br>";
        envioCorrecto = true;
    }

    if(celular.value.length !=9){
        msjMostrar += "Phone is not valid<br>";
        envioCorrecto = true;
    }

    if(contrasenia.value.length <6 || contrasenia.value.length > 20){
        msjMostrar += "Nickname is not valid<br>";
        envioCorrecto = true;
    }

    var letraNombre = contrasenia.value.charAt(0);
    if (!esMayus(letraNombre)){
        msjMostrar += "Password needs an uppercase letter<br>";
        envioCorrecto = false;
    }

    if (contrasenia2.value != contrasenia.value) {
        msjMostrar += "Passwords do not match<br>";
        condicion = false;
    }

    if (!terminosYcondiciones.checked) {
        msjMostrar += "Accept the terms and conditions<br>";
        condicion = false;
    } else {
        msjMostrar += "";
    }
    
    if(envioCorrecto){
        msj.innerHTML = msjMostrar;
        e.preventDefault();
    }
    else{
        msj.innerHTML = "Success, the form has been sent";
    }
    //return condicion;
});

function esMayus (letra){
    return letra == letra.toUpperCase();
  };


