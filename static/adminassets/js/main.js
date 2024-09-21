var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl)
})

const Toast = Swal.mixin({
    toast: true,
    position: "bottom-end",
    showConfirmButton: false,
    timer: 6000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.onmouseenter = Swal.stopTimer;
      toast.onmouseleave = Swal.resumeTimer;
    }
  });

const swalWithBootstrapButtons = Swal.mixin({
customClass: {
    confirmButton: "btn btn-success ms-2",
    cancelButton: "btn btn-danger me-2"
},
buttonsStyling: false
});

var table = new DataTable('#mdatatable', {
    language: {
        url: "/static/adminassets/fonts/es-MX.json",
    },
    columnDefs: [
        { orderable: false, targets: -1 },
        {
            orderable: false,
            render: DataTable.render.select(),
            targets: 0
        }
    ],
    select: {
        style: 'multi',
        selector: 'td:first-child',
        headerCheckbox: false,
    }
});

tinymce.init({
    selector: 'textarea#descri',
    language: 'es',
    height: 350,
    skin: 'oxide',
    menubar: false,
    plugins: [
        'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
        'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
        'insertdatetime', 'media', 'table', 'help', 'wordcount'
    ],
    toolbar: 'undo redo | blocks | ' +
    'bold italic backcolor | alignleft aligncenter ' +
    'alignright alignjustify | bullist numlist outdent indent | ' +
    'removeformat | help',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }',
    setup: (editor) => {
        editor.on('init', () => {
        editor.getContainer().style.transition='border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out';
        });
        editor.on('focus', () => {
        editor.getContainer().style.boxShadow='0 0 0 .2rem rgba(0, 123, 255, .25)';
        editor.getContainer().style.borderColor='#80bdff';
        });
        editor.on('blur', () => {
        editor.getContainer().style.boxShadow='';
        editor.getContainer().style.borderColor='';
        });
    },
});

function actualizarContenido(nuevoContenido) {
    tinymce.get('descri').setContent(nuevoContenido);
}

function deleteAlert(ev) {
    const address = ev.getAttribute('data-address')

    swalWithBootstrapButtons.fire({
        title: "¿Esta seguro?",
        text: "No podrá revertir esta acción",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar",
        reverseButtons: true
        }).then((result) => {
        if (result.isConfirmed) {
            location.href=address
        }
    });
    
}

function deleteAll(ev) {
    const address = ev.getAttribute('data-address')
    const csrf = ev.getAttribute('data-csrf')

    const dataTable = table.rows({ selected: true })

    let data = []

    for (const row of dataTable['0']) {
      data.push(Number(table.rows().data()[row][0]))
    }

    if ( Array. isArray(data) && data.length === 0 ){
        Toast.fire({
            icon: 'error',
            title: 'No ha marcado ningún registro',
        });
        return
    }

    swalWithBootstrapButtons.fire({
        title: "¿Esta seguro?",
        text: "No podrá revertir esta acción",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar",
        reverseButtons: true
        }).then((result) => {
        if (result.isConfirmed) {
            fetch(address, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf },
                body: JSON.stringify(data)
           })
           .then(response => {
               console.log(response)
           })
           .catch(error => {
               console.log(error)
           })
           location.href=address
        }
    });
    
  }