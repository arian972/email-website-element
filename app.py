from flask import Flask, request, jsonify, send_from_directory
import smtplib
from email.message import EmailMessage

app = Flask(__name__, static_folder='.', static_url_path='')

# Email configuration (you need to configure your SMTP here)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'arian.bartholovich@gmail.com'      # Replace with your email (must allow SMTP access)
SMTP_PASSWORD = 'hyuvlixwdftvqpaf'         # Use app password or your SMTP password

RECEIVER_EMAIL = 'arian.bartholovich@gmail.com'

@app.route('/')
def serve_index():
    return send_from_directory('.', 'templates/index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    name = data.get('name', '').strip()
    sender_email = data.get('email', '').strip()
    message_body = data.get('message', '').strip()

    if not name or not sender_email or not message_body:
        return jsonify({'error': 'Please fill in all fields.'}), 400

    msg = EmailMessage()
    msg['Subject'] = f'New message from {name} via website'
    msg['From'] = sender_email
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message_body}")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            smtp.send_message(msg)
        return jsonify({'message': 'Email sent successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
