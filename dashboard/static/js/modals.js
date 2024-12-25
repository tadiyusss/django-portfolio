$(document).ready(function() {

    $('#createLanguageBtn').click(function(){
        $('#createLanguageModal').removeClass('hidden');
        $('#sidebarOverlay').removeClass('hidden');
    });

    $('#createTestimonialsBtn').click(function(){
        $('#createTestimonialModal').removeClass('hidden');
        $('#sidebarOverlay').removeClass('hidden');
    })



    $('#closeModal, #closeModalBottom, #closeTestimonialModal, #closeTestimonialModalBottom').click(function() {
        $('#sidebarOverlay').addClass('hidden');
        $('#createLanguageModal').addClass('hidden');
        $('#createTestimonialModal').addClass('hidden');
    });

    $('#sidebarOverlay').click(function() {
        $('#sidebarOverlay').addClass('hidden');
        $('#createLanguageModal').addClass('hidden');
        $('#createTestimonialModal').addClass('hidden');
    });
});