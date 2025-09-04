from flask import Flask, request, redirect, url_for, flash, render_template
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret"

    # Store workouts in app.config (no globals)
    app.config["WORKOUTS"] = []

    @app.route('/')
    def index():
        workouts = app.config["WORKOUTS"]
        total_duration = sum(w["duration"] for w in workouts)
        return render_template('index.html', workouts=workouts, total_duration=total_duration)

    @app.route('/add', methods=['POST'])
    def add_workout():
        workouts = app.config["WORKOUTS"]
        workout_name = request.form.get("workout", "").strip()
        duration = request.form.get("duration", "").strip()

        if not workout_name or not duration:
            flash("Workout name and duration are required!", "error")
            return redirect(url_for("index"))

        try:
            duration = int(duration)
            if duration <= 0:
                raise ValueError
        except ValueError:
            flash("Invalid duration entered!", "error")
            return redirect(url_for("index"))

        workouts.append({
            "workout": workout_name,
            "duration": duration,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        flash(f"'{workout_name}' added successfully!", "success")
        return redirect(url_for("index"))

    @app.route('/delete/<int:index>')
    def delete_workout(index):
        workouts = app.config["WORKOUTS"]
        try:
            workout = workouts.pop(index)
            flash(f"'{workout['workout']}' deleted successfully!", "success")
        except IndexError:
            flash("Invalid workout selected", "error")
        return redirect(url_for("index"))

    return app


# Only run server if executing app.py directly
if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5173, debug=True)
