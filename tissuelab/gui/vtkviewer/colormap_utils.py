import numpy as np


class Colormap (object):

    def __init__(self, name=None):
        self._color_points = {}
        self._color_map = None
        self.name = name

    def get_color(self, value):
        from scipy.interpolate import splrep, splev
        if len(self._color_points) == 0:
            return (0.0, 0.0, 0.0)
        elif value <= np.min(self._color_points.keys()):
            return self._color_points[np.min(self._color_points.keys())]
        elif value >= np.max(self._color_points.keys()):
            return self._color_points[np.max(self._color_points.keys())]
        else:
            return tuple([float(splev(value, self._color_map[channel], der=0)) for channel in [0, 1, 2]])

    def get_values(self):
        return list(np.sort(self._color_points.keys()))

    def __call__(self, value):
        return self.get_color(value)

    def add_rgb_point(self, value, color):
        assert (value >= 0.0) & (value <= 1.0)
        if np.max(color) > 1.0:
            color = tuple(np.array(color) / 255.)
        self._color_points[value] = tuple(color)
        self._compute()

    def _compute(self):
        from scipy.interpolate import splrep, splev
        if len(self._color_points) > 1:
            self._color_map = [splrep(np.sort(self._color_points.keys()), np.array(self._color_points.values())[
                                      np.argsort(self._color_points.keys()), channel], s=0, k=1) for channel in [0, 1, 2]]

    def __str__(self):
        # return self._color_points.__str__()
        sorted_values = np.sort(self._color_points.keys())

        cmap_string = "{"
        for i, value in enumerate(sorted_values):
            cmap_string = cmap_string + \
                str(value) + " : " + str(self._color_points[value])
            if i < sorted_values.size - 1:
                cmap_string = cmap_string + ",\n"
        cmap_string = cmap_string + "}\n"
        return cmap_string


def colormap_from_file(filename, name=None, delimiter=' '):
    import csv

    colormap = Colormap(name=name)

    colormap_file = open(filename, "rU")
    colormap_reader = csv.reader(colormap_file, delimiter=delimiter)
    colormap_data = []
    for color_line in colormap_reader:
        if color_line[0].rfind('Index') == -1:
            colormap_data.append(np.array(color_line).astype(float))
    colormap_data = np.array(colormap_data)
    colormap_file.close()

    for c, color in enumerate(colormap_data):
        if colormap_data.shape[1] == 4:
            if colormap_data[:, 0].max() > 1:
                colormap.add_rgb_point(color[0] / 255., color[1:])
            else:
                colormap.add_rgb_point(color[0], color[1:])
        else:
            colormap.add_rgb_point(
                float(c) / (colormap_data.shape[0] - 1), color)
    return colormap


glasbey = np.array(
    [[1.0, 1.0, 1.0],
     [0.0, 0.0, 1.0],
     [1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 0.2],
     [1.0, 0.0, 0.713725490196],
     [0.0, 0.325490196078, 0.0],
     [1.0, 0.827450980392, 0.0],
     [0.0, 0.623529411765, 1.0],
     [0.603921568627, 0.301960784314, 0.258823529412],
     [0.0, 1.0, 0.745098039216],
     [0.470588235294, 0.247058823529, 0.756862745098],
     [0.121568627451, 0.588235294118, 0.596078431373],
     [1.0, 0.674509803922, 0.992156862745],
     [0.694117647059, 0.8, 0.443137254902],
     [0.945098039216, 0.0313725490196, 0.360784313725],
     [0.996078431373, 0.560784313725, 0.258823529412],
     [0.866666666667, 0.0, 1.0],
     [0.125490196078, 0.101960784314, 0.00392156862745],
     [0.447058823529, 0.0, 0.333333333333],
     [0.462745098039, 0.423529411765, 0.58431372549],
     [0.0078431372549, 0.678431372549, 0.141176470588],
     [0.78431372549, 1.0, 0.0],
     [0.533333333333, 0.423529411765, 0.0],
     [1.0, 0.717647058824, 0.623529411765],
     [0.521568627451, 0.521568627451, 0.403921568627],
     [0.63137254902, 0.0117647058824, 0.0],
     [0.078431372549, 0.976470588235, 1.0],
     [0.0, 0.278431372549, 0.619607843137],
     [0.862745098039, 0.36862745098, 0.576470588235],
     [0.576470588235, 0.83137254902, 1.0],
     [0.0, 0.298039215686, 1.0],
     [0.0, 0.258823529412, 0.313725490196],
     [0.223529411765, 0.654901960784, 0.41568627451],
     [0.933333333333, 0.439215686275, 0.996078431373],
     [0.0, 0.0, 0.392156862745],
     [0.670588235294, 0.960784313725, 0.8],
     [0.63137254902, 0.572549019608, 1.0],
     [0.643137254902, 1.0, 0.450980392157],
     [1.0, 0.807843137255, 0.443137254902],
     [0.278431372549, 0.0, 0.0823529411765],
     [0.83137254902, 0.678431372549, 0.772549019608],
     [0.98431372549, 0.462745098039, 0.435294117647],
     [0.670588235294, 0.737254901961, 0.0],
     [0.458823529412, 0.0, 0.843137254902],
     [0.650980392157, 0.0, 0.603921568627],
     [0.0, 0.450980392157, 0.996078431373],
     [0.647058823529, 0.364705882353, 0.682352941176],
     [0.38431372549, 0.517647058824, 0.0078431372549],
     [0.0, 0.474509803922, 0.658823529412],
     [0.0, 1.0, 0.513725490196],
     [0.337254901961, 0.207843137255, 0.0],
     [0.623529411765, 0.0, 0.247058823529],
     [0.258823529412, 0.176470588235, 0.258823529412],
     [1.0, 0.949019607843, 0.733333333333],
     [0.0, 0.364705882353, 0.262745098039],
     [0.988235294118, 1.0, 0.486274509804],
     [0.623529411765, 0.749019607843, 0.729411764706],
     [0.654901960784, 0.329411764706, 0.0745098039216],
     [0.290196078431, 0.152941176471, 0.423529411765],
     [0.0, 0.0627450980392, 0.650980392157],
     [0.56862745098, 0.305882352941, 0.427450980392],
     [0.811764705882, 0.58431372549, 0.0],
     [0.764705882353, 0.733333333333, 1.0],
     [0.992156862745, 0.266666666667, 0.250980392157],
     [0.258823529412, 0.305882352941, 0.125490196078],
     [0.41568627451, 0.00392156862745, 0.0],
     [0.709803921569, 0.513725490196, 0.329411764706],
     [0.517647058824, 0.913725490196, 0.576470588235],
     [0.376470588235, 0.850980392157, 0.0],
     [1.0, 0.435294117647, 0.827450980392],
     [0.4, 0.294117647059, 0.247058823529],
     [0.996078431373, 0.392156862745, 0.0],
     [0.894117647059, 0.0117647058824, 0.498039215686],
     [0.0666666666667, 0.780392156863, 0.682352941176],
     [0.823529411765, 0.505882352941, 0.545098039216],
     [0.356862745098, 0.462745098039, 0.486274509804],
     [0.125490196078, 0.23137254902, 0.41568627451],
     [0.705882352941, 0.329411764706, 1.0],
     [0.886274509804, 0.0313725490196, 0.823529411765],
     [0.0, 0.00392156862745, 0.078431372549],
     [0.364705882353, 0.517647058824, 0.266666666667],
     [0.650980392157, 0.980392156863, 1.0],
     [0.380392156863, 0.482352941176, 0.788235294118],
     [0.38431372549, 0.0, 0.478431372549],
     [0.494117647059, 0.745098039216, 0.227450980392],
     [0.0, 0.235294117647, 0.717647058824],
     [1.0, 0.992156862745, 0.0],
     [0.0274509803922, 0.772549019608, 0.886274509804],
     [0.705882352941, 0.654901960784, 0.223529411765],
     [0.580392156863, 0.729411764706, 0.541176470588],
     [0.8, 0.733333333333, 0.627450980392],
     [0.21568627451, 0.0, 0.192156862745],
     [0.0, 0.156862745098, 0.00392156862745],
     [0.588235294118, 0.478431372549, 0.505882352941],
     [0.152941176471, 0.533333333333, 0.149019607843],
     [0.807843137255, 0.509803921569, 0.705882352941],
     [0.588235294118, 0.643137254902, 0.76862745098],
     [0.705882352941, 0.125490196078, 0.501960784314],
     [0.43137254902, 0.337254901961, 0.705882352941],
     [0.576470588235, 0.0, 0.725490196078],
     [0.780392156863, 0.188235294118, 0.239215686275],
     [0.450980392157, 0.4, 1.0],
     [0.0588235294118, 0.733333333333, 0.992156862745],
     [0.674509803922, 0.643137254902, 0.392156862745],
     [0.713725490196, 0.458823529412, 0.980392156863],
     [0.847058823529, 0.862745098039, 0.996078431373],
     [0.341176470588, 0.552941176471, 0.443137254902],
     [0.847058823529, 0.333333333333, 0.133333333333],
     [0.0, 0.76862745098, 0.403921568627],
     [0.952941176471, 0.647058823529, 0.411764705882],
     [0.847058823529, 1.0, 0.713725490196],
     [0.00392156862745, 0.0941176470588, 0.858823529412],
     [0.203921568627, 0.258823529412, 0.211764705882],
     [1.0, 0.603921568627, 0.0],
     [0.341176470588, 0.372549019608, 0.00392156862745],
     [0.776470588235, 0.945098039216, 0.309803921569],
     [1.0, 0.372549019608, 0.521568627451],
     [0.482352941176, 0.674509803922, 0.941176470588],
     [0.470588235294, 0.392156862745, 0.192156862745],
     [0.635294117647, 0.521568627451, 0.8],
     [0.411764705882, 1.0, 0.862745098039],
     [0.776470588235, 0.321568627451, 0.392156862745],
     [0.474509803922, 0.101960784314, 0.250980392157],
     [0.0, 0.933333333333, 0.274509803922],
     [0.905882352941, 0.811764705882, 0.270588235294],
     [0.850980392157, 0.501960784314, 0.913725490196],
     [1.0, 0.827450980392, 0.819607843137],
     [0.819607843137, 1.0, 0.552941176471],
     [0.141176470588, 0.0, 0.0117647058824],
     [0.341176470588, 0.639215686275, 0.756862745098],
     [0.827450980392, 0.905882352941, 0.788235294118],
     [0.796078431373, 0.435294117647, 0.309803921569],
     [0.243137254902, 0.0941176470588, 0.0],
     [0.0, 0.458823529412, 0.874509803922],
     [0.439215686275, 0.690196078431, 0.345098039216],
     [0.819607843137, 0.0941176470588, 0.0],
     [0.0, 0.117647058824, 0.419607843137],
     [0.411764705882, 0.78431372549, 0.772549019608],
     [1.0, 0.796078431373, 1.0],
     [0.913725490196, 0.760784313725, 0.537254901961],
     [0.749019607843, 0.505882352941, 0.180392156863],
     [0.270588235294, 0.164705882353, 0.56862745098],
     [0.670588235294, 0.298039215686, 0.760784313725],
     [0.0549019607843, 0.458823529412, 0.239215686275],
     [0.0, 0.117647058824, 0.0980392156863],
     [0.462745098039, 0.286274509804, 0.498039215686],
     [1.0, 0.662745098039, 0.78431372549],
     [0.36862745098, 0.21568627451, 0.850980392157],
     [0.933333333333, 0.901960784314, 0.541176470588],
     [0.623529411765, 0.211764705882, 0.129411764706],
     [0.313725490196, 0.0, 0.580392156863],
     [0.741176470588, 0.564705882353, 0.501960784314],
     [0.0, 0.427450980392, 0.494117647059],
     [0.345098039216, 0.874509803922, 0.376470588235],
     [0.278431372549, 0.313725490196, 0.403921568627],
     [0.00392156862745, 0.364705882353, 0.623529411765],
     [0.388235294118, 0.188235294118, 0.235294117647],
     [0.0078431372549, 0.807843137255, 0.580392156863],
     [0.545098039216, 0.325490196078, 0.145098039216],
     [0.670588235294, 0.0, 1.0],
     [0.552941176471, 0.164705882353, 0.529411764706],
     [0.333333333333, 0.325490196078, 0.580392156863],
     [0.588235294118, 1.0, 0.0],
     [0.0, 0.596078431373, 0.482352941176],
     [1.0, 0.541176470588, 0.796078431373],
     [0.870588235294, 0.270588235294, 0.78431372549],
     [0.419607843137, 0.427450980392, 0.901960784314],
     [0.117647058824, 0.0, 0.266666666667],
     [0.678431372549, 0.298039215686, 0.541176470588],
     [1.0, 0.525490196078, 0.63137254902],
     [0.0, 0.137254901961, 0.235294117647],
     [0.541176470588, 0.803921568627, 0.0],
     [0.435294117647, 0.792156862745, 0.61568627451],
     [0.882352941176, 0.294117647059, 0.992156862745],
     [1.0, 0.690196078431, 0.301960784314],
     [0.898039215686, 0.909803921569, 0.223529411765],
     [0.447058823529, 0.0627450980392, 1.0],
     [0.435294117647, 0.321568627451, 0.396078431373],
     [0.525490196078, 0.537254901961, 0.188235294118],
     [0.388235294118, 0.149019607843, 0.313725490196],
     [0.411764705882, 0.149019607843, 0.125490196078],
     [0.78431372549, 0.43137254902, 0.0],
     [0.819607843137, 0.643137254902, 1.0],
     [0.776470588235, 0.823529411765, 0.337254901961],
     [0.309803921569, 0.403921568627, 0.301960784314],
     [0.682352941176, 0.647058823529, 0.650980392157],
     [0.666666666667, 0.176470588235, 0.396078431373],
     [0.780392156863, 0.317647058824, 0.686274509804],
     [1.0, 0.349019607843, 0.674509803922],
     [0.572549019608, 0.4, 0.305882352941],
     [0.4, 0.525490196078, 0.721568627451],
     [0.435294117647, 0.596078431373, 1.0],
     [0.360784313725, 1.0, 0.623529411765],
     [0.674509803922, 0.537254901961, 0.698039215686],
     [0.823529411765, 0.133333333333, 0.38431372549],
     [0.780392156863, 0.811764705882, 0.576470588235],
     [1.0, 0.725490196078, 0.117647058824],
     [0.980392156863, 0.580392156863, 0.552941176471],
     [0.192156862745, 0.133333333333, 0.305882352941],
     [0.996078431373, 0.317647058824, 0.380392156863],
     [0.996078431373, 0.552941176471, 0.392156862745],
     [0.266666666667, 0.211764705882, 0.0901960784314],
     [0.788235294118, 0.635294117647, 0.329411764706],
     [0.780392156863, 0.909803921569, 0.941176470588],
     [0.266666666667, 0.596078431373, 0.0],
     [0.576470588235, 0.674509803922, 0.227450980392],
     [0.0862745098039, 0.294117647059, 0.109803921569],
     [0.0313725490196, 0.329411764706, 0.474509803922],
     [0.454901960784, 0.176470588235, 0.0],
     [0.407843137255, 0.235294117647, 1.0],
     [0.250980392157, 0.160784313725, 0.149019607843],
     [0.643137254902, 0.443137254902, 0.843137254902],
     [0.811764705882, 0.0, 0.607843137255],
     [0.462745098039, 0.00392156862745, 0.137254901961],
     [0.325490196078, 0.0, 0.345098039216],
     [0.0, 0.321568627451, 0.909803921569],
     [0.16862745098, 0.360784313725, 0.341176470588],
     [0.627450980392, 0.850980392157, 0.572549019608],
     [0.690196078431, 0.101960784314, 0.898039215686],
     [0.113725490196, 0.0117647058824, 0.141176470588],
     [0.478431372549, 0.227450980392, 0.623529411765],
     [0.839215686275, 0.819607843137, 0.811764705882],
     [0.627450980392, 0.392156862745, 0.411764705882],
     [0.41568627451, 0.61568627451, 0.627450980392],
     [0.6, 0.858823529412, 0.443137254902],
     [0.752941176471, 0.219607843137, 0.811764705882],
     [0.490196078431, 1.0, 0.349019607843],
     [0.58431372549, 0.0, 0.133333333333],
     [0.835294117647, 0.635294117647, 0.874509803922],
     [0.0862745098039, 0.513725490196, 0.8],
     [0.650980392157, 0.976470588235, 0.270588235294],
     [0.427450980392, 0.411764705882, 0.380392156863],
     [0.337254901961, 0.737254901961, 0.305882352941],
     [1.0, 0.427450980392, 0.317647058824],
     [1.0, 0.0117647058824, 0.972549019608],
     [1.0, 0.0, 0.286274509804],
     [0.792156862745, 0.0, 0.137254901961],
     [0.262745098039, 0.427450980392, 0.0705882352941],
     [0.917647058824, 0.666666666667, 0.678431372549],
     [0.749019607843, 0.647058823529, 0.0],
     [0.149019607843, 0.172549019608, 0.2],
     [0.333333333333, 0.725490196078, 0.0078431372549],
     [0.474509803922, 0.713725490196, 0.619607843137],
     [0.996078431373, 0.925490196078, 0.83137254902],
     [0.545098039216, 0.647058823529, 0.349019607843],
     [0.552941176471, 0.996078431373, 0.756862745098],
     [0.0, 0.235294117647, 0.16862745098],
     [0.247058823529, 0.0666666666667, 0.156862745098],
     [1.0, 0.866666666667, 0.964705882353],
     [0.0666666666667, 0.101960784314, 0.572549019608],
     [0.603921568627, 0.258823529412, 0.329411764706],
     [0.58431372549, 0.61568627451, 0.933333333333],
     [0.494117647059, 0.509803921569, 0.282352941176],
     [0.227450980392, 0.0235294117647, 0.396078431373],
     [0.741176470588, 0.458823529412, 0.396078431373]
     ])
