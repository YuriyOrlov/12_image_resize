from args_parser import ConsoleArgsParser
from PIL import Image
from image_resize_class import ResizableImage


def get_type_of_resize(input_filepath, output_filepath,
                       output_format, height, width,
                       enlarge_scale, reduce_scale):
    if enlarge_scale and not (height or width or reduce_scale):
        img = ResizableImage(Image.open(input_filepath), input_filepath, output_filepath, output_format)
        img.resize_image_enlarge_scale(args.enlarge_scale)
    elif reduce_scale and not (height or width or enlarge_scale):
        img = ResizableImage(Image.open(input_filepath), input_filepath, output_filepath, output_format)
        img.resize_image_reduce_scale(args.reduce_scale)
    elif height and not (width or enlarge_scale or reduce_scale):
        img = ResizableImage(Image.open(input_filepath), input_filepath, output_filepath, output_format)
        img.resize_image_with_new_height(args.height)
    elif width and not (height or enlarge_scale or reduce_scale):
        img = ResizableImage(Image.open(input_filepath), input_filepath, output_filepath, output_format)
        img.resize_image_with_new_width(args.width)
    elif height and width and not (enlarge_scale or reduce_scale):
        print(enlarge_scale, (enlarge_scale is None))
        print(reduce_scale, (reduce_scale is None))
        img = ResizableImage(Image.open(input_filepath), input_filepath, output_filepath, output_format)
        ratio_btw_original_and_new_size = img.original_aspect_ratio - (height / width)
        if (ratio_btw_original_and_new_size > 0.05) or (ratio_btw_original_and_new_size < -0.05):
            print("The aspect ratio between sides of the picture is bad.")
        img.resize_image_without_aspect_ratio_saving(args.height, args.width)
    elif output_format and not (height or width or enlarge_scale or reduce_scale):
        img = ResizableImage(Image.open(input_filepath), input_filepath, output_filepath, output_format)
        img.change_image_format()
    else:
        raise ValueError('Too many keys. Please, remove some keys from the row.')


if __name__ == '__main__':
    parser = ConsoleArgsParser()
    args = parser.parse_args()
    get_type_of_resize(args.input_filepath, args.output_filepath,
                       args.output_format, args.height, args.width,
                       args.enlarge_scale, args.reduce_scale)
