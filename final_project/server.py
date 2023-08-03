from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate:
        translated_text = translator.translate(textToTranslate, src='en', dest='fr')
        return jsonify({"translated_text": translated_text})
    else:
        return jsonify({"error": "No text to translate."})
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    if textToTranslate:
        translated_text = translator.translate(textToTranslate, src='fr', dest='en')
        return jsonify({"translated_text": translated_text})
    else:
        return jsonify({"error": "No text to translate."})

    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
