(function () {
    "use strict";

    var RETRY_MS = 500;

    var connectedBefore = false;

    function connect() {
        var socket = new WebSocket("ws://" + location.host + "/__livereload");

        socket.onopen = function () {
            if (connectedBefore) location.reload();
            connectedBefore = true;
        };
        socket.onmessage = function () {
            location.reload();
        };
        socket.onclose = function () {
            setTimeout(connect, RETRY_MS);
        };
    }

    connect();
})();
