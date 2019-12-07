$(document).ready(function () {

    $('#noise-table').DataTable({
        responsive: true,
        ajax: {
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            url: '/noise-log/get-noise-logs/',
            method: 'GET',
            dataSrc: 'logs',
        },
        columns: [
            {
                data: 'timestamp',
                render: function (data) {
                    return new Date(data);
                }
            },
            {data: 'decibel'}
        ]
    });

    setInterval(function () {
        $('#noise-table').DataTable().ajax.reload();
    }, 10000);
});