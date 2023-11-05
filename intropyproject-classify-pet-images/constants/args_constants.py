__all__ = ["ArgsConstants"]

class ArgsConstants():
    DIR_FLAG = '--dir'
    DIR_DEFAULT = 'pet_images/'
    DIR_HELP = 'path to folder of images'

    ARCH_FLAG = '--arch'
    ARCH_DEFAULT = 'vgg'
    ARCH_HELP = 'which CNN architecture would you like?'

    DOGFILE_FLAG = '--dogfile'
    DOGFILE_DEFAULT = 'dognames.txt'
    DOGFILE_HELP = 'path to dognames file'
