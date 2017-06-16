$(document).ready(function () {
    //retrai o menu somente em telas largas
    if (window.matchMedia('(min-width: 992px)').matches) {
        $('#menu_toggle').click();
    }
    $(window).on('hashchange', function () {
        $("#conteudo").html("");
        if (window.location.hash == "#mqtt") {
            $("#conteudo").load("componentes/mqtt.html", function(){
                carregado();
            });
        }
    });
});

window.onload = function () {
    history.pushState('', document.title, window.location.pathname);
}