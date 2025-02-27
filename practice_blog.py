from flask import Flask, request, jsonify
import json

app = Flask(__name__)
DATA_FILE = "posts.json"

def load_posts():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_posts(posts):
    with open(DATA_FILE, "w") as file:
        json.dump(posts, file, indent=4)

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(load_posts())

@app.route("/posts", methods=["POST"])
def create_post():
    posts = load_posts()
    new_post = request.json
    new_post["id"] = len(posts) + 1
    posts.append(new_post)
    save_posts(posts)
    return jsonify(new_post), 201

@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    posts = load_posts()
    for post in posts:
        if post["id"] == post_id:
            post.update(request.json)
            save_posts(posts)
            return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    posts = load_posts()
    posts = [post for post in posts if post["id"] != post_id]
    save_posts(posts)
    return jsonify({"message": "Post deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
