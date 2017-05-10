import argparse
import textwrap
import sys


class ConsoleArgsParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(ConsoleArgsParser, self).__init__(*args, **kwargs)
        self.prog = 'Resizing Image'
        self.formatter_class = argparse.RawDescriptionHelpFormatter
        self.description = textwrap.dedent('''\
                      Script resizes your image.
                      It can be used for scaling or downgrading images in terminal. All
                      sizes are in pixels.\n
                      -----------------------------------------------------------------
                      If you want to stop the program press Ctrl+C.
                      ------------------------------------------------------------------
                      This program had been tested on Python 3.5.2.
                      ''')
        self.add_argument('input_filepath', nargs='?',
                          help='Paste full path to file, \
                          e.g /home/user/documents/test.jpg',
                          action='store')
        self.add_argument('output_filepath', nargs='?',
                          help='Specify the full path to folder and filename\
                              e.g /home/user/documents/test_200x100.jpg, \
                              else result will be shown in terminal window',
                          action='store', default='.')
        self.add_argument('-width',
                          help='The width of the output (pixels),\
                              e.g -width 127 \
                              (default: %(default)s)',
                          type=int, default=None)
        self.add_argument('-height',
                          help='The height of the output (pixels),\
                              e.g -height 15 \
                              (default: %(default)s)',
                          type=int, default=None)
        self.add_argument('-scale',
                          help='Enlarge a picture n-times,\
                              e.g -scale 5 or \
                              -scale 1.3 if you want to use percentage \
                              (default: %(default)s)',
                          type=float, default=None)
        self.add_argument('-output_format',
                          help='format of the output file,\
                              e.g -output_format PNG \
                              (default: %(default)s)',
                          type=str, default="JPEG")

    def error(self, message):
        sys.stderr.write('error: {}\n'.format(message))
        self.print_help()
        sys.exit(2)
