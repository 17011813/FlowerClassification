import tensorflow as tf
import random
import os
import numpy as np
from PIL import Image
import random
import time

import matplotlib.pyplot as plt
import cv2

   
def load_data(folder_name, label): # 데이터 불러오는 함수
   pic_names = os.listdir("./data/" + folder_name)
   temp = []

   for p in pic_names:
      img = Image.open("./data/" + folder_name + "/" + p) #괄호 안의 경로에 있는 이미지를 오픈.
      # + p 를 적은 이유는 data 폴더 안의 변수p 라는 이름을 가진 파일이라는 뜻을 나타내기 위함

      ####### 정규화 #######

      numerator = img - np.min(img)
      denominator = np.max(img)
      img = numerator / denominator + 1e-7 # 0값이 있으면 log 씌웠을 때 발산하니까 10^-7정도 작은 수를 넣어줌.

      ####### 정규화 #######
      
      img_array = np.expand_dims(np.array(img), axis=3) # 차원 맞춰줌.

      temp.append({label : img_array}) # 라벨 추가

   return temp

max_flower = 10 # 클래스 갯 수 

######### train 데이터  ######### 딕셔너리 형태
forsythia = load_data("forsythia",0)
buckwheat = load_data("buckwheat",1)
sunflower = load_data("sunflower",2)
cosmos = load_data("cosmos",3)
lily = load_data("lily",4)
roseofsharon = load_data("roseofsharon",5)
tulip = load_data("tulip",6)
cherryblossom = load_data("cherryblossom",7)
rose = load_data("rose",8)
korearose = load_data("korearose",9)

print("labeling finish")

x_data_list = forsythia + buckwheat + sunflower + cosmos + lily + roseofsharon + tulip + cherryblossom + rose + korearose
print("저장 중")
np.save("database2",x_data_list)
print("끝", len(x_data_list))
#database=np.load("database2_test")
#print(database_test)
#출처 https://stackoverflow.com/questions/19573809/open-images-from-a-folder-one-by-one-using-python
#출처 https://blog.naver.com/PostView.nhn?blogId=zzing0907&logNo=220213633559
#출처 https://stackoverflow.com/questions/51884439/store-and-label-image-in-a-2d-array-for-tensorflow
#출처 https://gldmg.tistory.com/43
