# load image
from kivy.app import App
from kivy.uix.image import Image, AsyncImage


class Paint5App(App):
    def build(self):
        #img = Image(source='boo.jpg')
        img = AsyncImage(
            source='https://inteng-storage.s3.amazonaws.com/img/iea/y5wWnBlP6X/sizes/ai-main_resize_md.jpg')
        return img


Paint5App().run()
