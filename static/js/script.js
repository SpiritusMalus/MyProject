$(document).ready(function () {
    const submit_btn = document.querySelectorAll('#submit_btn')
    submit_btn.forEach(el => el.addEventListener('click', function (event) {
        event.preventDefault();
        const product_id = el.dataset.product_id;
        const product_name = el.dataset.name;
        const product_price = el.dataset.price;
        const user_id = el.dataset.user_id

        const data = {};
        data.product_id = product_id;
        data.product_name = product_name;
        data.product_price = product_price;
        data.user_id = user_id;

        const csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;

        const url = 'basket/basket_adding/';

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

