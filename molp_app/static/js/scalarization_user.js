var user_socket = new WebSocket('ws://' + window.location.host + '/ws/user_scalarizations/')

user_socket.onmessage = function(event){
    var tasks = event.data;
    tasks = JSON.parse(tasks)

    for (let i = 0; i < tasks.length; i++) {
        problem_id = tasks[i].problem_pk
        status = tasks[i].task_status

        var a = $('#process-raw-data-user-'+problem_id);
        var dwnldbtn = $('#download-ch-user-'+problem_id);

        a.html(status);

        if (status != 'SUCCESS') {
            dwnldbtn.css('visibility', 'hidden');
            a.html(status);
        }
        else if (status == 'SUCCESS') {
            dwnldbtn.css('visibility', 'visible');
            a.html(status);
        }
    }
}