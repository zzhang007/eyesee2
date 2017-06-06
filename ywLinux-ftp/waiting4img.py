import os
import time
from shutil import move
import pysftp
host0="10.217.133.108"
user0="zzhang"
pwd0="zzhang007"

img_upload_dir = "/tmp-eyesee-computing/uploads/"
img_processing_dir = "/tmp-eyesee-computing/processing/";
img_result = "/tmp-eyesee-computing/result/";
ftp_dir = "/tmp-eyesee/result/";

while(1):
  ff = os.listdir(img_upload_dir)
  if ff==[]:
    print(" . . waiting for new image . . ")
  else:
    print("found new image, processing . .")
    time.sleep(2)
    for img in ff:
      f1 = open(img_result + img + '.txt', 'w');
      f1.write(img + '\n');
      f1.write('10011');
      f1.close();
      with pysftp.Connection(host0, username=user0, password=pwd0) as sftp:
        with sftp.cd(ftp_dir):             # temporarily chdir to public
          sftp.put(img_result + img + '.txt')
      print ('processing  '+img_upload_dir+img+' @ computing server')
      move(img_upload_dir + img, img_processing_dir+img);
      print ('move  ' + img_upload_dir + img + ' ::  to :: ' + img_processing_dir)

  time.sleep(2)
