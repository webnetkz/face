import cv2
import numpy as np
import pyautogui
import time

# разрешение экрана дисплея, получите его в настройках вашей ОС
SCREEN_SIZE = (pyautogui.size().width, pyautogui.size().height)
# определяем кодек
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
# создаем объект записи видео
#out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

while True:
    # сделать скриншот
    img = pyautogui.screenshot()
    # преобразовываем эти пиксели в правильный массив numpy для работы с OpenCV
    frame = np.array(img)
    # конвертировать цвета из BGR в RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # пишем фрейм
    #out.write(frame)
    # показать рамку
    cv2.imshow("screenshot", frame)
    # если пользователь нажимает q, он выходит
    if cv2.waitKey(1) == ord("q"):
        break

    time.sleep(5)
    break
    
    
# убедитесь, что все закрыто при выходе
cv2.destroyAllWindows()
#out.release()