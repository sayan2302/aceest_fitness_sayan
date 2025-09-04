# ACEest Fitness and Gym

A Flask-based web application for tracking workouts, built for the Introduction to DevOps Assignment by Sayan Pramanick. 
The app allows users to add, view, and delete workouts, with automated testing and containerization using Pytest, Docker, and GitHub Actions.

## Features
- Add workouts with name, duration (minutes), and timestamp.
- View workouts in a table with total duration.
- Delete workouts with confirmation messages.
- Automated CI/CD pipeline for building and testing.

## Project Structure
```
aceest_fitness_sayan/
├── app.py              # Flask application
├── templates/
│   └── index.html      # HTML template for the UI
├── test_app.py         # Pytest unit tests
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── .github/
│   └── workflows/
│       └── main.yml    # GitHub Actions CI/CD pipeline
└── README.md           # Project documentation
```

## Setup and Running Locally
1. **Ensure Python is Installed:Verify that Python 3.13 or later is installed on your system:**:
   ```bash
   python --version
   ```
   If Python is not installed, download and install it from python.org. Ensure python is added to your system's PATH.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/sayan2302/aceest_fitness_sayan.git
   cd aceest_fitness_sayan
   ```

3. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in a web browser to access the UI.

## Running Tests Locally
1. **Install Testing Dependencies**:
   ```bash
   Already Installed from requirements.txt
   ```

2. **Run Pytest**:
   ```bash
   pytest -v
   ```

## GitHub Actions CI/CD Pipeline
The pipeline (`.github/workflows/main.yml`) runs on every push or pull request to the `main` branch:
- Sets up Python 3.13 and installs dependencies.
- Runs Pytest unit tests to validate functionality.
- Builds a Docker image for the application.

Check the **Actions** tab in the GitHub repository to view workflow runs.

## Running with Docker
1. **Build the Docker Image**:
   ```bash
   docker build -t aceest-fitness .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 5000:5000 aceest-fitness
   ```
   Access the app at `http://127.0.0.1:5000`.

## Troubleshooting
- **TemplateNotFound Error**: Ensure `index.html` is in the `templates/` folder.
- **500 Internal Server Error**: Check the terminal for stack traces and verify `app.py` and `index.html` match the provided code.
- **Connection Issues**: Ensure port 5000 is open (e.g., check firewall settings) and try `http://127.0.0.1:5000`.

## License
MIT License