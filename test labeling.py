import tensorflow as tf
import random
import os
import numpy as np
from PIL import Image
import random
import time
   
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
forsythia_test = load_data("forsythia_test",0)
buckwheat_test = load_data("buckwheat_test",1)
sunflower_test = load_data("sunflower_test",2)
cosmos_test = load_data("cosmos_test",3)
lily_test = load_data("lily_test",4)
roseofsharon_test = load_data("roseofsharon_test",5)
tulip_test = load_data("tulip_test",6)
cherryblossom_test = load_data("cherryblossom_test",7)
rose_test = load_data("rose_test",8)
korearose_test = load_data("korearose_test",9)
#각 폴더 안에 있는 각 사진에다 클래스의 번호를 라벨링하는거임
print("labeling finish")

x_data_list_test = forsythia_test + buckwheat_test + sunflower_test + cosmos_test + lily_test + roseofsharon_test + tulip_test + cherryblossom_test + rose_test + korearose_test
print("저장 중")
np.save("database2_test",x_data_list_test)
print("끝", len(x_data_list_test))
#database=np.load("database2_test")
#print(database_test)
#출처 https://stackoverflow.com/questions/19573809/open-images-from-a-folder-one-by-one-using-python
#출처 https://blog.naver.com/PostView.nhn?blogId=zzing0907&logNo=220213633559
#출처 https://stackoverflow.com/questions/51884439/store-and-label-image-in-a-2d-array-for-tensorflow
#출처 https://gldmg.tistory.com/43

