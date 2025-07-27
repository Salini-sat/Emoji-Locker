


def detect_expression(landmarks, img_width, img_height):
    """
    Detect simple expressions like smile, surprise, wink from face mesh landmarks
    Returns: "Smile", "Wink", "Surprised", "Neutral"
    """

    # Get required points (indexes based on MediaPipe FaceMesh)
    left_eye = landmarks[159]  # Upper left eyelid
    right_eye = landmarks[386]  # Upper right eyelid
    mouth_top = landmarks[13]
    mouth_bottom = landmarks[14]

    # Convert to pixel coordinates
    def to_pixel(pt):
        return int(pt.x * img_width), int(pt.y * img_height)

    ly, ry = to_pixel(left_eye)[1], to_pixel(right_eye)[1]
    mt, mb = to_pixel(mouth_top)[1], to_pixel(mouth_bottom)[1]

    # Eye distance (for wink detection)
    eye_diff = abs(ly - ry)

    # Mouth openness
    mouth_gap = abs(mt - mb)

    if mouth_gap > 30:
        return "Surprised"
    elif eye_diff > 8:
        return "Wink"
    elif mouth_gap > 15:
        return "Smile"
    else:
        return "Neutral"
