from pygame import mixer
from time import sleep
from threading import *
import steam
import glob
import UI.Main
import webbrowser


def stop_music():
    mixer.music.stop()


def launchnextgame():
    print("Launching next game!")
    glob.launchevent.set()


def timerstart():
    print("Starting timer and game!")
    glob.timerevent.set()


def launchgame(appid):
    print("Launching " + str(appid))
    # steam://rungameid/413150
    webbrowser.open("steam://rungameid/" + str(appid))


if __name__ == '__main__':
    glob.init()
    process = Thread(target=UI.Main.start)
    process.start()

    # music
    mixer.init()
    mixer.music.load("resources\\Shirk_Haunted_shortened.mp3")
    mixer.music.set_volume(.1)
    mixer.music.fadeout(5)

    # http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=D6BE6E6AD94C0688E53CC0FA2280675C&steamid=76561198065615146&format=json
    webAPI = steam.webapi.WebAPI("D6BE6E6AD94C0688E53CC0FA2280675C", format='json', raw=False, https=False,
                                 http_timeout=30, apihost='api.steampowered.com', auto_load_interfaces=True)
    response = webAPI.call("IPlayerService.GetOwnedGames", steamid="76561198065615146",
                           include_appinfo=0, include_played_free_games=0, appids_filter=0)
    print(response)
    gameslist = response["response"]["games"]
    print(gameslist)

    for game in gameslist:
        print(game)
        if int(game["playtime_forever"]) < 60:
            print("Waiting for OK from user (Button)")
            glob.launchevent.wait()
            launchgame(game["appid"])  # install/launch
            glob.launchevent.clear()
            glob.timerevent.wait()
            launchgame(game["appid"])  # launch
            sleep(10)  # 360 = 1h
            glob.timerevent.clear()
            mixer.music.play()

    while mixer.music.get_busy():
        sleep(1)

    process.join()
