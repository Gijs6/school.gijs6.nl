(function () {
    "use strict";

    var toc = document.querySelector(".summary__toc");
    if (!toc) return;

    var details = toc.querySelector(".summary__toc-details");
    var scroller = toc.querySelector(".summary__toc-scroll") || toc;
    var sidebar = window.matchMedia("(min-width: 1200px)");

    var headings = [];
    var linkFor = new Map();

    Array.prototype.forEach.call(toc.querySelectorAll(".toc a[href^='#']"), function (link) {
        var heading = document.getElementById(decodeURIComponent(link.hash.slice(1)));
        if (!heading) return;
        headings.push(heading);
        linkFor.set(heading, link);
    });

    var current = null;

    function clearCurrent() {
        if (!current) return;
        linkFor.get(current).removeAttribute("aria-current");
        current = null;
    }

    function keepVisible(link) {
        var box = scroller.getBoundingClientRect();
        var rect = link.getBoundingClientRect();
        if (rect.top < box.top) {
            scroller.scrollTop -= box.top - rect.top + 8;
        } else if (rect.bottom > box.bottom) {
            scroller.scrollTop += rect.bottom - box.bottom + 8;
        }
    }

    function update() {
        if (!sidebar.matches || !headings.length) return;

        var active = headings[0];

        for (var i = 0; i < headings.length; i++) {
            if (headings[i].getBoundingClientRect().top - 100 > 0) break;
            active = headings[i];
        }

        if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) {
            active = headings[headings.length - 1];
        }

        if (active === current) return;

        if (current) linkFor.get(current).removeAttribute("aria-current");
        current = active;

        var link = linkFor.get(current);
        link.setAttribute("aria-current", "true");
        keepVisible(link);
    }

    function syncLayout() {
        if (details) details.open = sidebar.matches;
        if (sidebar.matches) {
            update();
        } else {
            clearCurrent();
        }
    }

    syncLayout();
    if (sidebar.addEventListener) sidebar.addEventListener("change", syncLayout);

    var ticking = false;

    function onScroll() {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(function () {
            ticking = false;
            update();
        });
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });

    window.addEventListener("load", update);
})();
