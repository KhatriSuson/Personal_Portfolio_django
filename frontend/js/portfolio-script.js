// Home page JavaScript
 // Background animation (stars, moon, programming icons)
const canvas = document.createElement('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
document.getElementById('background-animation').appendChild(canvas);

const ctx = canvas.getContext('2d');

let objects = [];
function init() {
    for (let i = 0; i < 100; i++) {
        objects.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 3,
            dx: Math.random() * 0.5 - 0.25,
            dy: Math.random() * 0.5 - 0.25,
        });
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    objects.forEach((obj) => {
        ctx.beginPath();
        ctx.arc(obj.x, obj.y, obj.size, 0, Math.PI * 2);
        ctx.fillStyle = '#fff';
        ctx.fill();
        obj.x += obj.dx;
        obj.y += obj.dy;

        if (obj.x < 0 || obj.x > canvas.width) obj.dx = -obj.dx;
        if (obj.y < 0 || obj.y > canvas.height) obj.dy = -obj.dy;
    });
    requestAnimationFrame(animate);
}

init();
animate();


