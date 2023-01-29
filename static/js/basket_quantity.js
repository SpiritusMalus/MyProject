$(document).ready(function () {
    const bt_minus = document.querySelectorAll('#bt_minus')
    bt_minus.forEach(el => el.addEventListener('click', function (event) {
        event.preventDefault();
        const quantity_minus = el.dataset.quantity_minus;
        const product_id = el.dataset.product_id;
        const product_price = el.dataset.price;
        console.log('OFEOFEFEK')
        const data = {};
        data.product_id = product_id;
        data.quantity_minus = quantity_minus;
        data.product_price = product_price;
        const csrf_token = $('#form_quantity [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;

        const url = 'basket_quantity/';

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
