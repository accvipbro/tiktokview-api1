from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/tiktokview", methods=["GET"])
def tiktokview():
    video_url = request.args.get("video")
    if not video_url:
        return jsonify({"error": "Thiếu link video"}), 400
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36"
        }
        r = requests.get(video_url, headers=headers, timeout=10)
        if r.status_code == 200:
            return jsonify({"success": True, "message": "Đã gửi request xem video"}), 200
        else:
            return jsonify({"success": False, "message": f"Lỗi: {r.status_code}"}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

app = app
