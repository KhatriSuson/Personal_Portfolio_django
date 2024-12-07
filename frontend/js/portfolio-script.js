
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll('.certification-card');
    items.forEach((item, index) => {
        item.style.opacity = "0";
        item.style.transform = "translateY(50px)";
        setTimeout(() => {
            item.style.transition = "opacity 0.5s ease, transform 0.5s ease";
            item.style.opacity = "1";
            item.style.transform = "translateY(0)";
        }, index * 200); // Delay for staggered animation
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const section = document.querySelector('.resume-content');
    section.style.opacity = "0";
    section.style.transform = "translateY(50px)";
    setTimeout(() => {
        section.style.transition = "opacity 0.8s ease, transform 0.8s ease";
        section.style.opacity = "1";
        section.style.transform = "translateY(0)";
    }, 300); // Delay to sync with page load
});

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('.contact-form');
    form.style.opacity = "0";
    form.style.transform = "translateY(50px)";
    setTimeout(() => {
        form.style.transition = "opacity 0.8s ease, transform 0.8s ease";
        form.style.opacity = "1";
        form.style.transform = "translateY(0)";
    }, 300);
});

  // Theme Toggle
  const toggleTheme = document.querySelector('.theme-toggle');
  toggleTheme.addEventListener('click', () => {
      document.body.dataset.theme = document.body.dataset.theme === 'dark' ? '' : 'dark';
  });

  // Mobile Menu Toggle
  const hamburger = document.querySelector('.hamburger');
  const navMenu = document.querySelector('nav ul');
  hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('active');
  });