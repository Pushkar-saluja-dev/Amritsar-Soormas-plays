document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Nav Stopwatch Logic ---
    const stopwatchEl = document.getElementById('nav-stopwatch');
    let startTime = Date.now();
    
    function updateStopwatch() {
        const elapsed = Date.now() - startTime;
        const minutes = Math.floor(elapsed / 60000);
        const seconds = Math.floor((elapsed % 60000) / 1000);
        const centiseconds = Math.floor((elapsed % 1000) / 10);
        
        const m = minutes.toString().padStart(2, '0');
        const s = seconds.toString().padStart(2, '0');
        const c = centiseconds.toString().padStart(2, '0');
        
        stopwatchEl.textContent = `${m}:${s}.${c}`;
        requestAnimationFrame(updateStopwatch);
    }
    requestAnimationFrame(updateStopwatch);


    // --- 2. Scrolling Pixelometer Logic ---
    const speedValueEl = document.getElementById('speed-value');
    const gaugePathEl = document.getElementById('gauge-path');
    let lastScrollTop = window.scrollY;
    let lastTimestamp = performance.now();
    let currentSpeedPxS = 0;
    let displaySpeed = 0;
    
    function updateSpeedometer() {
        // Smooth easing for the number display
        displaySpeed += (currentSpeedPxS - displaySpeed) * 0.15;
        
        // Decay speed back to 0 when not scrolling
        currentSpeedPxS *= 0.92;
        if (currentSpeedPxS < 1) currentSpeedPxS = 0;
        
        const roundedSpeed = Math.round(displaySpeed);
        speedValueEl.textContent = `${roundedSpeed} px/s`;
        
        // Update circular gauge (Stroke dash array maps 0 to 100)
        // Let's assume max reasonable scroll speed is 10000 px/s
        let percentage = Math.min((roundedSpeed / 5000) * 100, 100);
        gaugePathEl.setAttribute('stroke-dasharray', `${percentage}, 100`);
        
        // Color transition logic matching the original (blue to orange based on speed)
        if (percentage > 50) {
            gaugePathEl.style.stroke = '#FF8000'; // McLaren Orange
        } else {
            gaugePathEl.style.stroke = '#0061FE'; // Dropbox Blue
        }
        
        requestAnimationFrame(updateSpeedometer);
    }
    requestAnimationFrame(updateSpeedometer);

    window.addEventListener('scroll', () => {
        const currentScrollTop = window.scrollY;
        const currentTimestamp = performance.now();
        
        const timeDiff = currentTimestamp - lastTimestamp;
        const scrollDiff = Math.abs(currentScrollTop - lastScrollTop);
        
        if (timeDiff > 0) {
            // Speed = pixels / ms -> multiply by 1000 for px/s
            const rawSpeed = (scrollDiff / timeDiff) * 1000;
            currentSpeedPxS = rawSpeed;
        }
        
        lastScrollTop = currentScrollTop;
        lastTimestamp = currentTimestamp;
    }, { passive: true });


    // --- 3. Intersection Observer for Scroll Reveal Animations ---
    const observerOptions = {
        root: null,
        rootMargin: '200px',
        threshold: 0.05
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    const animElements = document.querySelectorAll('.fade-in-up, .fade-in-left, .fade-in-right');
    animElements.forEach(el => observer.observe(el));
});
