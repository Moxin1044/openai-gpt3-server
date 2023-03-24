from flask import Flask, request
import openai


def openai_davinci(prompt):
    openai.api_key = "***"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=4000,
        n=1,
        stop=None,
    )
    return response['choices'][0].text


app = Flask(__name__)


@app.route('/')
def index():
    query = request.args.get('q')
    if query:
        return f'{openai_davinci(query)}'
    else:
        return '请求失败'


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=65111)