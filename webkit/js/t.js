// Completes the full-name control and
// shows the submit button
function completeAndReturnName() {
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var full = fname + ' ' + lname;

    document.getElementById('fullname').value = full;
    document.getElementById('submit-btn').style.display = 'block';

    return full;
}
