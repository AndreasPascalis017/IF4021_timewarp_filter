import cv2

def capture_video():
    """Function to capture video from the default webcam and apply a timewarp filter."""
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return

    # Configuration
    threshold = 3  # Number of pixels to iterate
    is_upside_down = False  # Toggle for flipping the frame

    # Read the initial frame and validate
    ret, initial_frame = cap.read()
    if not ret:
        print("Error: Unable to read the initial frame from webcam.")
        cap.release()
        return

    # Create a copy of the initial frame for processing
    warped_frame = initial_frame.copy()
    temp_frame = initial_frame.copy()
    current_row = 0

    print(f"Frame dimensions: {initial_frame.shape}")

    while True:
        # Read the current frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read a frame from the webcam.")
            break

        # Flip the frame if needed
        frame = cv2.flip(frame, int(not is_upside_down))

        # Apply the timewarp filter logic
        temp_frame[current_row:current_row + threshold] = frame[current_row:current_row + threshold]
        warped_frame[:current_row] = temp_frame[:current_row]
        warped_frame[current_row:] = frame[current_row:]

        # Draw a green line to indicate the current row
        cv2.line(warped_frame, (0, current_row), (warped_frame.shape[1], current_row), (0, 255, 0), thickness=2)

        # Increment the current row by the threshold value
        current_row += threshold

        # Display the video with the timewarp effect
        cv2.imshow('Timewarp Filter', warped_frame)

        # Break the loop if the ESC key is pressed or the frame height is exceeded
        if cv2.waitKey(33) == 27 or current_row >= frame.shape[0]:
            break

    # Save the resulting image
    output_filename = 'timewarp_output.png'
    cv2.imwrite(output_filename, warped_frame)
    print(f"Timewarp filter applied and saved as '{output_filename}'.")

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

# Run the capture video function
if _name_ == "_main_":
    capture_video()