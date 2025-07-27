import cv2
import mediapipe as mp
import json
from expression_utils import detect_expression
import os



os.makedirs("user_data", exist_ok=True)


user_password = []
username = input("Enter your username: ")

# Setup
cap = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
print("Perform 3 expressions (like Smile, Wink, Surprise). Hold each for 3 seconds.")

while len(user_password) < 3:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            expr = detect_expression(face.landmark, frame.shape[1], frame.shape[0])
            cv2.putText(frame, f"Detected: {expr}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            if expr != "Neutral" and (len(user_password) == 0 or expr != user_password[-1]):
                print(f"Expression {len(user_password)+1}: {expr}")
                user_password.append(expr)
                cv2.waitKey(2000)  # 2-second pause

    cv2.imshow("Register - Emoji Locker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save to JSON
try:
    with open("user_data/passwords.json", "r") as f:
        data = json.load(f)
except:
    data = {}

data[username] = user_password

with open("user_data/passwords.json", "w") as f:
    json.dump(data, f, indent=2)

print("Password saved!")
