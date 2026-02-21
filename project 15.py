import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(

  min_detection_confidence=0.7,

  min_tracking_confidence=0.7

)
draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam error")
    exit()
def detect_gesture(lm):
    tip = [4, 8, 12, 16, 20]
    pip = [2, 6, 10, 14, 18]
    ext = 0
    if abs(lm[tip[0]].x - lm[pip[0]].x) > 0.04:
        ext += 1
    ext += sum(lm[tip[i]].y < lm[pip[i]].y for i in range(1, 5))
    return "Open" if ext >= 4 else "Closed Fist" if ext <= 1 else "Partial"
print("Press 'q' to quit")
while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    gesture = "No hand"
    if result.multi_hand_landmarks:
        for i, hand in enumerate(result.multi_hand_landmarks):
            draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            lm = hand.landmark
            gesture = detect_gesture(lm)
            for id in [4, 8, 12, 16, 20]:
                x, y = int(lm[id].x * frame.shape[1]), int(lm[id].y * frame.shape[0])
                cv2.circle(frame, (x, y), 8, (255, 0, 255), -1)
    color = (0, 255, 0) if gesture in ["Open", "Closed Fist"] else (0, 165, 255)
    cv2.putText(frame, f"Gesture: {gesture}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Hand Gesture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
