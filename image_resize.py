from args_parser import ConsoleArgsParser
from PIL import Image
from image_resize_class import ResizableImage


# def create_image(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
    # img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
    #                                 args.output_format)
    # img.resize_image_enlarge_scale(args.enlarge_scale)


if __name__ == '__main__':
    parser = ConsoleArgsParser()
    args = parser.parse_args()
    if args.enlarge_scale and not (args.height or args.width or args.reduce_scale):
        img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                             args.output_format)
        img.resize_image_enlarge_scale(args.enlarge_scale)
    elif args.reduce_scale and not (args.height or args.width or args.enlarge_scale):
        img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                             args.output_format)
        img.resize_image_reduce_scale(args.reduce_scale)
    elif args.height and not (args.width or args.enlarge_scale or args.reduce_scale):
        img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                             args.output_format)
        img.resize_image_with_new_height(args.height)
    elif args.width and not (args.height or args.enlarge_scale or args.reduce_scale):
        img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                             args.output_format)
        img.resize_image_with_new_width(args.width)
    elif args.height and args.width and not (args.enlarge_scale or args.reduce_scale):
        img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                             args.output_format)
        ratio_btw_original_and_new_size = img.original_aspect_ratio - (args.height / args.width)
        if (ratio_btw_original_and_new_size > 0.05) or (ratio_btw_original_and_new_size < -0.05):
            print("The aspect ratio between sides of the picture is bad.")
        img.resize_image_without_aspect_ratio_saving(args.height, args.width)
    elif args.output_format and not (args.height or args.width or args.enlarge_scale or args.reduce_scale):
        img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                             args.output_format)
        img.change_image_format()
    else:
        raise ValueError('Too many keys. Please, remove some keys from the row.')
    print('File created.')
