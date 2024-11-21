
<script>
    $(document).ready(function () {
        // Check if the dropdown-toggle element exists and initialize the dropdown
        if ($('.dropdown-toggle').length) {
            $('.dropdown-toggle').dropdown();
        }
    });

    $(function(){
    $('#sidebarCollapse').on('click',function(){
        $('#sidebar, #content').toggleClass('active');
    });
});

let slideIndex = 1;
showSlides(slideIndex);

function openModal() {
    document.getElementById('myModal').style.display = "flex";
}

function closeModal() {
    document.getElementById('myModal').style.display = "none";
}

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    const slides = document.getElementsByClassName("mySlides");

    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex - 1].style.display = "block";
}

</script>