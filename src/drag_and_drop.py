import cv2
from cvzone.HandTrackingModule import HandDetector
from drag_rect import RectUpdate

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=1, maxHands=2)
rec_color = (255, 255, 100)

cx, cy, w, h = 100, 100, 200, 200

rec_list = []

for x in range(5):
    rec_list.append(RectUpdate([x*150+100,100], rec_color))


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lm_list, _ = detector.findPosition(img)

    if lm_list:
        length, _, _ = detector.findDistance(8, 12, img)

        if length < 50:
            cursor = lm_list[8]
            for rec in rec_list:
                rec.update(cursor)
    
    for rec in rec_list:
        cx, cy = rec.pos_center
        w, h = rec.size
        cv2.rectangle(img, (cx-(w//2), cy-(h//2)), (cx+(w//2), cy+(h//2)), rec.rec_color, cv2.FILLED)

    cv2.imshow("image", img)
    cv2.waitKey(1)