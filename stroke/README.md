# StrokeGuard - Stroke Risk Prediction Web Application

StrokeGuard is a Django-based web application that helps users assess their risk of stroke using machine learning. The application provides personalized risk assessments based on various health parameters and maintains a history of predictions for registered users.

## Features

- User authentication and registration
- Personalized user profiles
- Stroke risk prediction using machine learning
- Dashboard with prediction history
- Responsive design using Bootstrap
- Activity logging for user actions

## Tech Stack

- Python 3.8+
- Django 5.1.7
- scikit-learn
- pandas
- Bootstrap 5
- SQLite (development) / PostgreSQL (production)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/strokeguard.git
cd strokeguard
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your environment variables:
```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
strokeguard/
├── app/                    # Main application directory
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── static/           # Static files (CSS, JS, images)
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   └── forms.py          # Form definitions
├── stroke/               # Project configuration
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## Machine Learning Model

The stroke prediction model is trained using scikit-learn and considers the following features:
- Age
- Gender
- Various health indicators (hypertension, heart disease, etc.)
- Lifestyle factors (smoking status, etc.)
- Medical measurements (BMI, glucose level)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Security Considerations

- The project uses environment variables for sensitive information
- CSRF protection is enabled
- Password validation rules are enforced
- User sessions are managed securely

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django documentation and community
- scikit-learn documentation and community
- Bootstrap team for the excellent UI framework

## Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/strokeguard