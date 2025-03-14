import base64

class BB64U8:
    def __intit__(self):
        self.binary_img = ""
        self.base64_img = ""

        # Use for printing on the screen
        self.utf8_img = ""

        self.decode_img = ""

    def encode(self, img_path, option=1):
        # Validate the option
        if option not in (0, 1):
            raise ValueError("Invalid option! Use 0 for binary conversion only or 1 for full conversion.")

        with open(img_path, "rb") as img_file:
            # Read the image as binary data
            self.binary_img = img_file.read()

            # Convert only binary
            if option == 0:
                self.base64_img = None
                self.utf8_img = None

            # Convert binary, Base64, and UTF-8 (select by default)
            elif option == 1:
                # Encode the binary image data to Base64 (byte)
                # * NOT FOR PRINTING * #
                self.base64_img = base64.b64encode(self.binary_img)
                # Convert Base64 (byte) to string format
                # * FOR PRINTING * #
                self.utf8_img = self.base64_img.decode("utf-8")

    def saveTextImg(self, file_path, textImage, EOF=None):
        with open(file_path, "wb") as file:
            file.write(textImage)
            if EOF is not None:
                file.write(EOF.encode('utf-8'))

    def decode(self, save_path, encodedImg):
        # Decode the Base64 back to binary data
        self.decode_img = base64.b64decode(encodedImg)

        # Save the decoded image to verify
        with open(save_path, "wb") as file:
            file.write(self.decode_img)
