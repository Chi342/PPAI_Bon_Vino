// Obtener el modal
var modal = document.getElementById("modalConfirmacion");

// Obtener el botón que abre el modal
var btn = document.querySelector("button[type='submit']");

// Obtener el elemento <span> que cierra el modal
var span = document.getElementsByClassName("close")[0];

// Obtener botones de cancelar y confirmar
var cancelar = document.getElementById("cancelar");
var confirmar = document.getElementById("confirmar");

// Cuando el usuario hace clic en el botón, abrir el modal
btn.onclick = function(e) {
  e.preventDefault(); // Prevenir la acción por defecto del formulario
  modal.style.display = "block";
}

// Cuando el usuario hace clic en <span> (x), cerrar el modal
span.onclick = function() {
  modal.style.display = "none";
}

// Cuando el usuario hace clic en "Cancelar", cerrar el modal
cancelar.onclick = function() {
  modal.style.display = "none";
}

// Si el usuario hace clic en "Confirmar", proceder con la acción
confirmar.onclick = function() {
  // Aquí puedes agregar la lógica para generar el reporte
  modal.style.display = "none";
  console.log("Reporte generado");
}

// Cuando el usuario hace clic fuera del modal, cerrarlo
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}