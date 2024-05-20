// $('#contactForm').submit(function (e) {
//     e.preventDefault();
//     var form = $(this);
//     var url = form.attr('action');

//     $.ajax({
//         type: "POST",
//         url: url,
//         data: form.serialize(),
//         success: function (data) {
//             console.log('API response:', data);
//         },
//         error: function (xhr, status, error) {
//             console.error('Error:', status, error);
//         }
//     });
// });


// (async function () {
//     const url = 'http://127.0.0.1:8000/api/v1/send-message/';
//     const res = await fetch(url, { method: 'POST' });
// })();
