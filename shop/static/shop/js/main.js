document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu
    const burgerBtn = document.getElementById('burgerBtn');
    const mainNav = document.getElementById('mainNav');

    if (burgerBtn && mainNav) {
        burgerBtn.addEventListener('click', function() {
            burgerBtn.classList.toggle('active');
            mainNav.classList.toggle('open');
        });

        mainNav.querySelectorAll('.header__link').forEach(function(link) {
            link.addEventListener('click', function() {
                burgerBtn.classList.remove('active');
                mainNav.classList.remove('open');
            });
        });
    }

    // Header scroll effect
    const header = document.getElementById('header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 20) {
                header.classList.add('header--scrolled');
            } else {
                header.classList.remove('header--scrolled');
            }
        });
    }

    // Scroll animations
    const animatedElements = document.querySelectorAll('.fade-in-up');
    if (animatedElements.length && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -40px 0px'
        });

        animatedElements.forEach(function(el, index) {
            el.style.transitionDelay = (index % 4) * 0.1 + 's';
            observer.observe(el);
        });
    } else {
        animatedElements.forEach(function(el) {
            el.classList.add('visible');
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                const top = target.getBoundingClientRect().top + window.scrollY - headerHeight;
                window.scrollTo({ top: top, behavior: 'smooth' });
            }
        });
    });
});
