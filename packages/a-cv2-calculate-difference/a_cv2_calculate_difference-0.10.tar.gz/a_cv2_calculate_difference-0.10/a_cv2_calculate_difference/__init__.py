from a_cv_imwrite_imread_plus import open_image_in_cv
import cv2
from a_cv2_imshow_thread import add_imshow_thread_to_cv2

add_imshow_thread_to_cv2()


def check_before_after(
    src, dst, show_results=True, return_image=False, color=(255, 0, 0)
):
    original = open_image_in_cv(src)
    new = open_image_in_cv(dst).copy()
    diff = original.copy()
    cv2.absdiff(original, new, diff)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    (T, thresh) = cv2.threshold(
        gray.copy(), 3, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )
    cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 2:
        cnts = cnts[0]
    elif len(cnts) == 3:
        cnts = cnts[1]
    boundingrect = []
    for cc in cnts:
        (x, y, w, h) = cv2.boundingRect(cc)
        boundingrect.append((x, y, w, h))
        if show_results or return_image:
            cv2.rectangle(new, (x, y), (x + w, y + h), tuple(reversed(color)), 2)
    if show_results:
        cv2.imshow_thread(new)
    if not return_image:
        return boundingrect
    else:
        return boundingrect, new

