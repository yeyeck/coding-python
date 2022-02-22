import math
from numpy import inner


def iou(bboxA, bboxB):
    x1 = max(bboxA[1], bboxB[1])
    y1 = max(bboxA[2], bboxB[2])

    x2 = min(bboxA[3], bboxB[3])
    y2 = min(bboxA[4], bboxB[4])

    a = (bboxA[3] - bboxA[1]) * (bboxA[4] - bboxA[2])
    b = (bboxB[3] - bboxB[1]) * (bboxB[4] - bboxB[2])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    outer = a + b - inter

    return inter / outer

def giou(bboxA, bboxB):
    # caculate iou
    x1 = max(bboxA[1], bboxB[1])
    y1 = max(bboxA[2], bboxB[2])

    x2 = min(bboxA[3], bboxB[3])
    y2 = min(bboxA[4], bboxB[4])

    a = (bboxA[3] - bboxA[1]) * (bboxA[4] - bboxA[2])
    b = (bboxB[3] - bboxB[1]) * (bboxB[4] - bboxB[2])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    outer = a + b - inter
    iou = inter / outer

    # caculate c
    cx1 = min(bboxA[1], bboxB[1])
    cy1 = min(bboxA[2], bboxB[2])

    cx2 = max(bboxA[3], bboxB[3])
    cy2 = max(bboxA[4], bboxB[4])

    c = (cx2 - cx1) * (cy2 - cy1)

    # caculate giou
    return iou - (c - inter) / c

def diou(bboxA, bboxB):
     # caculate iou
    x1 = max(bboxA[1], bboxB[1])
    y1 = max(bboxA[2], bboxB[2])

    x2 = min(bboxA[3], bboxB[3])
    y2 = min(bboxA[4], bboxB[4])

    a = (bboxA[3] - bboxA[1]) * (bboxA[4] - bboxA[2])
    b = (bboxB[3] - bboxB[1]) * (bboxB[4] - bboxB[2])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    outer = a + b - inter
    iou = inter / outer

    # caculate p
    cxA = (bboxA[1] + bboxA[3]) / 2
    cyA = (bboxA[2] + bboxA[4]) / 2
    
    cxB = (bboxB[1] + bboxB[3]) / 2
    cyB = (bboxB[2] + bboxB[4]) / 2
    
    interd_x = cxB - cxA
    interd_y = cyB - cyA
    p = interd_x * interd_x + interd_y * interd_y
    
    # caculate c
    cx1 = min(bboxA[1], bboxB[1])
    cy1 = min(bboxA[2], bboxB[2])

    cx2 = max(bboxA[3], bboxB[3])
    cy2 = max(bboxA[4], bboxB[4])
    
    cw = cx2 - cx1
    ch = cy2 - cy1
    cl2 =   cw * cw + ch * ch

    # caculate diou
    return iou - p / cl2


def nms(bboxes, iou_thres):
    bboxes = sorted(bboxes, key=lambda x: x[0], reverse=True)
    results = []
    while bboxes:
        bbox = bboxes.pop(0)
        results.append(bbox)
        for i, bbox_ in enumerate(bboxes):
            if iou(bbox, bbox_) > iou_thres:
                bboxes.pop(i)
    return results


def soft_nms(bboxes, iou_thres):
    pass

if __name__ == '__main__':
    # bbox1 = [0.6, 20, 40, 60, 80]
    bbox2 = [0.2, 200, 300, 300, 500]
    bbox3 = [0.4, 255, 200, 333, 555]
    # bboxes = [bbox1, bbox2, bbox3]
    # bboxes = sorted(bboxes, key=lambda x: x[0], reverse=True)
    # bboxes = nms(bboxes, 0.1)
    # print(bboxes)
    print(f'iou: {iou(bbox3, bbox2)}')
    print(f'giou: {giou(bbox3, bbox2)}')
    print(f'diou: {diou(bbox3, bbox2)}')

    
