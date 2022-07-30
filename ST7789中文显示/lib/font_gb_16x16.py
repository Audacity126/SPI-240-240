class Font:
    def __init__(self, size):
        self.WIDTH = size
        self.HEIGHT = size
        self.SIZE = size * (size // 8)


class Font32(Font):
    def __init__(self,size):
        Font.__init__(self,size)
        self.FONT = {
        '℃': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f,
              0x80, 0x00, 0x00, 0x1f, 0xc3, 0xff, 0x00, 0x1d, 0xc7, 0xff, 0xb0, 0x1d, 0xcf, 0x83, 0xf0, 0x1d, 0xde,
              0x00, 0xf0, 0x1f, 0xfc, 0x00, 0x70, 0x07, 0x3c, 0x00, 0x70, 0x00, 0x78, 0x00, 0x30, 0x00, 0x78, 0x00,
              0x30, 0x00, 0x78, 0x00, 0x30, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00,
              0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00,
              0x3c, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x30, 0x00, 0x3e, 0x00, 0x70, 0x00, 0x1f, 0x01, 0xe0, 0x00, 0x0f,
              0x87, 0xc0, 0x00, 0x07, 0xff, 0x80, 0x00, 0x03, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        '睢': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xee, 0x00, 0x00, 0x01, 0xf7, 0x80, 0x38,
              0xf1, 0xe7, 0x80, 0x3f, 0xf1, 0xc7, 0x98, 0x38, 0xf3, 0xc3, 0xbc, 0x38, 0xe3, 0xff, 0xfe, 0x38, 0xe7,
              0x87, 0x00, 0x38, 0xe7, 0x87, 0x00, 0x38, 0xe7, 0x87, 0x00, 0x38, 0xef, 0x87, 0x30, 0x3f, 0xef, 0x87,
              0x78, 0x38, 0xff, 0xff, 0xfc, 0x38, 0xfb, 0x87, 0x00, 0x38, 0xfb, 0x87, 0x00, 0x38, 0xe3, 0x87, 0x00,
              0x38, 0xe3, 0x87, 0x00, 0x3f, 0xe3, 0x87, 0x30, 0x38, 0xe3, 0x87, 0x78, 0x38, 0xe3, 0xff, 0xfc, 0x38,
              0xe3, 0x87, 0x00, 0x38, 0xe3, 0x87, 0x00, 0x38, 0xe3, 0x87, 0x00, 0x38, 0xe3, 0x87, 0x00, 0x3f, 0xe3,
              0x87, 0x18, 0x38, 0xe3, 0x87, 0x3c, 0x38, 0xe3, 0xff, 0xfe, 0x38, 0xc3, 0x80, 0x00, 0x30, 0x03, 0x80,
              0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00],
        '县': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xc0, 0x07, 0x00, 0x01, 0xff, 0xff, 0x80, 0x01,
              0xe0, 0x07, 0x80, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xff,
              0xff, 0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xe0, 0x07,
              0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xff, 0xff, 0x00, 0x01, 0xe0, 0x07, 0x00, 0x01, 0xe0, 0x07, 0x00,
              0x01, 0xe0, 0x07, 0x18, 0x01, 0xe0, 0x07, 0x3c, 0x7f, 0xff, 0xff, 0xfe, 0x78, 0x0e, 0x00, 0x00, 0x00,
              0x0f, 0x00, 0x00, 0x00, 0x1f, 0x80, 0x00, 0x00, 0x3e, 0x1c, 0x00, 0x00, 0x78, 0x1f, 0x00, 0x00, 0xf0,
              0x07, 0xc0, 0x03, 0xe0, 0x03, 0xe0, 0x07, 0x80, 0x03, 0xf0, 0x0f, 0xff, 0xff, 0xf0, 0x0f, 0xff, 0x80,
              0xf0, 0x07, 0x80, 0x00, 0x70, 0x00, 0x00, 0x00, 0x00],
        '当': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x00, 0x03, 0xe0, 0x00, 0x0e,
              0x03, 0xc1, 0xc0, 0x0f, 0x83, 0xc3, 0xe0, 0x07, 0xc3, 0xc3, 0xe0, 0x03, 0xe3, 0xc7, 0xc0, 0x01, 0xf3,
              0xcf, 0x00, 0x00, 0xf3, 0xce, 0x00, 0x00, 0xf3, 0xdc, 0x00, 0x00, 0x03, 0xf8, 0x00, 0x00, 0x03, 0xc0,
              0x78, 0x1f, 0xff, 0xff, 0xfc, 0x0e, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78,
              0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x07, 0xff, 0xff, 0xf8, 0x03,
              0x80, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00,
              0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x1f, 0xff, 0xff, 0xf8, 0x1e, 0x00, 0x00,
              0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x00],
        '前': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x0e, 0x00, 0x00, 0x78, 0x0f, 0x00, 0x00,
              0x7c, 0x1f, 0x00, 0x00, 0x3c, 0x1c, 0x00, 0x00, 0x3c, 0x38, 0x38, 0x00, 0x1c, 0x70, 0x7c, 0x7f, 0xff,
              0xff, 0xfe, 0x38, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00, 0xe0, 0x0e, 0x0f, 0x00, 0xf0, 0x0f, 0xff, 0x3c,
              0xe0, 0x0f, 0x0e, 0x3c, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0,
              0x0f, 0xfe, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f,
              0xfe, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e, 0x38, 0xe0, 0x0f, 0x0e,
              0x3c, 0xe0, 0x0f, 0x0e, 0x30, 0xe0, 0x0f, 0x0e, 0x3d, 0xe0, 0x0f, 0x7e, 0x3f, 0xe0, 0x0f, 0x3e, 0x07,
              0xc0, 0x0f, 0x1c, 0x03, 0xc0, 0x00, 0x00, 0x00, 0x00],
        '天': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xc0, 0x00,
              0x00, 0x03, 0xe0, 0x0f, 0xff, 0xff, 0xf0, 0x07, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03,
              0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x07, 0x80, 0x00, 0x00, 0x07, 0x80, 0x00, 0x00, 0x07, 0x80,
              0x70, 0x00, 0x07, 0x80, 0xf8, 0x7f, 0xff, 0xff, 0xfc, 0x38, 0x07, 0xe0, 0x00, 0x00, 0x07, 0xe0, 0x00,
              0x00, 0x0f, 0x60, 0x00, 0x00, 0x0f, 0x70, 0x00, 0x00, 0x0e, 0x70, 0x00, 0x00, 0x1e, 0x38, 0x00, 0x00,
              0x1e, 0x3c, 0x00, 0x00, 0x3c, 0x1c, 0x00, 0x00, 0x78, 0x1e, 0x00, 0x00, 0x78, 0x0f, 0x00, 0x00, 0xf0,
              0x07, 0xc0, 0x01, 0xe0, 0x07, 0xe0, 0x07, 0xc0, 0x03, 0xfc, 0x0f, 0x00, 0x01, 0xfe, 0x3e, 0x00, 0x00,
              0x7c, 0x78, 0x00, 0x00, 0x38, 0x00, 0x00, 0x00, 0x00],
        '气': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x00, 0x00, 0x01, 0xf0, 0x00, 0x00, 0x01,
              0xf0, 0x00, 0x00, 0x01, 0xe0, 0x00, 0x60, 0x03, 0xc0, 0x00, 0xf0, 0x03, 0xff, 0xff, 0xf8, 0x07, 0x80,
              0x03, 0x00, 0x07, 0x80, 0x07, 0x80, 0x0f, 0xff, 0xff, 0xc0, 0x0e, 0x70, 0x00, 0x00, 0x1e, 0x00, 0x00,
              0x00, 0x3c, 0x00, 0x07, 0x00, 0x3f, 0xff, 0xff, 0x80, 0x77, 0x80, 0x07, 0x00, 0x60, 0x00, 0x07, 0x00,
              0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00,
              0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x07, 0x8c, 0x00, 0x00, 0x07, 0x8c, 0x00, 0x00,
              0x03, 0x9c, 0x00, 0x00, 0x03, 0xdc, 0x00, 0x00, 0x03, 0xfc, 0x00, 0x00, 0x01, 0xfc, 0x00, 0x00, 0x00,
              0xfc, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x00, 0x00],
        '阴': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1c, 0x19, 0xc0, 0x70, 0x1f, 0xff, 0xff, 0xf8, 0x1c,
              0x3d, 0xe0, 0x78, 0x1c, 0x39, 0xe0, 0x70, 0x1c, 0x79, 0xe0, 0x70, 0x1c, 0x71, 0xe0, 0x70, 0x1c, 0x71,
              0xe0, 0x70, 0x1c, 0xe1, 0xe0, 0x70, 0x1c, 0xe1, 0xff, 0xf0, 0x1c, 0xc1, 0xe0, 0x70, 0x1c, 0xe1, 0xe0,
              0x70, 0x1c, 0x71, 0xe0, 0x70, 0x1c, 0x39, 0xe0, 0x70, 0x1c, 0x3d, 0xe0, 0x70, 0x1c, 0x1d, 0xe0, 0x70,
              0x1c, 0x1d, 0xff, 0xf0, 0x1c, 0x1d, 0xe0, 0x70, 0x1f, 0x3d, 0xe0, 0x70, 0x1f, 0xfd, 0xc0, 0x70, 0x1c,
              0xfd, 0xc0, 0x70, 0x1c, 0x7b, 0xc0, 0x70, 0x1c, 0x03, 0xc0, 0x70, 0x1c, 0x03, 0x80, 0x70, 0x1c, 0x07,
              0x80, 0x70, 0x1c, 0x0f, 0x00, 0x70, 0x1c, 0x1e, 0x0f, 0xf0, 0x1c, 0x3c, 0x07, 0xf0, 0x1c, 0x78, 0x01,
              0xf0, 0x1c, 0xe0, 0x00, 0xe0, 0x00, 0x00, 0x00, 0x00],
        '多': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x00, 0x03, 0xe0, 0x00, 0x00,
              0x07, 0xc0, 0x00, 0x00, 0x0f, 0x00, 0xe0, 0x00, 0x3f, 0xff, 0xf0, 0x00, 0x7c, 0x03, 0xf0, 0x00, 0xfe,
              0x07, 0xc0, 0x03, 0xef, 0x0f, 0x80, 0x0f, 0x8f, 0x1f, 0x00, 0x1e, 0x07, 0x7e, 0x00, 0x18, 0x07, 0xf8,
              0x00, 0x00, 0x03, 0xf0, 0x00, 0x00, 0x0f, 0xc0, 0x00, 0x00, 0x7f, 0xf0, 0x00, 0x07, 0xfb, 0xf0, 0x00,
              0x3f, 0x87, 0xc0, 0x78, 0x30, 0x0f, 0xff, 0xfc, 0x00, 0x1f, 0x00, 0xfc, 0x00, 0x7c, 0x01, 0xf0, 0x01,
              0xfe, 0x03, 0xe0, 0x03, 0xef, 0x07, 0xc0, 0x0f, 0x87, 0x8f, 0x80, 0x0c, 0x07, 0xbf, 0x00, 0x00, 0x07,
              0xfc, 0x00, 0x00, 0x03, 0xf8, 0x00, 0x00, 0x0f, 0xe0, 0x00, 0x00, 0x7f, 0x80, 0x00, 0x07, 0xfc, 0x00,
              0x00, 0x3f, 0xc0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        '云': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x01, 0xc0, 0x00, 0x00, 0x03, 0xe0, 0x07, 0xff, 0xff, 0xe0, 0x03, 0x80, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x38, 0x00, 0x00, 0x00, 0x7c, 0x7f, 0xff, 0xff, 0xfe, 0x38, 0x07, 0x80, 0x00, 0x00, 0x0f, 0x00, 0x00,
              0x00, 0x0f, 0x00, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x00, 0x1e, 0x18, 0x00, 0x00, 0x3c, 0x1c, 0x00, 0x00,
              0x78, 0x0e, 0x00, 0x00, 0x78, 0x0f, 0x80, 0x00, 0xf0, 0x07, 0xc0, 0x01, 0xe0, 0x03, 0xe0, 0x03, 0xc0,
              0x03, 0xe0, 0x0f, 0xff, 0xff, 0xf0, 0x0f, 0xff, 0xff, 0xf0, 0x07, 0xfe, 0x00, 0xf0, 0x07, 0x80, 0x00,
              0xe0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        '晴': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x00, 0x1e, 0x30, 0x00,
              0x00, 0x1c, 0x78, 0x38, 0xff, 0xff, 0xfc, 0x3f, 0xfc, 0x1c, 0x00, 0x38, 0xf0, 0x1c, 0x00, 0x38, 0xe0,
              0x1c, 0xf0, 0x38, 0xe7, 0xff, 0xf8, 0x38, 0xe3, 0x1c, 0x00, 0x38, 0xe0, 0x1c, 0x18, 0x38, 0xe0, 0x1c,
              0x3c, 0x38, 0xff, 0xff, 0xfe, 0x3f, 0xfc, 0x00, 0x00, 0x38, 0xe7, 0x00, 0xf0, 0x38, 0xe3, 0xff, 0xf0,
              0x38, 0xe3, 0x80, 0xf0, 0x38, 0xe3, 0x80, 0xe0, 0x38, 0xe3, 0xff, 0xe0, 0x38, 0xe3, 0x80, 0xe0, 0x38,
              0xe3, 0x80, 0xe0, 0x3f, 0xe3, 0x80, 0xe0, 0x38, 0xe3, 0xff, 0xe0, 0x38, 0xe3, 0x80, 0xe0, 0x38, 0xe3,
              0x80, 0xe0, 0x30, 0x03, 0x80, 0xe0, 0x00, 0x03, 0x80, 0xe0, 0x00, 0x03, 0x8f, 0xe0, 0x00, 0x03, 0x87,
              0xe0, 0x00, 0x07, 0x01, 0xe0, 0x00, 0x00, 0x00, 0x00],
        '雨': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x00,
              0x00, 0x00, 0x78, 0x3f, 0xff, 0xff, 0xfc, 0x1c, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03,
              0x80, 0x00, 0x0e, 0x03, 0x80, 0xf0, 0x0f, 0xff, 0xff, 0xf8, 0x0e, 0x03, 0x80, 0xf0, 0x0f, 0xc3, 0xa0,
              0xf0, 0x0f, 0xf3, 0xf8, 0xf0, 0x0e, 0xfb, 0xbe, 0xf0, 0x0e, 0x7f, 0x9e, 0xf0, 0x0e, 0x3f, 0x8e, 0xf0,
              0x0e, 0x3b, 0x8e, 0xf0, 0x0e, 0x1b, 0x86, 0xf0, 0x0f, 0x83, 0x80, 0xf0, 0x0f, 0xe3, 0xf8, 0xf0, 0x0e,
              0xfb, 0xbe, 0xf0, 0x0e, 0x7b, 0x9e, 0xf0, 0x0e, 0x3b, 0x8f, 0xf0, 0x0e, 0x3b, 0x8f, 0xf0, 0x0e, 0x1b,
              0x86, 0xf0, 0x0e, 0x03, 0x80, 0xf0, 0x0e, 0x03, 0x9f, 0xf0, 0x0e, 0x03, 0x9f, 0xe0, 0x0e, 0x03, 0x83,
              0xe0, 0x0e, 0x03, 0x01, 0xc0, 0x00, 0x00, 0x00, 0x00],
        '大': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x00,
              0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03,
              0x80, 0x38, 0x00, 0x03, 0x80, 0x7c, 0x7f, 0xff, 0xff, 0xfe, 0x38, 0x03, 0x80, 0x00, 0x00, 0x03, 0xc0,
              0x00, 0x00, 0x03, 0xc0, 0x00, 0x00, 0x07, 0xc0, 0x00, 0x00, 0x07, 0xe0, 0x00, 0x00, 0x07, 0xe0, 0x00,
              0x00, 0x07, 0x70, 0x00, 0x00, 0x0f, 0x70, 0x00, 0x00, 0x0f, 0x78, 0x00, 0x00, 0x0e, 0x38, 0x00, 0x00,
              0x1e, 0x1c, 0x00, 0x00, 0x1c, 0x1e, 0x00, 0x00, 0x3c, 0x0f, 0x00, 0x00, 0x78, 0x07, 0x80, 0x00, 0xf0,
              0x07, 0xe0, 0x01, 0xe0, 0x03, 0xf0, 0x03, 0xc0, 0x01, 0xfe, 0x0f, 0x80, 0x00, 0xfe, 0x3e, 0x00, 0x00,
              0x38, 0x78, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        '小': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0x01, 0xe0, 0x00, 0x00,
              0x01, 0xe0, 0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0x01,
              0xc0, 0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0xf1, 0xcc, 0x00, 0x00, 0xf9, 0xce, 0x00, 0x00, 0xf9, 0xc7,
              0x00, 0x01, 0xf1, 0xc7, 0x80, 0x01, 0xe1, 0xc3, 0xe0, 0x03, 0xc1, 0xc1, 0xf0, 0x03, 0xc1, 0xc0, 0xf0,
              0x07, 0x81, 0xc0, 0xf8, 0x07, 0x01, 0xc0, 0x7c, 0x0f, 0x01, 0xc0, 0x7c, 0x1e, 0x01, 0xc0, 0x3c, 0x1c,
              0x01, 0xc0, 0x3c, 0x38, 0x01, 0xc0, 0x1c, 0x70, 0x01, 0xc0, 0x00, 0x00, 0x01, 0xc0, 0x00, 0x00, 0x01,
              0xc0, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x00, 0x7f, 0xc0, 0x00, 0x00, 0x3f, 0xc0, 0x00, 0x00, 0x0f, 0x80,
              0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        '中': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x00,
              0x03, 0xc0, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x20, 0x0c, 0x03,
              0x80, 0x78, 0x0f, 0xff, 0xff, 0xf8, 0x0e, 0x03, 0x80, 0x70, 0x0e, 0x03, 0x80, 0x70, 0x0e, 0x03, 0x80,
              0x70, 0x0e, 0x03, 0x80, 0x70, 0x0e, 0x03, 0x80, 0x70, 0x0e, 0x03, 0x80, 0x70, 0x0e, 0x03, 0x80, 0x70,
              0x0e, 0x03, 0x80, 0x70, 0x0f, 0xff, 0xff, 0xf0, 0x0e, 0x03, 0x80, 0x70, 0x0e, 0x03, 0x80, 0x70, 0x1c,
              0x03, 0x80, 0x60, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03,
              0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x03, 0x80,
              0x00, 0x00, 0x03, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00],
        '阵': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x78, 0x00, 0x38,
              0x78, 0x78, 0x00, 0x3f, 0xf8, 0x70, 0x30, 0x3c, 0x78, 0xf0, 0x78, 0x3c, 0xff, 0xff, 0xfc, 0x3c, 0xee,
              0xe0, 0x00, 0x3c, 0xe0, 0xe0, 0x00, 0x3d, 0xc1, 0xec, 0x00, 0x3d, 0xc1, 0xcf, 0x00, 0x3d, 0x83, 0xce,
              0x00, 0x3d, 0x83, 0xce, 0x00, 0x3d, 0xc3, 0x8e, 0x30, 0x3c, 0xe7, 0x8e, 0x78, 0x3c, 0xff, 0xff, 0xfc,
              0x3c, 0x77, 0xfe, 0x00, 0x3c, 0x78, 0x0e, 0x00, 0x3c, 0x78, 0x0e, 0x00, 0x3c, 0x78, 0x0e, 0x18, 0x3f,
              0xf8, 0x0e, 0x3c, 0x3f, 0xff, 0xff, 0xfe, 0x3d, 0xff, 0xfe, 0x00, 0x3d, 0xc0, 0x0e, 0x00, 0x3c, 0x00,
              0x0e, 0x00, 0x3c, 0x00, 0x0e, 0x00, 0x3c, 0x00, 0x0e, 0x00, 0x3c, 0x00, 0x0e, 0x00, 0x3c, 0x00, 0x0e,
              0x00, 0x3c, 0x00, 0x0e, 0x00, 0x00, 0x00, 0x00, 0x00],
        '雾': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x80, 0x03, 0xff, 0xff, 0xc0, 0x01,
              0xc3, 0xc0, 0x00, 0x06, 0x03, 0xc0, 0x38, 0x0f, 0xff, 0xff, 0xfc, 0x0e, 0x03, 0xc0, 0x7c, 0x1f, 0xff,
              0xff, 0xf0, 0x3e, 0x03, 0xc0, 0xe0, 0x19, 0xff, 0xff, 0x80, 0x00, 0x03, 0xc0, 0x00, 0x00, 0x3b, 0x80,
              0x00, 0x00, 0x7c, 0x0f, 0x00, 0x00, 0xff, 0xff, 0x80, 0x01, 0xf8, 0x1f, 0x80, 0x03, 0xdc, 0x3c, 0x00,
              0x0f, 0x0f, 0xf0, 0x00, 0x0e, 0x07, 0xf0, 0x00, 0x00, 0x3f, 0xff, 0xfe, 0x01, 0xff, 0x3f, 0xfe, 0x1f,
              0xe7, 0x87, 0xf8, 0x7c, 0x07, 0x83, 0x80, 0x03, 0xff, 0xff, 0xc0, 0x01, 0xcf, 0x03, 0x80, 0x00, 0x0f,
              0x07, 0x80, 0x00, 0x1e, 0x07, 0x00, 0x00, 0x3c, 0x07, 0x00, 0x00, 0xf8, 0xff, 0x00, 0x07, 0xe0, 0x7e,
              0x00, 0x3f, 0x00, 0x3e, 0x00, 0x00, 0x00, 0x00, 0x00],
        '': [],
        '': [],

    }
class Font48(Font):
    def __init__(self,size):
        Font.__init__(self,size)
        self.WIDTH = 24
        self.SIZE = 144
        self.FONT = {
            '1': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0c, 0x00, 0x00, 0x1c, 0x00, 0x00, 0xfc, 0x00, 0x07,
                  0xfc, 0x00, 0x07, 0xfc, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
                  0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c,
                  0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00,
                  0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00,
                  0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x7e, 0x00, 0x07, 0xff,
                  0xf0, 0x07, 0xff, 0xf0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '2': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x80, 0x07, 0xff, 0xe0, 0x0f, 0x83, 0xf0, 0x1f,
                  0x01, 0xf0, 0x1e, 0x00, 0xf8, 0x1e, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x3f, 0x00, 0x78, 0x3f, 0x00, 0x78,
                  0x3f, 0x00, 0x78, 0x1f, 0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0, 0x00, 0x03,
                  0xf0, 0x00, 0x03, 0xe0, 0x00, 0x07, 0xc0, 0x00, 0x0f, 0x80, 0x00, 0x1f, 0x00, 0x00, 0x3e, 0x00, 0x00,
                  0x7c, 0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0, 0x00, 0x03, 0xe0, 0x00, 0x03, 0xc0, 0x00, 0x07, 0x80, 0x1c,
                  0x0f, 0x00, 0x1c, 0x1f, 0x00, 0x38, 0x3e, 0x00, 0x38, 0x3c, 0x00, 0xf8, 0x3f, 0xff, 0xf8, 0x3f, 0xff,
                  0xf8, 0x3f, 0xff, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '3': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x0f, 0x87, 0xe0, 0x1e,
                  0x03, 0xe0, 0x1e, 0x01, 0xf0, 0x1e, 0x01, 0xf0, 0x1f, 0x00, 0xf0, 0x1f, 0x00, 0xf0, 0x1f, 0x00, 0xf0,
                  0x00, 0x00, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x01, 0xf0, 0x00, 0x03, 0xe0, 0x00, 0x07, 0xc0, 0x00, 0x3f,
                  0x80, 0x00, 0xff, 0x00, 0x00, 0xff, 0xc0, 0x00, 0x07, 0xe0, 0x00, 0x01, 0xf0, 0x00, 0x00, 0xf8, 0x00,
                  0x00, 0xf8, 0x00, 0x00, 0x78, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x1e, 0x00, 0x7c, 0x3f, 0x00, 0x7c,
                  0x3f, 0x00, 0x7c, 0x3f, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x1e, 0x01, 0xf0, 0x1f, 0x83, 0xe0, 0x0f, 0xff,
                  0xc0, 0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '4': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00,
                  0x0f, 0xc0, 0x00, 0x0f, 0xc0, 0x00, 0x1f, 0xc0, 0x00, 0x3f, 0xc0, 0x00, 0x3f, 0xc0, 0x00, 0x7f, 0xc0,
                  0x00, 0xf7, 0xc0, 0x00, 0xe7, 0xc0, 0x01, 0xe7, 0xc0, 0x01, 0xc7, 0xc0, 0x03, 0xc7, 0xc0, 0x07, 0x87,
                  0xc0, 0x07, 0x07, 0xc0, 0x0f, 0x07, 0xc0, 0x1e, 0x07, 0xc0, 0x1c, 0x07, 0xc0, 0x3c, 0x07, 0xc0, 0x38,
                  0x07, 0xc0, 0x7f, 0xff, 0xfe, 0x7f, 0xff, 0xfe, 0x7f, 0xff, 0xfe, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0,
                  0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x07, 0xc0, 0x00, 0x7f,
                  0xfe, 0x00, 0x7f, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '5': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0xff, 0xf8, 0x0f, 0xff, 0xf8, 0x0f, 0xff, 0xf8, 0x0e,
                  0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00,
                  0x0e, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x0e, 0x3f, 0x00, 0x0f, 0xff, 0xc0, 0x0f, 0xff, 0xe0, 0x0f, 0xc3,
                  0xf0, 0x1f, 0x01, 0xf0, 0x1e, 0x00, 0xf8, 0x1e, 0x00, 0xf8, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00,
                  0x00, 0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x7c, 0x1e, 0x00, 0x7c, 0x3f, 0x00, 0x7c, 0x3f, 0x00, 0x78,
                  0x3f, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x1e, 0x01, 0xf0, 0x0f, 0x83, 0xe0, 0x07, 0xff,
                  0xc0, 0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '6': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7f, 0xc0, 0x01, 0xff, 0xe0, 0x03, 0xe1, 0xf0, 0x07,
                  0xc1, 0xf8, 0x0f, 0x81, 0xf8, 0x0f, 0x01, 0xf8, 0x1f, 0x00, 0xf0, 0x1f, 0x00, 0x00, 0x1e, 0x00, 0x00,
                  0x3e, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x3e, 0x7f, 0xc0, 0x3f, 0xff, 0xe0, 0x3f, 0xff,
                  0xf0, 0x3f, 0xc1, 0xf8, 0x3f, 0x80, 0xf8, 0x3f, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e,
                  0x00, 0x3c, 0x3e, 0x00, 0x3c, 0x3e, 0x00, 0x3c, 0x3e, 0x00, 0x3c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c,
                  0x1f, 0x00, 0x7c, 0x1f, 0x00, 0x7c, 0x0f, 0x80, 0x78, 0x0f, 0xc0, 0xf8, 0x07, 0xe1, 0xf0, 0x03, 0xff,
                  0xe0, 0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '7': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1f, 0xff, 0xfc, 0x1f, 0xff, 0xfc, 0x1f, 0xff, 0xf8, 0x1f,
                  0x00, 0x78, 0x1e, 0x00, 0x70, 0x1c, 0x00, 0xf0, 0x38, 0x00, 0xe0, 0x38, 0x01, 0xe0, 0x00, 0x01, 0xc0,
                  0x00, 0x03, 0xc0, 0x00, 0x03, 0x80, 0x00, 0x07, 0x80, 0x00, 0x07, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f,
                  0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x3e, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x3c, 0x00, 0x00,
                  0x7c, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x78, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00,
                  0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xf8,
                  0x00, 0x00, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '8': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x80, 0x07, 0xff, 0xe0, 0x0f, 0x83, 0xf0, 0x1f,
                  0x00, 0xf0, 0x1e, 0x00, 0xf8, 0x3e, 0x00, 0x78, 0x3c, 0x00, 0x7c, 0x3c, 0x00, 0x7c, 0x3e, 0x00, 0x7c,
                  0x3e, 0x00, 0x78, 0x3f, 0x00, 0x78, 0x1f, 0x80, 0xf8, 0x1f, 0xe0, 0xf0, 0x0f, 0xf3, 0xe0, 0x07, 0xff,
                  0xc0, 0x01, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x0f, 0x9f, 0xe0, 0x1f, 0x0f, 0xf0, 0x1e, 0x03, 0xf8, 0x3e,
                  0x01, 0xf8, 0x3c, 0x00, 0xfc, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c, 0x78, 0x00, 0x3c, 0x7c, 0x00, 0x3c,
                  0x7c, 0x00, 0x7c, 0x3c, 0x00, 0x7c, 0x3e, 0x00, 0x78, 0x1f, 0x00, 0xf8, 0x0f, 0x83, 0xf0, 0x07, 0xff,
                  0xe0, 0x01, 0xff, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '9': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0xff, 0x00, 0x07, 0xff, 0xc0, 0x0f, 0x83, 0xe0, 0x1f,
                  0x01, 0xf0, 0x1e, 0x00, 0xf0, 0x3e, 0x00, 0xf8, 0x3e, 0x00, 0xf8, 0x3c, 0x00, 0x78, 0x7c, 0x00, 0x7c,
                  0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0x7c, 0x7c, 0x00, 0xfc, 0x3e, 0x00,
                  0xfc, 0x3e, 0x01, 0xfc, 0x3f, 0x03, 0xfc, 0x1f, 0x87, 0xfc, 0x1f, 0xff, 0xfc, 0x07, 0xff, 0x7c, 0x03,
                  0xfc, 0x7c, 0x00, 0x00, 0xfc, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00, 0x00, 0xf8, 0x00, 0x01, 0xf0,
                  0x0f, 0x01, 0xf0, 0x1f, 0x01, 0xe0, 0x1f, 0x03, 0xe0, 0x1f, 0x07, 0xc0, 0x1f, 0x8f, 0x80, 0x0f, 0xff,
                  0x00, 0x07, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '0': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x00, 0x03, 0xff, 0xc0, 0x07, 0xe7, 0xe0, 0x07,
                  0xc3, 0xe0, 0x0f, 0x81, 0xf0, 0x1f, 0x80, 0xf0, 0x1f, 0x00, 0xf8, 0x1f, 0x00, 0xf8, 0x3e, 0x00, 0xf8,
                  0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00,
                  0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e,
                  0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0x7c, 0x3e, 0x00, 0xf8, 0x1f, 0x00, 0xf8,
                  0x1f, 0x00, 0xf8, 0x1f, 0x00, 0xf0, 0x0f, 0x81, 0xf0, 0x07, 0xc3, 0xe0, 0x07, 0xe7, 0xe0, 0x03, 0xff,
                  0xc0, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            ':': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0xfe, 0x00, 0x00, 0xfe, 0x00, 0x00, 0xfe, 0x00, 0x00, 0x7c,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0xfe, 0x00, 0x00, 0xfe, 0x00, 0x00, 0xfe,
                  0x00, 0x00, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '-': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x7f, 0xff, 0xfe, 0x7f, 0xff, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '/': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0e, 0x00, 0x00,
                  0x1e, 0x00, 0x00, 0x1c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00, 0x70, 0x00,
                  0x00, 0xf0, 0x00, 0x00, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xc0, 0x00, 0x03, 0xc0, 0x00, 0x03, 0x80,
                  0x00, 0x07, 0x80, 0x00, 0x07, 0x80, 0x00, 0x07, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0e, 0x00, 0x00, 0x1e,
                  0x00, 0x00, 0x1c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00, 0x70, 0x00, 0x00,
                  0xf0, 0x00, 0x00, 0xe0, 0x00, 0x01, 0xe0, 0x00, 0x01, 0xc0, 0x00, 0x03, 0xc0, 0x00, 0x03, 0x80, 0x00,
                  0x07, 0x80, 0x00, 0x07, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x1e, 0x00, 0x00, 0x1e, 0x00,
                  0x00, 0x1c, 0x00, 0x00, 0x3c, 0x00, 0x00, 0x38, 0x00, 0x00, 0x78, 0x00, 0x00, 0x70, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        }

if __name__ == '__main__':
    f32 = Font32(32)
    f48 = Font48(48)
    print(f32.SIZE)
    print(f48.WIDTH)

