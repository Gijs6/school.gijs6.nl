(function () {
    "use strict";

    var MAX_LENGTH = 40;

    var path = document.querySelector(".error__path");
    if (!path) return;

    var trimmed = location.pathname.replace(/\/+$/, "");
    if (!trimmed) return;

    function fit() {
        var keep = Math.min(trimmed.length, MAX_LENGTH - 1);
        path.textContent = trimmed.length > MAX_LENGTH ? "…" + trimmed.slice(-keep) : trimmed;

        while (path.scrollWidth > path.clientWidth && keep > 1) {
            keep -= 1;
            path.textContent = "…" + trimmed.slice(-keep);
        }
    }

    path.hidden = false;
    fit();
    window.addEventListener("resize", fit);
    if (document.fonts) document.fonts.ready.then(fit);
})();
