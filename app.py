from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', 'Festival Poster')

    # Trial ke liye demo image, baad me yahan AI lagega
    # Safety ke liye prompt ko saaf kar rahe hain
    safe_prompt = prompt[:100]

    return jsonify({
        'status': 'success',
        'prompt': safe_prompt,
        'image_url': f'https://dummyimage.com/512x512/101010/00FF88&text={safe_prompt.replace(" ", "+")}',
        'message': 'Trial Poster Ready!'
    })

if __name__ == '__main__':
    app.run()
