from imagekit import ImageSpec
from imagekit.processors import ResizeToFit, Adjust


class HDSpec(ImageSpec):
    processors = [ResizeToFit(1024, 768)]
    format = 'JPEG'
    options = {'quality': 90}


class ThumbnailSpec(ImageSpec):
    processors = [Adjust(contrast=1.2, sharpness=1.1),
                  ResizeToFit(300, 200)]
    format = 'JPEG'
    options = {'quality': 90}
