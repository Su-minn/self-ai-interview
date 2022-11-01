from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from navertts import NaverTTS


def jussuit_naver_tts(text: str) -> None:
    tts = NaverTTS(text, lang="ko")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp = BytesIO(fp.getvalue())
    my_sound = AudioSegment.from_file(fp, format="mp3")
    play(my_sound)
