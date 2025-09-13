from flask import Flask, jsonify, render_template

API_KEY="0f2ffeb209fb489c862b463c83746e6e"
url="https://newsapi.org/v2/everything?q=tesla&from=2025-08-11&sortBy=publishedAt&apiKey=0f2ffeb209fb489c862b463c83746e6e"

import requests

app=Flask(__name__)

@app.route("/api/news",methods=["GET"])
def get_news():
    response=requests.get(url)
    if response.status_code == 200:
        news_data=response.json()
        total_articles=len(news_data["articles"])
        first_article=news_data["articles"][0]
        author=first_article["author"]
        title=first_article["title"]
        publishedAt=first_article["publishedAt"]
        output_data={"total_articles":total_articles,
                    "auhtor":author,
                    "title":title,
                    "publishedAt":publishedAt}
        return jsonify(output_data)
        
    else:
        return jsonify({"msg":"invalid api keys"})


if __name__== "__main__":
    app.run(debug=True)