import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configurez votre clé API OpenAI à partir d'une variable d'environnement
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get('prompt')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
