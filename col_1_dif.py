import cv2
import numpy as np

def get_color_name(bgr_value):
    color_names = {
        'red': (0, 0, 255),
        'green': (0, 255, 0),
        'blue': (255, 0, 0),
        'yellow': (0, 255, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'orange': (0, 165, 255),
        'purple': (128, 0, 128)     
    }
    
    min_distance = float('inf')
    closest_color = None
    
    for name, color in color_names.items():
        distance = np.linalg.norm(np.array(bgr_value) - np.array(color))
        if distance < min_distance:
            min_distance = distance
            closest_color = name
    
    return closest_color

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = frame[y, x]
        hsv_pixel = cv2.cvtColor(np.uint8([[pixel]]), cv2.COLOR_BGR2HSV)[0][0]
        color_name_bgr = get_color_name(pixel)
        color_name_hsv = get_color_name(hsv_pixel)
        print("BGR:", pixel, "Color Name (BGR):", color_name_bgr)
        #print("HSV:", hsv_pixel, "Color Name (HSV):", color_name_hsv)

cap = cv2.VideoCapture(0) #connection establish garna lai
cv2.namedWindow('Webcam')
cv2.setMouseCallback('Webcam', on_mouse_click)

while True:
    # frame capture garna lai
    ret, frame = cap.read()
    # webcam display garauna lai
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()