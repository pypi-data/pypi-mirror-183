import numpy, base64, cv2
class ImageConverter:
    @staticmethod 
    def numpy2bytes(numpy_image : numpy.ndarray, encoding : str = ".jpg") -> bytes:
        return cv2.imencode(encoding, numpy_image)[1].tobytes()
    @staticmethod 
    def bytes2string(byte_image : bytes, encoding : str = "ascii") -> str:
        return base64.b64encode(byte_image).decode(encoding)
    @staticmethod 
    def string2bytes(string_image : str) -> bytes:
        return base64.b64decode(string_image)
    @staticmethod 
    def bytes2numpy(byte_image  : bytes, 
                    np_encoding :   int = numpy.uint8, 
                    cv_encoding :   int = cv2.IMREAD_COLOR) -> numpy.ndarray:
        return cv2.imdecode(numpy.frombuffer(byte_image, np_encoding), cv_encoding)