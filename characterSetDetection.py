#useful if you are seeing anomalies in your data processing, this will try to determine the character set you are working with.

from chardet.universaldetector import UniversalDetector

# Path to the file
file_path = r'C:\Users\yourfile.txt'

try:
    # Initialize the UniversalDetector
    detector = UniversalDetector()

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()

    # Retrieve the detected encoding
    encoding = detector.result['encoding']
    confidence = detector.result['confidence']

    if encoding:
        print(f"Detected encoding: {encoding} with confidence {confidence:.2f}")
    else:
        print("Encoding could not be detected.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
