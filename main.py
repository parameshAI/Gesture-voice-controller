import cv2
import mediapipe as mp
import pyautogui
import math
import speech_recognition as sr
import pyttsx3
import time

# --- 1. SETUP VOICE (Triggered by 'S' Key) ---
PROJECT_NAME = "CONTROL (Zero Lag)"
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"🤖 AI: {text}")
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

def active_listening():
    try:
        with sr.Microphone() as source:
            print("🎤 LISTENING... (Say: 'Open Chrome', 'Open Notepad')")
            listener.adjust_for_ambient_noise(source, duration=0.5)
            # Listen for 4 seconds max
            voice = listener.listen(source, timeout=4)
            command = listener.recognize_google(voice).lower()
            print(f"👤 YOU SAID: {command}")
            return command
    except:
        return ""

def execute_command(cmd):
    if "open" in cmd:
        app_name = cmd.replace("open", "").strip()
        speak(f"Opening {app_name}")
        pyautogui.press("win")
        time.sleep(0.5)
        pyautogui.write(app_name)
        time.sleep(0.5)
        pyautogui.press("enter")
    elif "stop" in cmd or "exit" in cmd:
        speak("Goodbye")
        return False
    else:
        speak("I didn't understand.")
    return True

# --- 2. SETUP VISION ---
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
pyautogui.FAILSAFE = False

print(f"✅ {PROJECT_NAME} ONLINE")
print("👉 RIGHT HAND: Move | Pinch=Click | Pinch+Hold=Drag")
print("👉 LEFT HAND:  Pinch=Vol Down | Open=Vol Up | Peace ✌️=Right Click")
print("⌨️  VOICE:     Press 'S' key to speak")

# Variables
pinch_start_time = 0
is_dragging = False
last_action_time = 0

running = True
while running:
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Tips
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # --- DETERMINE HAND SIDE ---
            
            # >>> RIGHT SIDE: MOUSE & DRAG <<<
            if index_tip.x > 0.5:
                # 1. Move Mouse
                target_x = int(index_tip.x * screen_width)
                target_y = int(index_tip.y * screen_height)
                pyautogui.moveTo(target_x, target_y)

                # 2. Click & Drag Logic
                dist = math.hypot(tx - ix, ty - iy)
                if dist < 40: # Pinch
                    if pinch_start_time == 0:
                        pinch_start_time = time.time()
                    
                    # DRAG if held > 0.4s
                    if time.time() - pinch_start_time > 0.4 and not is_dragging:
                        pyautogui.mouseDown()
                        is_dragging = True
                        print("✊ DRAGGING")
                    
                    # Visual: Red = Dragging, Green = Ready to Click
                    color = (0, 0, 255) if is_dragging else (0, 255, 0)
                    cv2.circle(img, (ix, iy), 15, color, cv2.FILLED)
                else:
                    if is_dragging:
                        pyautogui.mouseUp()
                        is_dragging = False
                        print("✋ DROPPED")
                    elif pinch_start_time > 0:
                        pyautogui.click()
                        print("🔵 LEFT CLICK")
                    pinch_start_time = 0

            # >>> LEFT SIDE: VOLUME & RIGHT CLICK <<<
            else:
                # 1. PEACE SIGN ✌️ (Right Click)
                # Logic: Index & Middle UP, Ring DOWN
                if index_tip.y < hand_landmarks.landmark[5].y and \
                   middle_tip.y < hand_landmarks.landmark[9].y and \
                   ring_tip.y > hand_landmarks.landmark[13].y:
                    
                    if time.time() - last_action_time > 1.0:
                        pyautogui.rightClick()
                        cv2.putText(img, "RIGHT CLICK", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                
                # 2. Volume Logic
                else:
                    dist = math.hypot(tx - ix, ty - iy)
                    if time.time() - last_action_time > 0.1:
                        if dist < 40: # Closed Pinch
                            pyautogui.press("volumedown")
                            cv2.putText(img, "VOL DOWN", (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                            last_action_time = time.time()
                        elif dist > 150: # Wide Open
                            pyautogui.press("volumeup")
                            cv2.putText(img, "VOL UP", (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                            last_action_time = time.time()

    cv2.imshow("CONTROL (Press S for Voice)", img)
    
    # --- KEYBOARD CONTROLS ---
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    # PRESS 'S' TO SPEAK
    if key == ord('s'):
        speak("Yes?")
        cmd = active_listening()
        if cmd:
            keep_going = execute_command(cmd)
            if not keep_going: running = False

cap.release()
cv2.destroyAllWindows()