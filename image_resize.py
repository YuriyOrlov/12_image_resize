from args_parser import ConsoleArgsParser
from PIL import Image
from image_resize_class import ResizableImage

if __name__ == '__main__':
    parser = ConsoleArgsParser()
    args = parser.parse_args()
    img = ResizableImage(Image.open(args.input_filepath), args.input_filepath, args.output_filepath,
                         args.output_format, height=args.height, width=args.width,
                         enlarge_scale=args.enlarge_scale, reduce_scale=args.reduce_scale)
    if img.action == 'height_width':
        ratio_btw_original_and_new_size = img.original_aspect_ratio - (args.height / args.width)
        if (ratio_btw_original_and_new_size > 0.05) or (ratio_btw_original_and_new_size < -0.05):
            print("The aspect ratio between sides of the picture is bad.")
        img.resize_image_without_aspect_ratio_saving(args.height, args.width)
    print('File created.')
