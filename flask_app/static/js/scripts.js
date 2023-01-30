$(document).ready(()=>{
    $('.add-task').on('click', ()=>{
        $('#task-form').show();
    });
    
    $('#close-task-from').on('click', ()=>{
        $('#task-form').hide();
    });
})