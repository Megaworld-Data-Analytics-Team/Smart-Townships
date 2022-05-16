import numpy
import cv2
import json

# class Vehicle(object):

config = {
    "NUMBER_OF_LINES": 2,
    "START_POINT": [
        [400, 400], [600, 600]
    ],
    "END_POINT": [
        [1000, 400], [1500, 600]
    ],
    "COLOR_OF_LINE": [255, 255, 0],
    "DISTANCE": 100  # meter
}
KMH = 3.6

def draw_lines(frame):
    """

    Add color line based on START_POINT and END_POINT

    """
    number_of_line = config["NUMBER_OF_LINES"]
    color_line = config["COLOR_OF_LINE"]
    color = (color_line[0], color_line[1], color_line[2])
    for i in range(number_of_line):
        start_point = config["START_POINT"][i]
        end_point = config["END_POINT"][i]
        cv2.line(frame, (start_point[0], start_point[1]), (end_point[0], end_point[1]), color, 2)


def is_crossed(id, center, start_point, end_point):
    """
    Function to check if vehicle has crossed the end line
    """
    res = center[1] - end_point[1] - (
            ((end_point[1] - start_point[1]) / (end_point[0] - start_point[0])) * (center[0] - end_point[0]))

    if res >= 0:
        return True
    else:
        return False


class VelocityTracker:

    def __init__(self):

        self.startFrames = {}
        self.endFrames = {}
        self.section = {}
        self.velocity = {}
        self.direction = {}  
        self.startLine = (config["START_POINT"][0], config["END_POINT"][0])
        self.endLine = (config["START_POINT"][1], config["END_POINT"][1])
        print(self.endLine)

    def calculate(self, id, fps, end_frame):
        duration = abs(self.startFrames[id] - end_frame) / fps
        distance_meter = config["DISTANCE"]

        velocity = distance_meter / duration * KMH
        return round(velocity, 3)

    def section_check(self, fps, fcnt, id, center, frame, bbox):
        if self.direction[id] == 1:  
            if is_crossed(id, center, self.endLine[0], self.endLine[1]) == False and self.section[id] == 3:
                self.section[id] -= 1
                self.startFrames[id] = fcnt
            elif is_crossed(id, center, self.startLine[0], self.startLine[1]) == False and self.section[id] == 2:
                self.section[id] -= 1
                self.endFrames[id] = fcnt  # for later use
                self.velocity[id] = self.calculate(id, fps, fcnt)
            elif self.section[id] == 1:
                cv2.putText(frame, str(self.velocity[id]) + "km/h", (int(bbox[2]), int(bbox[3])), 0, 5e-3 * 150,
                            (255, 0, 255), 2)

        elif self.direction[id] == -1:  
            if is_crossed(id, center, self.startLine[0], self.startLine[1]) and self.section[id] == 1:
                self.section[id] += 1
                self.startFrames[id] = fcnt
            elif is_crossed(id, center, self.endLine[0], self.endLine[1]) and self.section[id] == 2:
                self.section[id] += 1
                self.endFrames[id] = fcnt  # for later use
                self.velocity[id] = self.calculate(id, fps, fcnt)
            elif self.section[id] == 3:
                cv2.putText(frame, str(self.velocity[id]) + "km/h", (int(bbox[2]), int(bbox[3])), 0, 5e-3 * 150,
                            (255, 0, 255), 2)


    def entering_check(self, fps, fcnt, id, center, frame, bbox):
        if id not in self.section:  
            if is_crossed(id, center, self.startLine[0], self.startLine[1]):
                self.section[id] = 3
                self.direction[id] = 1
            else:  
                self.section[id] = 1
                self.direction[id] = -1
        else:
            self.section_check(fps, fcnt, id, center, frame, bbox)