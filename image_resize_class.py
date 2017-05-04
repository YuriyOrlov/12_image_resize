from PIL import ImageOps


class ResizableImage(object):

    def __init__(self, image, input_filepath, output_filepath, output_format, *args, **kwargs):
        self._image = image
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
        self.output_format = output_format
        super(ResizableImage, self).__init__(*args, **kwargs)
        self.image_height, self.image_width = self.size
        self.original_aspect_ratio = float(self.image_height / self.image_width)

    def __getattr__(self, key):
        if key == '_image':
            raise AttributeError()
        return getattr(self._image, key)

    def __repr__(self):
        return '{}{}'.format(self.image_height, self.image_width)

    def create_name_for_output_file(self, new_image_height, new_image_width):
        if self.output_format == "JPEG":
            input_filename = (self.input_filepath.split("/")[-1]).split(".")[0]
            return "{}/{}_{}x{}.jpeg".format(self.output_filepath, input_filename, new_image_height, new_image_width)
        else:
            input_filename = (self.input_filepath.split("/")[-1]).split(".")[0]
            return "{}/{}_{}x{}.png".format(self.output_filepath, input_filename, new_image_height, new_image_width)

    def scaling_down_image(self, num_scale):
        if num_scale > 1:
            size = (self.image_height / num_scale, self.image_width / num_scale)
            self._image.thumbnail(size)
            return self._image
        else:
            size = (self.image_height - (self.image_height * num_scale),
                    self.image_width - (self.image_width * num_scale))
            self._image.thumbnail(size)
            return self._image

    def scaling_up_image(self, num_scale):
        if num_scale > 1:
            size = (int(self.image_height * num_scale), int(self.image_width * num_scale))
            return ImageOps.fit(self._image, size)
        else:
            size = (int(self.image_height + (self.image_height * num_scale)),
                    int(self.image_width + (self.image_width * num_scale)))
            return ImageOps.fit(self._image, size)

    def resize_image_enlarge_scale(self, scale):
        modified_image = self.scaling_up_image(scale)
        modified_image_height, modified_image_width = modified_image.size
        output_filename = self.create_name_for_output_file(modified_image_height, modified_image_width)
        modified_image.save(output_filename, self.output_format)

    def resize_image_reduce_scale(self, scale):
        modified_image = self.scaling_up_image(scale)
        modified_image_height, modified_image_width = modified_image.size
        output_filename = self.create_name_for_output_file(modified_image_height, modified_image_width)
        modified_image.save(output_filename, self.output_format)

    def resize_image_with_new_width(self, new_width):
        new_height = int(new_width * self.image_height / self.image_width)
        self._image.thumbnail((new_height, new_width))
        output_filename = self.create_name_for_output_file(new_height, new_width)
        self._image.save(output_filename, self.output_format)

    def resize_image_with_new_height(self, new_height):
        new_width = int(new_height * self.image_width / self.image_height)
        self._image.thumbnail((new_height, new_width))
        output_filename = self.create_name_for_output_file(new_height, new_width)
        self._image.save(output_filename, self.output_format)

    def resize_image_without_aspect_ratio_saving(self, new_height, new_width):
        resized_image = self._image.resize((new_height, new_width))
        output_filename = self.create_name_for_output_file(new_height, new_width)
        resized_image.save(output_filename, self.output_format)

    def change_image_format(self):
        output_filename = self.create_name_for_output_file(self.image_height, self.image_width)
        self._image.save(output_filename, self.output_format)
