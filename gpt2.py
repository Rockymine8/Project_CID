
    
from flask import Flask, request, render_template, url_for
import openai
import re
import os

#hey

app = Flask(__name__, static_url_path='/static')


#Set api key
openai.api_key = os.getenv("CHATGPT_API_KEY")

# define a function to check if a device can run Doom
def can_run_doom(device):
    # ask GPT-3.5 if the device can run Doom
    prompt = f"Is it possible to play 1993 doom on {device}? If the device is not a computer, answer no. If the thing in question has computer elements and could work or is a computer device, answer yes. Only answer in yes or no."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=60,
    )

    # parse the response and return a boolean value
    answer = response.choices[0].text.strip()
    return "Yes" in answer or "yes" in answer or "True" in answer or "true" in answer

# handle GET requests to the homepage
@app.route('/')
def home():
    return render_template('index.html')

    
# handle POST requests from the form
@app.route('/result', methods=['GET', 'POST'])
def check_doom():
    device = request.form['device']
    result = can_run_doom(device)
    if result:
        message = f"A {device} can run Doom!"
    else:
        message = f"Sorry, a {device} cannot run Doom."
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
    
#damn
