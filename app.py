import os
from flask import Flask, render_template, request, jsonify
from config import config
from models import db, User

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load config
    env_config = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env_config if env_config in config else 'default'])
    
    # Initialize DB
    db.init_app(app)
    
    with app.app_context():
        # Create tables if they don't exist (mainly for SQLite dev)
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/submit', methods=['POST'])
    def submit_email():
        data = request.json
        email = data.get('email')
        
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        # Simple validation
        if '@' not in email or '.' not in email:
            return jsonify({'error': 'Invalid email format'}), 400

        try:
            # Check if email already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                 return jsonify({'message': 'Email already registered. We will contact you soon.'}), 200

            new_user = User(email=email)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'Success! We have received your request.'}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
