from Module.bb64u8 import BB64U8

bb64u8 = BB64U8()

bb64u8.encode('path_of_imgage_to_encode.jpg')
bb64u8.saveTextImg('path_to_save_encode.txt', bb64u8.base64_img)

print("UTF-8")
print(bb64u8.utf8_img)

bb64u8.decode('path_to_save_decode_img.png', bb64u8.base64_img)
