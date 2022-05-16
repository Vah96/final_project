window.onload = (event) => {
    cancel_button = document.getElementById('cancel_add_car')
    if (cancel_button) {
        document.getElementById('cancel_add_car').onclick = function () {
            // alert('Click has been done!!!')
            window.location = '/'
        }
    }

};