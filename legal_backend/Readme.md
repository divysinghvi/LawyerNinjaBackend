# Legal Document Assistant

## Overview
This project is a Django-based backend for a legal document assistant. It allows users to upload PDFs, process them into text, and generate AI-driven legal drafts using the Ollama Mistral model. The backend is designed to integrate with a React-based frontend for seamless interaction.

## Features
- User authentication (Login & Signup)
- File upload & storage
- AI-powered legal draft generation
- REST API endpoints for frontend integration
- SQLite database support (can be extended to PostgreSQL/MySQL)

## Technologies Used
- **Backend:** Django, Django REST Framework (DRF)
- **AI Model:** Ollama Mistral
- **Database:** SQLite (configurable to PostgreSQL/MySQL)
- **Frontend Integration:** React (via API requests)
- **Authentication:** Django Authentication

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip
- Virtualenv (optional but recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/legal-doc-assistant.git
   cd legal-doc-assistant
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

6. Start the server:
   ```sh
   python manage.py runserver
   ```
   The backend will be available at `http://127.0.0.1:8000/`.

## API Endpoints
| Method | Endpoint            | Description                    |
|--------|---------------------|--------------------------------|
| POST   | `/api/upload/`      | Upload a legal document (PDF) |
| GET    | `/api/documents/`   | List uploaded documents       |
| GET    | `/api/draft/{id}/`  | Retrieve AI-generated draft   |

## Troubleshooting
### **Common Errors & Fixes**
#### 1. **No such table: api_uploadedfile**
   - Run migrations again:
     ```sh
     python manage.py makemigrations
     python manage.py migrate
     ```
   - Ensure the app is registered in `INSTALLED_APPS` in `settings.py`.

#### 2. **ModuleNotFoundError: No module named 'rest_framework'**
   - Ensure all dependencies are installed:
     ```sh
     pip install -r requirements.txt
     ```

#### 3. **500 Internal Server Error on Upload**
   - Check `logs/errors.log` for debugging.
   - Ensure media file handling is correctly configured in `settings.py`:
     ```python
     MEDIA_URL = '/media/'
     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
     ```

## Contribution Guidelines
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For inquiries, please contact divysinghvi5@gamil.com .

