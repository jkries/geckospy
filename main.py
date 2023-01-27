import cv2
import pyshine as ps
HTML="""
<html> <head> <title>GeckoSpy&#8482;</title> </head> <body>
<center><h1>GeckoSpy&#8482; Live Stream</h1></center>
<center><img src="stream.mjpg" width='800' height='600' autoplay
playsinline></center> </body> </html> """
def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,HTML)
    address = ('YOURIPADDRESS',9000) # Enter your IP address
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,800)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
        capture.set(cv2.CAP_PROP_FPS,30)
        StreamProps.set_Capture(StreamProps,capture)
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        print('Server started at','http://'+address[0]+':'+str(address[1]))
        server.serve_forever()

    except KeyboardInterrupt:
        capture.release()
        server.socket.close()

if __name__=='__main__':
    main()
