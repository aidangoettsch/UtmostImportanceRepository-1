// Okay Copilot, create something interesting.

var copilot = {};

copilot.init = function() {
    copilot.canvas = document.getElementById("copilot");
    copilot.context = copilot.canvas.getContext("2d");
    copilot.canvas.width = window.innerWidth;
    copilot.canvas.height = window.innerHeight;
    copilot.canvas.style.backgroundColor = "black";
    copilot.canvas.style.border = "1px solid white";
    copilot.canvas.style.margin = "0px";
    copilot.canvas.style.padding = "0px";
    copilot.canvas.style.position = "absolute";
    copilot.canvas.style.top = "0px";
    copilot.canvas.style.left = "0px";
    copilot.canvas.style.zIndex = "0";
    copilot.canvas.style.cursor = "none";
    copilot.canvas.style.pointerEvents = "none";
    copilot.canvas.style.userSelect = "none";
    copilot.canvas.style.webkitUserSelect = "none";
    copilot.canvas.style.mozUserSelect = "none";
    copilot.canvas.style.msUserSelect = "none";
    copilot.canvas.style.oUserSelect = "none";
    copilot.canvas.style.webkitTouchCallout = "none";
    copilot.canvas.style.webkitTapHighlightColor = "rgba(0,0,0,0)";
    copilot.canvas.style.touchAction = "none";
    copilot.canvas.style.MozTouchAction = "none";
    copilot.canvas.style.KhtmlUserSelect = "none";
    copilot.canvas.style.MozUserSelect = "none";
    copilot.canvas.style.msUserSelect = "none";
    copilot.canvas.style.oUserSelect = "none";
    copilot.canvas.style.userDrag = "none";
    copilot.canvas.style.webkitUserDrag = "none";
    copilot.canvas.style.MozUserDrag = "none";
    copilot.canvas.style.msUserDrag = "none";
    copilot.canvas.style.oUserDrag = "none";
    copilot.canvas.style.userSelect = "none";
    copilot.canvas.style.webkitUserSelect = "none";
    copilot.canvas.style.MozUserSelect = "none";
    copilot.canvas.style.msUserSelect = "none";
    copilot.canvas.style.oUserSelect = "none";
};

// Let's get another one:
copilot.create = function() {
    copilot.init();
    copilot.canvas.addEventListener("mousedown", copilot.mousedown, false);
    copilot.canvas.addEventListener("mouseup", copilot.mouseup, false);
    copilot.canvas.addEventListener("mousemove", copilot.mousemove, false);
    copilot.canvas.addEventListener("touchstart", copilot.touchstart, false);
    copilot.canvas.addEventListener("touchmove", copilot.touchmove, false);
    copilot.canvas.addEventListener("touchend", copilot.touchend, false);
    copilot.canvas.addEventListener("touchcancel", copilot.touchcancel, false);
    copilot.canvas.addEventListener("keydown", copilot.keydown, false);
    copilot.canvas.addEventListener("keyup", copilot.keyup, false);
};

copilot.mousedown = function(e) {
    copilot.mouseDown = true;
    copilot.mouseX = e.pageX;
    copilot.mouseY = e.pageY;
    copilot.canvas.style.cursor = "none";
    copilot.canvas.style.pointerEvents = "none";
    copilot.canvas.style.userSelect = "none";
    copilot.canvas.style.webkitUserSelect = "none";
    copilot.canvas.style.mozUserSelect = "none";
    copilot.canvas.style.msUserSelect = "none";
    copilot.canvas.style.oUserSelect = "none";
    copilot.canvas.style.webkitTouchCallout = "none";
    copilot.canvas.style.webkitTapHighlightColor = "rgba(0,0,0,0)";
    copilot.canvas.style.touchAction = "none";
    copilot.canvas.style.MozTouchAction = "none";
    copilot.canvas.style.KhtmlUserSelect = "none";
    copilot.canvas.style.MozUserSelect = "none";
    copilot.canvas.style.msUserSelect = "none";
}

// Thank you Copilot, very cool.