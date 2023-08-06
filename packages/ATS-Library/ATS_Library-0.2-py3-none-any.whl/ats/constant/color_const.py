from collections import namedtuple

Color = namedtuple('Color', "hex rgb cmyk hsl hsv")

# 红色
RED = Color(hex="#FF0000", rgb="255, 0, 0", cmyk="0, 100, 100, 0", hsl="0%, 100%, 50%", hsv="0, 100, 100")

# 绿色
GREEN = Color(hex="#00FF00", rgb="0, 255, 0", cmyk="100, 0, 100, 0", hsl="120, 100%, 50%", hsv="120, 100, 100")

# 蓝色
BLUE = Color(hex="#0000FF", rgb="0, 0, 255", cmyk="100, 100, 0, 0", hsl="240, 100%, 50%", hsv="240, 100, 100")

# 黄色
YELLOW = Color(hex="#FFFF00", rgb="255, 255, 0", cmyk="0, 0, 100, 0", hsl="60, 100%, 50%", hsv="60, 100, 100")

# 青色
CYAN = Color(hex="#00FFFF", rgb="0, 255, 255", cmyk="100, 0, 0, 0", hsl="180, 100%, 50%", hsv="180, 100, 100")

# 品红
MAGENTA = Color(hex="#FF00FF", rgb="255, 0, 255", cmyk="0, 100, 0, 0", hsl="300, 100%, 50%", hsv="300, 100, 100")

# 白色
WHITE = Color(hex="#FFFFFF", rgb="255, 255, 255", cmyk="0, 0, 0, 0", hsl="0, 0%, 100%", hsv="0, 0, 100")

# 黑色
BLACK = Color(hex="#000000", rgb="0, 0, 0", cmyk="0, 0, 0, 100", hsl="0, 0%, 0%", hsv="0, 0, 0")

# 灰色
GRAY = Color(hex="#808080", rgb="128, 128, 128", cmyk="0, 0, 0, 50", hsl="0, 0%, 50%", hsv="0, 0, 50")
