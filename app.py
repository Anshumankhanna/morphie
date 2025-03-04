from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv
from mistralai import Mistral

import os
import json

load_dotenv()

app = Flask(__name__)
CORS(app)

system_prompt = """
    You are a design assistant who responds only when the user’s question will be of the type:\n

    1) If the user is having a introductory conversation state your purpose
    
    2) When the user states a type of website (e.g., e-commerce, blog, portfolio, marketing, etc.), you should 
    respond with a suggested colors and one of three layout types (masonry, bento, or grid).\n
    Return an object that contains colors and layout field, both fields should be lists with 3 items at least\n
    Each item in colors list should be comprised of an object that has 'primary_color', 'secondary_color', 'accent_color' and 'background_color'\n
    background_color should be shades of black or white, consider popularly used shades for the specified website type and primary_color, secondary_color, and accent_color should be vibrant and should be of the same shade\n
    Even if layout or colors are specified, make sure no value should be left empty, the output should always have the said structure
"""

'''The output returned by this route will an object, that can contain these fields:
    {
        "colors": [],
        "layout": [],
        "output": [],
        "error": [],
    }

    All of these fields may or may not exist.
    If the first two fields exist, we have a good answer,
    If the third field exists, we have an intermediate answer (just a conversation but not giving the colors and layouts),
    If the last field exists, we have an error and we can't do anything about it.
'''
@app.route("/", methods=["POST"])
def chat_endpoint():
    api_key = os.getenv("MISTRAL_API_KEY")
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)
    
    # Get the user input from the query string (POST parameter)
    user_input = request.args.get("user_input")

    # print(user_input)

    chat_response = client.chat.complete(
        model = model,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )

    output = chat_response.choices[0].message.content

    # Parse JSON response from model
    start, end = output.find('{'), output.rfind('}')
    
    if end != -1:
        try:
            # when we have { colors, layout } object output.
            return Response(output[start : end + 1], content_type="application/json"), 200
        except json.JSONDecodeError:
            # when we can't process the output to become { colors, layout }.
            return jsonify({ "error": "Could not parse response from model" }), 500

    # when we have an intermediatary output.
    return jsonify({ "output": output }), 500


if __name__ == "__main__":
    app.run()