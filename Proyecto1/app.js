$(document).ready(function() {
    $("#password-form").submit(function(event) {
      event.preventDefault();
  
      var formData = $(this).serialize();
      $.ajax({
        type: "POST",
        url: "/generar_contraseña",
        data: formData,
        success: function(response) {
          $("#password").text(response);
          $("#password-result").show();
        },
        error: function() {
          alert("Error al generar la contraseña. Asegúrate de que el servidor Flask esté en ejecución.");
        }
      });
    });
  });
  