from flask import Flask, render_template
import random
import os

app = Flask(__name__)


from openai import OpenAI

d ="sk-B1x6tnwRIcca4WOzureUFhWzoxvywPgNBWZ_q7TPIqT3BlbkFJzAZH4ZKwJYmFM7_C950QkACr14DYWfmRZCe5tkBiMA"

client = OpenAI(api_key=d)

def AI(query):
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[ {"role": "user", "content": query} ],max_tokens=1000 )
    return response.choices[0].message.content
# Simulate a function to fetch text from an AI API

def fetch_random_article():
    # Placeholder for AI-generated API content (replace this with actual API integration)
    articles = [
        {"title": "Understanding Phishing Attacks", 
         "content": AI("Give me a detailed article on :"+ "Understanding Phishing Attacks")},
        {"title": "Importance of Strong Passwords", 
         "content": AI("Give me a detailed article on :"+ "Importance of Strong Passwords")},
        {"title": "Top 5 Cybersecurity Practices", 
         "content": AI("Give me a detailed article on :"+ "Top 5 Cybersecurity Practices")},
    ]
    return random.choice(articles)  # Return a random article

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/articles")
def articles():
    article = fetch_random_article()
    return render_template("articles.html", title="Articles", article=article)

@app.route("/knowledge-hub")
def knowledge_hub():
    return render_template("knowledge_hub.html", title="Knowledge Hub")

@app.route("/forum")
def forum():
    return render_template("forum.html", title="Community Forum")

@app.route("/events")
def events():
    return render_template("events.html", title="Events")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
