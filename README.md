current function 

zzLinux: zz's ubuntu machine --- webserver
yaLinux: yw's ubuntu machine --- computing server

1/ zzLinux hosts web portal (php for now), receiving image from web browser 
   http://10.217.133.108/eyesee2/index.html, 
   then check whether it is a fundus image
2/ If yes, save the image to zzLinux local directory
3/ zzLinux back end processing code (python) continue checking if new image available, if yes, send the image to computing server ywLinux via SFTP
4/ yaLinux back end processing code (python) continue checking if new image available, if yes, produce pseudo diagnosis result, then send the result image to zzLinux
5/ zzLinux web portal checking if the result is available, if Yes, then display the result