import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# random greeting response
def greeting_response(text):
    text = text.lower()

    # Bots greeting response
    bot_greetings = ['Hi, This is Wiki(An automated bot).\nHow can i help you?',
                     'Hello, This is Wiki(An automated bot).\nHow can i help you?',
                     'Hey, This is Wiki(An automated bot).\nHow can i help you?',
                     'Hola, This is Wiki(An automated bot).\nHow can i help you?']

    # User_greetings
    user_greetings = ['hi', 'hello', 'hey', 'good morning', 'morning']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index



def bot_response(user_input, sentence_list):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response_message = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()

    # find the index of the highest similarity score
    index = index_sort(similarity_scores_list)
    index = index[1:]

    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response_message = bot_response_message + ' '+sentence_list[index[i]]
            response_flag = 1
            j += 1
        if j>2:
            break
    if response_flag == 0:
        bot_response_message = bot_response_message+' '+'I apologize, I couldnt help you.\nOur HR personnel will contact you within 12 hours'

    sentence_list.remove(user_input)
    return bot_response_message