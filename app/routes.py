from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)

@api.route('/generate', methods=['POST'])
def generate_content():
    data = request.get_json()
    prompt = data.get('prompt', '')
    instructions = data.get('instructions', '')
    
    # Mock response logic
    response = f"This is a mock response based on the prompt: '{prompt}' with instructions: '{instructions}'"
    
    return jsonify({"response": response})
