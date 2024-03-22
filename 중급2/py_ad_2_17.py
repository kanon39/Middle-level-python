"""
chapter 4
pyton Advanced(4) - 나만의 패키지 만들기(1)
Keyword - png(jpg) to gif, pil. image
"""

"""
패키지 작성
-> 정적이미지(JPG, PNG) -> GIF 이미지 변환기를 패키지 호출 형태로 작성
"""

import glob
from PIL import Image
# 에러가 안나게 견고하게 설계해야 개발 실력이 많이 향상됨.
class GifConverter :
    def __init__ (self, path_in=None, path_out=None, resize = (320,240)):
        """
        path_in : 원본 여러 이미지 경로(Ex : images/*.png)
        path_ou : 결과 이미지 경로(Ex : output/filename.gif)
        resize : 리사이징 크기 ((320,240))
        """
        self.path_in = path_in or './*.png' # 같은 경로에 png를 쓰거나 아니면 해당경로에자동으로 png 파일 찾기
        self.path_out = path_out or './output.gif'
        self.resize = resize
        
    def convert_gif(self) :
        """
        GIF 이미지 변환 기능 수행
        """
        print(self.path_in, self.path_out, self.resize) # 배포할떄는 print가아니라 logging을 이용해서 만들어야함
        
        img, *images = \
            [Image.open(f).resize(self.resize,Image.ANTIALIAS) for f in sorted(glob.glob(self.path_in))]
            
        try :
            img.save(
                        fp = self.path_out,
                        format = 'GIF',
                        append_images = images,
                        save_all = True,
                        duration = 500,
                        loop = 0
                    )
        except IOError :
            print('Cannot convet!', img)



# 그런데 아래처럼 실행한 이력까지배포해버리면 실행시켰을떄 
# 아래 코드까지 다 돌아가게 된다. 그래서 __name__ = '__main__'이 있는 것이다.
# 이 패키지를 import 하지않고 그냥실행하게되면 이 코드창이 main이 된다.
# 만약 다른 오픈소스 창에서 이 class를 실행한다하면 아래 main이 실행되지 않는다.
if __name__ == '__main__' :
    path_in = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/images/*.png'
    path_out = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/image_out/result.gif'

    # 클래스
    c = GifConverter(path_in, path_out,(320,240))
    # 반환
    c.convert_gif()
