const form = document.getElementById('contact-form');
const status = document.getElementById('status');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  status.textContent = 'Sending...';
  status.style.color = varToRgb('--display-text');

  const formData = {
    name: form.name.value.trim(),
    email: form.email.value.trim(),
    message: form.message.value.trim()
  };

  try {
    const response = await fetch('/send-email', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });

    const data = await response.json();

    if (response.ok) {
      status.textContent = 'Message sent successfully!';
      status.style.color = 'limegreen';
      form.reset();
    } else {
      throw new Error(data.error || 'Failed to send message');
    }
  } catch (err) {
    status.textContent = 'Error: ' + err.message;
    status.style.color = 'tomato';
  }
});

function varToRgb(variable) {
  return getComputedStyle(document.documentElement).getPropertyValue(variable).trim();
}
