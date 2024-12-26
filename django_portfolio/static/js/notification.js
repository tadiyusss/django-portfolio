function notify_info(message){
    $("#notification-container").append(`<div class="mb-3 w-full bg-blue-800 text-white p-3 rounded"> <p>${message}</p> </div>`)
    setTimeout(function(){
        $("#notification-container").children().first().fadeOut(1000, function(){
            $(this).remove();
        });
    }, 3000);
}

function notify_error(message){
    $("#notification-container").append(`<div class="mb-3 w-full bg-red-800 text-white p-3 rounded"> <p>${message}</p> </div>`)
    setTimeout(function(){
        $("#notification-container").children().first().fadeOut(1000, function(){
            $(this).remove();
        });
    }, 3000);
}

function notify_success(message){
    $("#notification-container").append(`<div class="mb-3 w-full bg-green-800 text-white p-3 rounded"> <p>${message}</p> </div>`)
    setTimeout(function(){
        $("#notification-container").children().first().fadeOut(1000, function(){
            $(this).remove();
        });
    }, 3000);
}

function notify_warning(message){
    $("#notification-container").append(`<div class="mb-3 w-full bg-yellow-800 text-white p-3 rounded"> <p>${message}</p> </div>`)
    setTimeout(function(){
        $("#notification-container").children().first().fadeOut(1000, function(){
            $(this).remove();
        });
    }, 3000);
}