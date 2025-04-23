const canvas = document.createElement('canvas');
canvas.width = 600;
canvas.height = 200;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');
ctx.font = '28px Arial';
const text = 'Online Avto School';
let particles = [];

for (let i = 0; i < text.length; i++) {
    particles.push({
        x: 50 + i * 20,
        y: 100,
        char: text[i],
        vx: (Math.random() - 0.5) * 3,
        vy: (Math.random() - 0.5) * 3,
        color: `hsl(${Math.random() * 360}, 70%, 50%)`
    });
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
        ctx.fillStyle = p.color;
        ctx.fillText(p.char, p.x, p.y);
    });
    requestAnimationFrame(animate);
}
animate();