// Instance the tour
var tour = new Tour({
    template: "<div class='popover tour' ><div class='arrow'></div><h3 class='popover-title bg-primary text-white'></h3><div class='popover-content'></div><div class='popover-navigation'><button class='btn btn-primary' data-role='prev'>« Anterior</button><span data-role='separator'>|</span><button class='btn btn-primary' data-role='next'>Siguiente »</button></div><button class='btn btn-primary' data-role='end'>Finalizar</button></div>",
    steps: [
    {
      element: "#button_agendar_cita",
      title: "Agendar una cita",
      content: "Presione el botón para llenar el formulario de su cita !"
    },
    {
      element: "#obtener_ayuda",
      title: "Obtener asesoramiento",
      content: "Presione el botón para ver nuestros servicios"
    }
  ]});
  
  // Initialize the tour
  tour.init();
  
  // Start the tour
  tour.start();