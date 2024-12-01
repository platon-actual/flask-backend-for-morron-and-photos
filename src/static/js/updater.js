// Ramiro Iván Ríos 2024-12-01
// Copyright 2024.

function reload_page() {
    alert("Actualizando página...");
    location.reload();
}

window.onload = function(evt) {
    let TIMEOUT_ = 60 * 5 * 1000;
    window.setTimeout( reload_page, TIMEOUT_)
}