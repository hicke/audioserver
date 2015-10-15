from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/soundcards")
def getSoundcards():
    cmd = ["pacmd","list-sinks"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

@app.route("/volume/<soundcardId>/<percentValue>", methods=['POST'])
def volumeChange(soundcardId, percentValue):
    cmd = ["pactl", "set-sink-volume", soundcardId, percentValue]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out

if __name__ == "__main__":
    app.run()
