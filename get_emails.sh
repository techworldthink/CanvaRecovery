#!/bin/bash

# Execute Python code inside the container to fetch emails using the app context
docker exec canva-recovery python -c "
from app import create_app
from models import User

app = create_app()
with app.app_context():
    users = User.query.all()
    print(f'Found {len(users)} emails:')
    print('-' * 30)
    for user in users:
        print(f'{user.email} (Joined: {user.created_at})')
"
