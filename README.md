** current workflow **

1/ zzLinux hosts web portal (php for now), receiving image from web browser 
http://10.217.133.108/eyesee2/index.html , with image validation.

2/ If yes, save the image to zzLinux local directory

3/ zzLinux back end processing code (python) continue waiting for new image.
If found, it send the image to computing server ywLinux via SFTP, then continue waiting

4/ ywLinux back end processing code (python) continue waiting for new image.
If found, produce pseudo diagnosis result, then send the result to zzLinux

5/ zzLinux web portal checking if the result is available, if Yes, then display the result

6/ No any error checking / logging stuff for now, just make sure the connection all working well.
