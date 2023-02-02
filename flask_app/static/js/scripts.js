$(document).ready(()=>{
    $('.add-task').on('click', ()=>{
        $('#task-form').slideDown(200);
    });
    $('#close-task-from').on('click', ()=>{
        $('#task-form').slideUp(200);
    });
})