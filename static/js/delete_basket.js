$(document).ready(function () {
    const delete_btn = document.querySelectorAll('#delete_btn')
    delete_btn.forEach(el => el.addEventListener('click', function (event) {
        event.preventDefault();
        const product_id = el.dataset.product_id;
        const data = {};
        data.product_id = product_id;
        const csrf_token = $('#form_delete_product [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;

        const url = 'basket_remove/';

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK');

            },
            error: function () {
                console.log('ERROR')
            }

        });
    }));
});


