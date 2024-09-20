var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
return new bootstrap.Tooltip(tooltipTriggerEl)
})

const swalWithBootstrapButtons = Swal.mixin({
customClass: {
    confirmButton: "btn btn-success",
    cancelButton: "btn btn-danger"
},
buttonsStyling: false
});

var table = new DataTable('#mdatatable', {
    language: {
        url: "/static/adminassets/fonts/es-MX.json",
    },
});

tinymce.init({
    selector: 'textarea#descri',
    height: 400,
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
    }
});

function deleteAlert(ev) {
    const address = ev.getAttribute('data-address')

    swalWithBootstrapButtons.fire({
        title: "Esta seguro?",
        text: "No podra revertir esta acción!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, eliminar!",
        cancelButtonText: "No, cancelar!",
        reverseButtons: true
        }).then((result) => {
        if (result.isConfirmed) {

            location.href=address

        }
    });
    
}