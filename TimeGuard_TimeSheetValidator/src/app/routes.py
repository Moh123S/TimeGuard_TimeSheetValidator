from flask import render_template, request, jsonify
from src.utils.csv_parser import parse_csv
from src.services.validation_service import validate_timesheet
from werkzeug.utils import secure_filename
import os

def init_routes(app):
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            os.makedirs('uploads', exist_ok=True)
            file.save(filepath)
            timesheet = parse_csv(filepath)
            report = validate_timesheet(timesheet)
            return jsonify({'report': report})