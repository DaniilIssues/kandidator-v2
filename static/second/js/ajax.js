let btn = document.querySelectorAll('.td_ajax');

for (let i = 0; i < btn.length; i++) {
    let url_ = btn[i].querySelector('.url_ajax').getAttribute('href');
    btn[i].querySelector('.act_ajax').onclick = function () {
        $.ajax({
            url: url_,
            type:'get',
            success: function (form) {
                $('.modal-body').html('').append(form);
            },
            failure: function (form) {
                console.log('errorrrrr');
            }
        });

    };
}
