function initPageTrigger() {
    $('#menu-mqtt').on('click', function () {
        $("#conteudo").html("");
        $("#conteudo").load("componentes/mqtt.html");

        if (window.matchMedia('(max-width: 992px)').matches) {
            $('#menu_toggle').click();
        }
    });

    $('#menu-home').on('click', function () {
        $("#conteudo").html("");
    });
}