 document.addEventListener('DOMContentLoaded', function () {
        // Form validation and enhancement
        const form = document.getElementById('contactForm');
        const submitBtn = form.querySelector('.btn-send');

        form.addEventListener('submit', function (e) {
            // Add loading state
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
            submitBtn.disabled = true;

            // Re-enable button after 3 seconds (in case of errors)
            setTimeout(function () {
                submitBtn.innerHTML = '<i class="fas fa-paper-plane me-2"></i>Send Message';
                submitBtn.disabled = false;
            }, 3000);
        });

        // Auto-hide alerts after 5 seconds
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            setTimeout(function () {
                alert.classList.add('fade');
                setTimeout(function () {
                    alert.remove();
                }, 150);
            }, 5000);
        });
    });