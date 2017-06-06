import os
import time
from shutil import move
import pysftp
host0="10.217.134.130"
user0="yanwu"
pwd0="yanwu"

img_upload_dir = "/tmp-eyesee/uploads/"
img_processing_dir = "/tmp-eyesee/processing/"

ftp_dir = "/tmp-eyesee-computing/uploads/"
    
while(1):  
  ff = os.listdir(img_upload_dir)
  if ff==[]:  
    print("waiting for new image")
  else:
    print("found new image, processing")
    time.sleep(2)
    for img in ff:
      with pysftp.Connection(host0, username=user0, password=pwd0) as sftp:
        with sftp.cd(ftp_dir):             # temporarily chdir to public
          sftp.put(img_upload_dir + img)  # upload file to public/ on remote   
      sftp.close()
      print ('send  ' + img_upload_dir + img + ' :: to :: computing server via sftp')
      move(img_upload_dir + img, img_processing_dir+img);
      print ('move  ' + img_upload_dir + img + ' ::  to :: ' + img_processing_dir)      

  time.sleep(2)
  