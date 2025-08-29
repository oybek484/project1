# Abstrakt sinf
class MediaPlayer:
    def play(self):
        raise NotImplementedError("play() metodi implement qilinishi kerak")

# MP3 Player
class MP3Player(MediaPlayer):
    def play(self):
        print("MP3 Player: Musiqa ijro etilmoqda...")

# Video Player
class VideoPlayer(MediaPlayer):
    def play(self):
        print("Video Player: Video va ovoz ijro etilmoqda...")

# Radio Player
class RadioPlayer(MediaPlayer):
    def play(self):
        print("Radio Player: Jonli radio eshittiruv ijro etilmoqda...")

# MediaFactory
class MediaFactory:
    @staticmethod
    def get_player(player_type):
        if player_type.lower() == "mp3":
            return MP3Player()
        elif player_type.lower() == "video":
            return VideoPlayer()
        elif player_type.lower() == "radio":
            return RadioPlayer()
        else:
            raise ValueError("Noto‘g‘ri player turi: " + player_type)

print("--- Media Player Tizimi ---")
mp3 = MediaFactory.get_player("mp3")
mp3.play()

video = MediaFactory.get_player("video")
video.play()

radio = MediaFactory.get_player("radio")
radio.play()


#2-masala    JavobBeruvchi interfeysi
# class JavobBeruvchi:
#     def javob_yarat(self, matn: str) -> str:
#         raise NotImplementedError("javob_yarat() metodi implement qilinishi kerak")
#
# # Do‘stonaBot
# class DostonaBot(JavobBeruvchi):
#     def javob_yarat(self, matn: str) -> str:
#         return f"Salom do‘stim! Siz aytdingiz: {matn}"
#
# # KinoyaliBot
# class KinoyaliBot(JavobBeruvchi):
#     def javob_yarat(self, matn: str) -> str:
#         return f"Ha albatta... bu juda muhim edi: {matn}"
#
# # RasmiyBot
# class RasmiyBot(JavobBeruvchi):
#     def javob_yarat(self, matn: str) -> str:
#         return f"Hurmatli foydalanuvchi, siz yozdingiz: “{matn}”. Rahmat!"
#
# # ChatXizmat sinfi
# class ChatXizmat:
#     def __init__(self, bot: JavobBeruvchi):
#         self.bot = bot
#
#     def foydalanuvchiga_javob_ber(self, matn: str):
#         print(self.bot.javob_yarat(matn))
#
# # Sinov
# print("\n--- Chatbot Sinovi ---")
#
# chat1 = ChatXizmat(DostonaBot())
# chat1.foydalanuvchiga_javob_ber("Bugun ob-havo qanday?")
#
# chat2 = ChatXizmat(KinoyaliBot())
# chat2.foydalanuvchiga_javob_ber("Bugun ishga boraymi?")
#
# chat3 = ChatXizmat(RasmiyBot())
# chat3.foydalanuvchiga_javob_ber("Yordam kerak.")


