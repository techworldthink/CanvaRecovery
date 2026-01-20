document.getElementById('recoveryForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const emailInput = document.getElementById('email');
    const submitBtn = document.getElementById('submitBtn');
    const messageArea = document.getElementById('messageArea');
    const email = emailInput.value.trim();

    // Reset UI
    messageArea.className = 'message';
    messageArea.textContent = '';
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email }),
        });

        const data = await response.json();

        if (response.ok) {
            messageArea.textContent = data.message;
            messageArea.classList.add('success');
            emailInput.value = ''; // Clear input on success
        } else {
            messageArea.textContent = data.error || 'Something went wrong. Please try again.';
            messageArea.classList.add('error');
        }
    } catch (error) {
        console.error('Error:', error);
        messageArea.textContent = 'Network error. Please try again later.';
        messageArea.classList.add('error');
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<span>Recover Access</span>';
    }
});
