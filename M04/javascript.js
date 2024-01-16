document.getElementById('scrollLeft').addEventListener('click', function() {
    document.querySelector('.scrolling-wrapper').scrollBy({
        top: 0,
        left: -200, // Cambia este valor según el ancho de tus tarjetas de imagen
        behavior: 'smooth'
    });
});

document.getElementById('scrollRight').addEventListener('click', function() {
    document.querySelector('.scrolling-wrapper').scrollBy({
        top: 0,
        left: 200, // Cambia este valor según el ancho de tus tarjetas de imagen
        behavior: 'smooth'
    });
});