AICOCO
======

입력 img_size = 28,28
<span style="color:red">max_pooling 에서 ksize = [1,2,2,1] , padding = 'SAME'으로 줬기 때문에 반토막난다.</span>

con1 :  (?, 14, 14, 32)
con2 :  (?, 7, 7, 64)
con3 :  (?, 4, 4, 128)
con4 :  (?, 2, 2, 256)
con5 :  (?, 1, 1, 128)

flatten :  (?, 128)        1 x 1 x 128

fc1 :  (?, 1024)           128을 입력으로 넣고 1024를 출력으로 지정해줬기 때문에 1024 결과
fc2 :  (?, 10)             1024를 입력으로 넣고 class 개수인 10을 출력으로 지정
 
![model](https://user-images.githubusercontent.com/48427281/89166949-bf176600-d5b5-11ea-8d84-4743b805b46d.JPG)
구조가 잘 보이지는 않지만 사진은 점점 반토막나서 작아지고 필터 수는 늘어나면서 5개의 conv layer를 거친다.
활성화함수로는 relu를 사용했고, cross_entroy_error로 loss를 구한 후, Adam으로 gradient를 최적화한다.
batch_size는 50이고, keep_prob는 1로 설정하여 dropout은 안했다.

![27fd6eda1b802ce09c97aab49d57955ff43ad912ad8dd55b04db6a64cddaf76d](https://user-images.githubusercontent.com/44748142/58758502-faa04580-8556-11e9-9bdf-fe82be954acf.gif)

Flower Classification
---------------------


#### 현재 진행 상황

- [:simple_smile:] 크롤링 방법을 사용하여 데이터셋을 각 꽃당 1000장 씩 모음 -> 10개의 클래스로 총 10000장
- [:simple_smile:] PIL 라이브러리를 사용하여 데이터셋을 90도 회전, 180도 회전, 270도 회전, 색반전, GRAY로
      채널 변경을 하여 총 50000 장의 데이터를 추가로 얻음 -> 원본 10000장 + 가공된 50000장의 데이터 셋
- [:simple_smile:] 엑셀에 꽃 축제 정보를 입력하여 파이썬으로 불러오기 
- [:simple_smile:] 데이터 라벨링이 완료된 npy 파일 완성 
- [:simple_smile:] 완성된 npy파일을 사용하여 CNN 학습

---------------------------------------------------------------------------------------------

#### 계획 대비 진행 상황

날짜별 계획서에 따라 100% 진행 완료

---------------------------------------------------------------------------------------------

#### 진행해야할 사항

- [:blush:] 학습에 사용된 모델의 정확도 비교
- [:blush:] 모델의 성능 향상
- [:blush:] 웹 앱 디자인
- [:blush:] CHECK POINT를 활용해 정확도 표출
- [:blush:] 웹 PREDICT 부분을 우리 CHECK POINT이용한 코드로 바꿔서 돌리기
- [:blush:] IMAGE RESIZE PILLOW 대신 OPENCV로 변경
- [:blush:] 우리코드 결과 이름만 있는거 [[이름],[ 확률] ] 꼴로 바꾸기
