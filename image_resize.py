from args_parser import ConsoleArgsParser
from PIL import Image, ImageOps


def create_name_for_output_file(path_to_original, path_to_result, new_image_height, new_image_width, output_format):
    input_filename = (path_to_original.split("/")[-1]).split(".")[0]
    output_filename = "{}/{}_{}x{}.".format(path_to_result,
                                            input_filename,
                                            new_image_height,
                                            new_image_width)
    if output_format == "JPEG":
        return "{}{}".format(output_filename, 'jpeg')
    else:
        return "{}{}".format(output_filename, 'png')


def resize_image_scale(image, path_to_original, path_to_result, output_format, scale):
    image_height, image_width = image.size
    size = (int(image_height * scale), int(image_width * scale))
    modified_image = ImageOps.fit(image, size, Image.LANCZOS)
    modified_image_height, modified_image_width = modified_image.size
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  modified_image_height, modified_image_width, output_format)
    modified_image.save(output_filename, output_format)


def resize_image_with_new_width(image, path_to_original, path_to_result, output_format, new_width):
    image_height, image_width = image.size
    new_height = int(new_width * image_height / image_width)
    image.thumbnail((new_height, new_width), Image.LANCZOS)
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  new_height, new_width, output_format)
    image.save(output_filename, output_format)


def resize_image_with_new_height(image, path_to_original, path_to_result, output_format, new_height):
    image_height, image_width = image.size
    new_width = int(new_height * image_width / image_height)
    image.thumbnail((new_height, new_width), Image.LANCZOS)
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  new_height, new_width, output_format)
    image.save(output_filename, output_format)


def resize_image_without_aspect_ratio_saving(image, path_to_original, path_to_result,
                                             output_format, new_height, new_width):
    resized_image = image.resize((new_height, new_width), Image.LANCZOS)
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  new_height, new_width, output_format)
    resized_image.save(output_filename, output_format)


def change_image_format(image, path_to_original, path_to_result,
                        output_format):
    image_height, image_width = image.size
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  image_height, image_width, output_format)
    image.save(output_filename, output_format)


def determine_action(image, **kwargs):
    if kwargs.get('scale') and not (kwargs.get('height') or kwargs.get('width')):
        resize_image_scale(image, kwargs.get('input_filepath'),
                           kwargs.get('output_filepath'), kwargs.get('output_format'),
                           kwargs.get('scale'))
    elif args.height and not (kwargs.get('width') or kwargs.get('scale')):
        resize_image_with_new_height(image, kwargs.get('input_filepath'),
                                     kwargs.get('output_filepath'), kwargs.get('output_format'),
                                     kwargs.get('height'))
    elif args.width and not (kwargs.get('height') or kwargs.get('scale')):
        resize_image_with_new_width(image, kwargs.get('input_filepath'),
                                    kwargs.get('output_filepath'), kwargs.get('output_format'),
                                    kwargs.get('width'))
    elif args.height and args.width and not (args.scale):
        resize_image_without_aspect_ratio_saving(image, kwargs.get('input_filepath'),
                                                 kwargs.get('output_filepath'), kwargs.get('output_format'),
                                                 kwargs.get('height'), kwargs.get('width'))
    elif args.output_format and not (args.height or args.width or args.scale):
        change_image_format(image, kwargs.get('input_filepath'),
                            kwargs.get('output_filepath'), kwargs.get('output_format'))
    else:
        raise ValueError('Too many keys. Please, remove some keys from the row.')


if __name__ == '__main__':
    parser = ConsoleArgsParser()
    args = parser.parse_args()
    img = Image.open(args.input_filepath)
    determine_action(img, input_filepath=args.input_filepath, output_filepath=args.output_filepath,
                     output_format=args.output_format, scale=args.scale, height=args.height,
                     width=args.width)
