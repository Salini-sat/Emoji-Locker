import cv2
import mediapipe as mp
import json
from expression_utils import detect_expression
import os


os.makedirs("user_data", exist_ok=True)


username = input("Enter your username: ")

# Load password
try:
    with open("user_data/passwords.json", "r") as f:
        data = json.load(f)
        real_password = data[username]
except:
    print("User not found.")
    exit()

print("Now perform your expression sequence...")

cap = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

user_input = []

while len(user_input) < len(real_password):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            expr = detect_expression(face.landmark, frame.shape[1], frame.shape[0])
            cv2.putText(frame, f"Detected: {expr}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if expr != "Neutral" and (len(user_input) == 0 or expr != user_input[-1]):
                print(f"Step {len(user_input)+1}: {expr}")
                user_input.append(expr)
                cv2.waitKey(2000)

    cv2.imshow("Login - Emoji Locker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if user_input == real_password:
    print("✅ Access Granted!")
else:
    print("❌ Access Denied.")