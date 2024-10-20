from flask import Flask, render_template, request, jsonify
from models.plagiarism_checker import check_plagiarism
from models.ai_detector import detect_ai_content
from percentage_calc import calculate_percentage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_text():
    text = request.form['text']
    
    # Run plagiarism check
    plagiarism_result = check_plagiarism(text)
    
    # Run AI content detection
    ai_result = detect_ai_content(text)
    
    # Calculate percentages
    plagiarism_percentage = calculate_percentage(plagiarism_result, text)
    ai_percentage = calculate_percentage(ai_result, text)
    
    return render_template('result.html', plagiarism=plagiarism_percentage, 
                           ai=ai_percentage, plagiarism_result=plagiarism_result, 
                           ai_result=ai_result)

if __name__ == '__main__':
    app.run(debug=True)
