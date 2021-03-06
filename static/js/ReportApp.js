// Selectors
const formEvent = document.getElementById('btn-alert');
const reportName = document.getElementById('r-name');
const reportRv = document.getElementById('rv');
const reportBs = document.getElementById('bs');
const reportMin = document.getElementById('min');
const text = document.getElementById('error-text');

formEvent.addEventListener('click', function (event) {
    let errorMessages = [];
    if (reportName.value === '' || reportName.value == null) {
        errorMessages.push('Hey, You Forgot To Create A Report Name');
        text.className += "alert alert-danger";
    }

    if (reportMin.value > 60) {
        errorMessages.push(reportMin.value + ' Minutes Is higher Than 1 Hour! Just Add To Your Hours');
        text.className += "alert alert-danger";
    }

    if (reportBs.value > reportRv.value) {
        errorMessages.push('Sorry, You Cant Have ' + reportBs.value + ' Bible Studies And Just ' + reportRv.value + ' Return Visits');
        text.className += "alert alert-danger";
    }

    if (errorMessages.length > 0) {
        event.preventDefault();
        text.innerHTML = errorMessages.join(', ');
    }
});


// functions