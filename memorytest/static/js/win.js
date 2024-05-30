document.addEventListener('DOMContentLoaded', () => {
    const confettiContainer = document.querySelector('.confetti');

    const createConfettiPiece = () => {
        const confettiPiece = document.createElement('div');
        confettiPiece.classList.add('confetti-piece');
        confettiPiece.style.left = Math.random() * 100 + 'vw';
        confettiPiece.style.top = 0;
        confettiPiece.style.animationDuration = (Math.random() * 2 + 3) + 's';
        confettiPiece.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
        confettiContainer.appendChild(confettiPiece);

        setTimeout(() => {
            confettiPiece.remove();
        }, 5000);
    };

    for (let i = 0; i < 100; i++) {
        setTimeout(createConfettiPiece, Math.random() * 5000);
    }
});