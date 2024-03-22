"""
chapter 4
pyton Advanced(4) - 나만의 패키지 만들기(1)
Keyword - png(jpg) to gif, pil. image
"""

"""
패키지 작성
-> 정적이미지(JPG, PNG) -> GIT(애니메이션) 이미지 변환 패키지
"""

import glob # 폴더에 있는 다양한 이미지, 영상, 파일들을 한번에 가져와서 리스트형태로 반환해줌.
# os로도 가능하나 glbo으로 사용해볼 예정
from PIL import Image # Pyton Image Library

# 이미지, 결과 생성 경로
# glob이 있어서 끝에 *.png 가능 > png 파일 다가져와라
path_in = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/images/*.png'
path_out = 'E:/Study/Python/Middle_level_python_강의자료/수업자료/예제파일/project/image_out/result.gif'

# 첫 번째 이미지 & 모든 이미지 리스트 팩킹

#img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]
# image 형태로 리스트에 들어감

# 리사이즈 : resize = 320,240 가로세로, 
img, *images = [Image.open(f).resize((320,240),Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]



# 첫번째 이미지 기준 이미지 저장
img.save(
    fp = path_out,
    format = 'GIF',
    append_images = images,
    save_all = True,
    duration = 500,
    loop = 0
)

