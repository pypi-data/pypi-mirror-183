import mediapipe as mp
import cv2

class ht():
    def __init__(self):
        self.handsmp = mp.solutions.hands
        self.hands = self.handsmp.Hands()
        self.drawmp = mp.solutions.drawing_utils

    def findhand(self, img, show_lines=True):
        img = cv2.flip(img, 1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        self.output =  results.multi_hand_landmarks
        self.h, self.w, _ = img.shape
        if self.output:
            self.lm = self.output[0].landmark
            if show_lines:
                for i in self.output:
                    self.drawmp.draw_landmarks(img, i, self.handsmp.HAND_CONNECTIONS)
        return img
    def findpos(self):
        lml = []
        if self.output:
            hand = self.output[0].landmark
            for id, lms in enumerate(hand):
                    x = int(lms.x * self.w)
                    y = int(lms.y * self.h) 
                    lml.append([x, y])
        return lml


