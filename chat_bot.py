#Import the required libraries
from newspaper import Article, Config
import nltk
import bot_utils
import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template, request

# download nltk-punkt package
nltk.download('punkt', quiet=True)

# Get the article from web-page

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75  Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

article = Article('https://resources.workable.com/company-travel-policy#')
article.download()
article.parse()
article.nlp()
corpus = article.text

# look at the data
#print(corpus)


text = corpus
sentence_list = nltk.sent_tokenize(text)

#print(sentence_list)

exit_list = ['exit', 'bye', 'quit', 'thank you']


app = Flask(__name__)


@app.route('/')
def chat():
    return render_template('chat.html',
                           user_input='You Message will be displayed here',
                           response='Hey, I am Wiki (Automated BOT).\nI will be answering your queries about Company Travel Policy.\nIf you want to exit, Please type "bye/exit"')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    if user_input.lower() in exit_list:
        br = 'Wiki: Have a great day! Talk to you later :-)'
    else:
        if bot_utils.greeting_response(user_input) != None:
            br = bot_utils.greeting_response(user_input)
        else:
            br = bot_utils.bot_response(user_input, sentence_list)

    return render_template('chat.html', user_input=user_input, response=br)


if __name__ == '__main__':
    app.run(debug=True, port=5002)




