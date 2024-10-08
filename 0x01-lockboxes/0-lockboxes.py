#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked_boxes = set([0])
    keys = [0]
    
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.add(key)
                keys.append(key)

    return len(unlocked_boxes) == len(boxes)
