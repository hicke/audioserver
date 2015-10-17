from flask import Flask
import subprocess
import json

app = Flask(__name__)

@app.route("/soundcards")
def getSoundcards():
    indexCmd = ["pacmd list-sinks | grep index:"]
    indexP = subprocess.Popen(indexCmd,
                                    shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
    indexRawData, err = indexP.communicate()
    indexRawData = indexRawData.replace('index:','').replace('*','')
    indexArray = indexRawData.split('\n')

    nameCmd = ["pacmd list-sinks | grep name:"]
    nameP = subprocess.Popen(nameCmd,
                                    shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
    nameRawData, err = nameP.communicate()
    nameRawData = nameRawData.replace('name:','').replace('\t', '').replace('<', '').replace('>', '')
    nameArray = nameRawData.split('\n')

    #volumeCmd = ["pacmd list-sinks | grep volume:"]
    #volumeP = subprocess.Popen(volumeCmd,
    #                                shell=True,
    #                                stdout = subprocess.PIPE,
    #                                stderr=subprocess.PIPE,
    #                                stdin=subprocess.PIPE)
    #volumeRawData, err = volumeP.communicate()
    #volumeRawData = volumeRawData.replace('volume:','').replace('\t', '')
    #volumeArray = volumeRawData.split('\n')

    mutedCmd = ["pacmd list-sinks | grep muted:"]
    mutedP = subprocess.Popen(mutedCmd,
                                    shell=True,
                                    stdout = subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
    mutedRawData, err = mutedP.communicate()
    mutedRawData = mutedRawData.replace('muted:','').replace('\t', '')
    mutedArray = mutedRawData.split('\n')

    soundcards = []
    class Object(object):
        pass
    for i in range(len(indexArray)-1):
        soundcard = Object()
        soundcard.index = indexArray[i].strip()
        soundcard.name = nameArray[i].strip()
    #    soundcard.volume = volumeArray[i].strip()
        soundcard.muted = mutedArray[i].strip()
        soundcards.append(soundcard)

    def obj_dict(obj):
        return obj.__dict__

    jsonData = json.dumps(soundcards, default=obj_dict)

    return jsonData


@app.route("/volume/<soundcardId>/<percentValue>", methods=['POST'])
def volumeChange(soundcardId, percentValue):
    cmd = ["pactl", "set-sink-volume", soundcardId, percentValue + "%"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out


@app.route("/mute/<soundcardId>/<muteSetting>", methods=['POST'])
def volumeChange(soundcardId, percentValue):
    cmd = ["pactl", "set-sink-mute", soundcardId]
    muteP = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                              Shell=True,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE)
    out,err = muteP.communicate()
    return out

@app.route("/play", methods=['POST'])
def volumeChange(soundcardId, percentValue):
    cmd = ["mplayer 54454545.m4a"] # Only example file. Must be replaced by variable
    playP = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                              Shell=True,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE)
    out,err = playP.communicate()
    return out

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = 'True')
