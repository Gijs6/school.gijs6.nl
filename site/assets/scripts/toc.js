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

    function fit() {
        var gap = parseFloat(window.getComputedStyle(toc).top) || 0;
        var tocViewportTop = toc.getBoundingClientRect().top;
        var headingHeight = scroller.getBoundingClientRect().top - tocViewportTop;
        var availableHeight = window.innerHeight - Math.max(tocViewportTop, gap) - headingHeight - gap;
        scroller.style.maxHeight = Math.max(availableHeight, 128) + "px";
    }

    function keepVisible(link) {
        var box = scroller.getBoundingClientRect();
        var rect = link.getBoundingClientRect();
        var edgeRoom = Math.min(rect.height * 2.5, box.height / 3);
        if (rect.top < box.top + edgeRoom) {
            scroller.scrollTop -= box.top + edgeRoom - rect.top;
        } else if (rect.bottom > box.bottom - edgeRoom) {
            scroller.scrollTop += rect.bottom + edgeRoom - box.bottom;
        }
    }

    function update() {
        if (!sidebar.matches) return;

        fit();

        if (!headings.length) return;

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
            scroller.style.maxHeight = "";
            clearCurrent();
        }
    }

    syncLayout();
    if (sidebar.addEventListener) sidebar.addEventListener("change", syncLayout);

    var updateQueued = false;

    function onScroll() {
        if (updateQueued) return;
        updateQueued = true;
        window.requestAnimationFrame(function () {
            updateQueued = false;
            update();
        });
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });

    window.addEventListener("load", update);
})();
