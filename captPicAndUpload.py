import cv2,dropbox,time,random

startTime=time.time()

def take_snapshot():
    rnum=random.randint(0,99)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imgN="img"+str(rnum)+".png"
        cv2.imwrite(imgN,frame)
        startTime=time.time
        result=False
    return imgN
    print("Snapshot Taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def upload_file(imgN):
    access_token="sl.BLbh9FsaBznE7bb80AxDFaocMo_JoBvCYqG77ZzUqcEPtrw4NdAT-N7Xeul4IDyeNrFVmPVBk_CT56IsRc_bhxteQ1ydbReP2a-abHhn_Zk71dEBuLgPgNJtbjwlQEagcVaul_I"
    file=imgN
    file_from=file
    file_to="/newFolder/"+(imgN)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=20):
            name=take_snapshot()
            upload_file(name)
main()
    
