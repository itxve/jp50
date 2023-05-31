# 清音/平假名/写
voiceless_holiday_write = [
    "あ",
    "い",
    "う",
    "え",
    "お",
    "か",
    "き",
    "く",
    "け",
    "こ",
    "さ",
    "し",
    "す",
    "せ",
    "そ",
    "た",
    "ち",
    "つ",
    "て",
    "と",
    "な",
    "に",
    "ぬ",
    "ね",
    "の",
    "は",
    "ひ",
    "ふ",
    "へ",
    "ほ",
    "ま",
    "み",
    "む",
    "め",
    "も",
    "や",
    "い",
    "ゆ",
    "え",
    "よ",
    "ら",
    "り",
    "る",
    "れ",
    "ろ",
    "わ",
    "い",
    "う",
    "え",
    "を",
    "ん",
]

# 清音/假名/读
voiceless_read = [
    "a",
    "i",
    "u",
    "e",
    "o",
    "ka",
    "ki",
    "ku",
    "ke",
    "ko",
    "sa",
    "si",
    "su",
    "se",
    "so",
    "ta",
    "ti",
    "tu",
    "te",
    "to",
    "na",
    "ni",
    "nu",
    "ne",
    "no",
    "ha",
    "hi",
    "hu",
    "he",
    "ho",
    "ma",
    "mi",
    "mu",
    "me",
    "mo",
    "ya",
    "i",
    "yu",
    "e",
    "yo",
    "ra",
    "ri",
    "ru",
    "re",
    "ro",
    "wa",
    "i",
    "u",
    "e",
    "wo",
    "n",
]

# 清音/片假名/写
voiceless_film_leave_write = [
    "ア",
    "イ",
    "ウ",
    "エ",
    "オ",
    "カ",
    "キ",
    "ク",
    "ケ",
    "コ",
    "サ",
    "シ",
    "ス",
    "セ",
    "ソ",
    "タ",
    "チ",
    "ツ",
    "テ",
    "ト",
    "ナ",
    "ニ",
    "ヌ",
    "ネ",
    "ノ",
    "ハ",
    "ヒ",
    "フ",
    "ヘ",
    "ホ",
    "マ",
    "ミ",
    "ム",
    "メ",
    "モ",
    "ヤ",
    "イ",
    "ユ",
    "エ",
    "ヨ",
    "ラ",
    "リ",
    "ル",
    "レ",
    "ロ",
    "ワ",
    "イ",
    "ウ",
    "エ",
    "ヲ",
    "ン",
]

# 浊音/平假名/写
vibrant_holiday_write = [
    "が",
    "ぎ",
    "ぐ",
    "げ",
    "ご",
    "ざ",
    "じ",
    "ず",
    "ぜ",
    "ぞ",
    "だ",
    "ぢ",
    "づ",
    "で",
    "ど",
    "ば",
    "び",
    "ぶ",
    "べ",
    "ぼ",
    "ぱ",
    "ぴ",
    "ぷ",
    "ぺ",
    "ぽ",
]

# 浊音/读
vibrant_read = [
    "ga",
    "gi",
    "gu",
    "ge",
    "go",
    "za",
    "zi",
    "zu",
    "ze",
    "zo",
    "da",
    "di",
    "du",
    "de",
    "do",
    "ba",
    "bi",
    "bu",
    "be",
    "bo",
    "pa",
    "pi",
    "pu",
    "pe",
    "po",
]

# 浊音/片假名/写
vibrant_film_leave_write = [
    "ガ",
    "ギ",
    "グ",
    "ゲ",
    "ゴ",
    "ザ",
    "ジ",
    "ズ",
    "ゼ",
    "ゾ",
    "ダ",
    "ヂ",
    "ヅ",
    "デ",
    "ド",
    "バ",
    "ビ",
    "ブ",
    "ベ",
    "ボ",
    "パ",
    "ピ",
    "プ",
    "ペ",
    "ポ",
]


host = " https://res.hjfile.cn/pt/m/jp/50yin"
import requests, os


# 下载mp3
def down_mp3(str):
    url = f"{host}/audio/{str}.mp3"
    req = requests.get(url)
    os.makedirs(f"./mp3", exist_ok=True)
    with open(f"./mp3/{str}.mp3", "wb") as f:
        f.write(req.content)


# 下载gif
def down_gif(type, str, index, name):
    url = f"{host}/img/gif/{type}/{type}_gif_{str}{index}.gif"
    req = requests.get(url)
    os.makedirs(f"./gif/{type}", exist_ok=True)
    with open(f"./gif/{type}/{name}.gif", "wb") as f:
        f.write(req.content)


def get_down():
    for text in voiceless_holiday_write + vibrant_film_leave_write:
        print(f"downloading {text} mp3 source")
        down_mp3(text)

    for index, text in enumerate(voiceless_read):
        for type in ["ping", "pian"]:
            print(f"downloading {type} / {text} source")
            down_gif(type, text, index + 1, voiceless_holiday_write[index])


# get_down()



import 