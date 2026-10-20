from pepperapi import ALVideoDevice
import pepperapi.robot_client as rc
from PIL import Image
import io
rc.init("192.168.0.147")
def get_head_cam_image() -> bytes:
    """Get jpeg bytes from an image captured with the head cam"""
    cam = ALVideoDevice.subscribeCamera("testcam", 0, 1, 11, 5)
    image_data = ALVideoDevice.getImageRemote(cam)
    width, height, pixels = image_data[0], image_data[1], image_data[6]
    ALVideoDevice.unsubscribe(cam)
    image = Image.frombytes("RGB", (width, height), pixels)
    save_buf = io.BytesIO()
    image.save(save_buf, format="JPEG")
    return save_buf.getvalue()
open("tmp/imagetest.jpg", "bw").write(get_head_cam_image())
