from args_parser import ConsoleArgsParser
from PIL import Image, ImageOps


def scaling_down_image(num_scale, image, image_height, image_width):
    if num_scale > 1:
        size = (image_height / num_scale, image_width / num_scale)
        image.thumbnail(size, Image.LANCZOS)
        return image
    else:
        size = (image_height - (image_height * num_scale), image_width - (image_width * num_scale))
        image.thumbnail(size, Image.LANCZOS)
        return image


def scaling_up_image(num_scale, image, image_height, image_width):
    if num_scale > 1:
        size = (image_height * num_scale, image_width * num_scale)
        return ImageOps.fit(image, size, Image.LANCZOS)
    else:
        size = (int(image_height + (image_height * num_scale)), int(image_width + (image_width * num_scale)))
        return ImageOps.fit(image, size, Image.LANCZOS)


def create_name_for_output_file(path_to_original, path_to_result, new_image_height, new_image_width, output_format):
    if output_format == "JPEG":
        input_filename = (path_to_original.split("/")[-1]).split(".")[0]
        return "{}/{}_{}x{}.jpeg".format(path_to_result, input_filename, new_image_height, new_image_width)
    else:
        input_filename = (path_to_original.split("/")[-1]).split(".")[0]
        return "{}/{}_{}x{}.png".format(path_to_result, input_filename, new_image_height, new_image_width)


def resize_image_enlarge_scale(path_to_original, path_to_result, output_format, scale):
    image = Image.open(path_to_original)
    image_height, image_width = image.size
    modified_image = scaling_up_image(scale, image, image_height, image_width)
    modified_image_height, modified_image_width = modified_image.size
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  modified_image_height, modified_image_height, output_format)
    modified_image.save(output_filename, "JPEG")


def resize_image_reduce_scale(path_to_original, path_to_result, output_format, scale):
    image = Image.open(path_to_original)
    image_height, image_width = image.size
    modified_image = scaling_down_image(scale, image, image_height, image_width)
    modified_image_height, modified_image_width = modified_image.size
    output_filename = create_name_for_output_file(path_to_original, path_to_result,
                                                  modified_image_height, modified_image_height, output_format)
    modified_image.save(output_filename, "JPEG")


# def resize_image_with_width(path_to_original, path_to_result, output_format, width):
#     image = Image.open(path_to_original)
#     image_height, image_width = image.size


if __name__ == '__main__':
    parser = ConsoleArgsParser()
    args = parser.parse_args()
    if args.enlarge_scale:
        resize_image_enlarge_scale(args.filepath, args.output, args.output_format, args.enlarge_scale)
    elif args.reduce_scale:
        resize_image_reduce_scale(args.filepath, args.output, args.output_format, args.reduce_scale)
    # print(args.filepath, args.output, args.height, args.width, args.enlarge_scale, args.reduce_scale)
    # print(args.filepath.split("/")[-1])
