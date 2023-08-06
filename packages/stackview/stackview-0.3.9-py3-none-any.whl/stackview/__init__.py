__version__ = "0.3.9"

import warnings
from ._static_view import jupyter_displayable_output, insight
from ._utilities import merge_rgb
from ._context import nop
from ._slice_viewer import _SliceViewer
from ._annotate import annotate
from ._utilities import _no_resize

def slice(
        image,
        slice_number : int = None,
        axis : int = 0,
        display_width : int = None,
        display_height : int = None,
        continuous_update:bool=False,
        slider_text:str="Slice",
        zoom_factor:float = 1.0,
        zoom_spline_order:int = 0
):
    """Shows an image with a slider to go through a stack.

    Parameters
    ----------
    image : image
        Image shown
    slice_number : int, optional
        Slice-position in the stack
    axis : int, optional
        Axis in case we are slicing a stack
    display_width : int, optional
        This parameter is obsolete. Use zoom_factor instead
    display_height : int, optional
        This parameter is obsolete. Use zoom_factor instead
    continuous_update : bool, optional
        Update the image while dragging the mouse, default: False
    zoom_factor: float, optional
        Allows showing the image larger (> 1) or smaller (<1)
    zoom_spline_order: int, optional
        Spline order used for interpolation (default=0, nearest-neighbor)

    Returns
    -------
    An ipywidget with an image display and a slider.
    """

    import ipywidgets
    viewer = _SliceViewer(image,
        slice_number,
        axis,
        display_width,
        display_height,
        continuous_update,
        slider_text,
        zoom_factor=zoom_factor,
        zoom_spline_order=zoom_spline_order
    )
    view = viewer.view
    slice_slider = viewer.slice_slider

    if slice_slider is None:
        return _no_resize(view)
    else:
        return ipywidgets.VBox([_no_resize(view), slice_slider])


def curtain(
        image,
        image_curtain,
        slice_number: int = None,
        axis: int = 0,
        display_width: int = None,
        display_height: int = None,
        continuous_update: bool = False,
        alpha: float = 1,
        zoom_factor:float = 1.0,
        zoom_spline_order:int = 0
):
    """Show two images and allow with a slider to show either the one or the other image.

    Parameters
    ----------
    image : image
        Image shown on the left (behind the curtain)
    image_curtain : image
        Image shown on the right (in front of the curtain)
    slice_number : int, optional
        Slice-position in case we are looking at an image stack
    axis : int, optional
        Axis in case we are slicing a stack
    display_width : int, optional
        This parameter is obsolete. Use zoom_factor instead
    display_height : int, optional
        This parameter is obsolete. Use zoom_factor instead
    continuous_update : bool, optional
        Update the image while dragging the mouse, default: False
    alpha: float, optional
        sets the transperancy of the curtain
    zoom_factor: float, optional
        Allows showing the image larger (> 1) or smaller (<1)
    zoom_spline_order: int, optional
        Spline order used for interpolation (default=0, nearest-neighbor)
        
    Returns
    -------
    An ipywidget with an image display and a slider.
    """
    import ipywidgets
    from ._image_widget import ImageWidget
    import numpy as np

    slice_slider = None
    if len(image.shape) > 2:
        if slice_number is None:
            slice_number = int(image.shape[axis] / 2)

        # setup user interface for changing the slice
        slice_slider = ipywidgets.IntSlider(
            value=slice_number,
            min=0,
            max=image.shape[axis]-1,
            continuous_update=continuous_update,
            description="Slice"
        )

    # setup user interface for changing the curtain position
    slice_shape = list(image.shape)
    slice_shape.pop(axis)
    curtain_slider = ipywidgets.IntSlider(
        value=slice_shape[-1] / 2,
        min=0,
        max=slice_shape[-1],
        continuous_update=continuous_update,
        description="Curtain"
    )

    if len(image.shape) <= 2:
        view = ImageWidget(image, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order)
    else:
        view = ImageWidget(np.take(image, slice_number, axis=axis), zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order)
    if display_width is not None:
        view.width = display_width
    if display_height is not None:
        view.height = display_height

    from ._image_widget import _img_to_rgb

    def transform_image():
        if slice_slider is None:
            image_slice = _img_to_rgb(image.copy())
            image_slice_curtain = _img_to_rgb(image_curtain)
        else:
            image_slice = _img_to_rgb(np.take(image, slice_slider.value, axis=axis))
            image_slice_curtain = _img_to_rgb(np.take(image_curtain, slice_slider.value, axis=axis))

        image_slice[curtain_slider.value:] = (1 - alpha) * image_slice[curtain_slider.value:] + alpha * image_slice_curtain[curtain_slider.value:]
        return image_slice

    # event handler when the user changed something:
    def configuration_updated(event):
        view.data = transform_image()

    configuration_updated(None)

    # connect user interface with event
    curtain_slider.observe(configuration_updated)

    if slice_slider is not None:
        # connect user interface with event
        slice_slider.observe(configuration_updated)

        return ipywidgets.VBox([_no_resize(view), slice_slider, curtain_slider])
    else:
        return ipywidgets.VBox([_no_resize(view), curtain_slider])

def orthogonal(
        image,
        display_width : int = None,
        display_height : int = None,
        continuous_update:bool=False,
        zoom_factor:float = 1.0,
        zoom_spline_order:int = 0
):
    """Show three viewers slicing the image stack in Z,Y and X.

    Parameters
    ----------
    image : image
        Image to be displayed
    display_width : int, optional
        This parameter is obsolete. Use zoom_factor instead
    display_height : int, optional
        This parameter is obsolete. Use zoom_factor instead
    continuous_update : bool, optional
        Update the image while dragging the mouse, default: False
    zoom_factor: float, optional
        Allows showing the image larger (> 1) or smaller (<1)
    zoom_spline_order: int, optional
        Spline order used for interpolation (default=0, nearest-neighbor)

    Returns
    -------
    An ipywidget with an image display and a slider.

    See Also
    --------
    slice()
    """
    import ipywidgets

    return ipywidgets.HBox([
        slice(image, axis=0, slider_text="Z", display_width=display_width, display_height=display_height, continuous_update=continuous_update, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order),
        slice(image, axis=1, slider_text="Y", display_width=display_width, display_height=display_height, continuous_update=continuous_update, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order),
        slice(image, axis=2, slider_text="X", display_width=display_width, display_height=display_height, continuous_update=continuous_update, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order),
    ])


def side_by_side(
        image1,
        image2,
        slice_number: int = None,
        axis: int = 0,
        display_width: int = None,
        display_height: int = None,
        continuous_update: bool = False,
        slider_text: str = "Slice",
        zoom_factor:float = 1.0,
        zoom_spline_order:int = 0
):
    """Shows two images in magenta and green plus a third with their colocalization / overlap view and
    a slider to go through a stack.

    Parameters
    ----------
    image1 : image
        Image shown on the left
    image2 : image
        Image shown on the right
    slice_number : int, optional
        Slice-position in the stack
    axis : int, optional
        Axis in case we are slicing a stack
    display_width : int, optional
        This parameter is obsolete. Use zoom_factor instead
    display_height : int, optional
        This parameter is obsolete. Use zoom_factor instead
    continuous_update : bool, optional
        Update the image while dragging the mouse, default: False
    zoom_factor: float, optional
        Allows showing the image larger (> 1) or smaller (<1)
    zoom_spline_order: int, optional
        Spline order used for interpolation (default=0, nearest-neighbor)

    Returns
    -------
    An ipywidget with three image displays and a slider.
    """

    import ipywidgets
    from ._image_widget import ImageWidget
    import numpy as np

    if slice_number is None:
        slice_number = int(image1.shape[axis] / 2)

    if len(image1.shape) <= 2:
        slice_image = image1
    else:
        slice_image = np.take(image1, slice_number, axis=axis)

    zeros_image = np.zeros(slice_image.shape)
    view1 = ImageWidget(slice_image, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order)
    view2 = ImageWidget(slice_image, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order)
    view3 = ImageWidget(slice_image, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order)

    if display_width is not None:
        view1.display = display_width
        view2.display = display_width
        view3.display = display_width
    if display_height is not None:
        view1.display = display_height
        view2.display = display_height
        view3.display = display_height

    # setup user interface for changing the slice
    slice_slider = None
    if len(image1.shape) > 2:
        slice_slider = ipywidgets.IntSlider(
            value=slice_number,
            min=0,
            max=image1.shape[0] - 1,
            continuous_update=continuous_update,
            description=slider_text,
        )

    from ._image_widget import _is_label_image, _img_to_rgb

    # event handler when the user changed something:
    def configuration_updated(event):
        if slice_slider is not None:
            z = slice_slider.value
            slice_image1 = np.take(image1, z, axis=axis)
            slice_image2 = np.take(image2, z, axis=axis)
        else:
            slice_image1 = image1
            slice_image2 = image2

        if _is_label_image(slice_image1) or _is_label_image(slice_image2):
            rgb_image1 = _img_to_rgb(slice_image1)
            rgb_image2 = _img_to_rgb(slice_image2)

            if _is_label_image(slice_image1) and _is_label_image(slice_image2):
                warnings.warn("Side-by-side mixing two label images may look weird." +
                              "Consider showing original image and a label image side-by-side.")
                factor1 = 0.5
                factor2 = 0.5
            elif _is_label_image(slice_image1):
                factor1 = 0.3
                factor2 = 0.7
            elif _is_label_image(slice_image2):
                factor1 = 0.7
                factor2 = 0.3

            rgb_mix = factor1 * rgb_image1 + factor2 * rgb_image2

            view1.data = rgb_image1
            view2.data = rgb_image2
            view3.data = rgb_mix
        else:
            view1.data = np.asarray([slice_image1, zeros_image, slice_image1]).swapaxes(0, 2)
            view2.data = np.asarray([zeros_image, slice_image2, zeros_image]).swapaxes(0, 2)
            view3.data = np.asarray([slice_image1, slice_image2, slice_image1]).swapaxes(0, 2)

    configuration_updated(None)

    if slice_slider is not None:
        # connect user interface with event
        slice_slider.observe(configuration_updated)

        return ipywidgets.VBox([
            ipywidgets.HBox([_no_resize(view1), _no_resize(view2), _no_resize(view3)]),
            slice_slider
        ])
    else:
        return ipywidgets.HBox([_no_resize(view1), _no_resize(view2), _no_resize(view3)])


def interact(func,
             image = None,
             *args,
             continuous_update: bool = False,
             context:dict = None,
             zoom_factor:float = 1.0,
             zoom_spline_order:int = 0,
             **kwargs):
    """Takes a function which has an image as first parameter and additional parameters.
    It will build a user interface consisting of sliders for numeric parameters and parameters
    that are called "footprint" or "selem".

    Parameters
    ----------
    func : function
    image : Image, optional
        If not provided, context must be provided instead.
    args
    continuous_update : bool, optioonal
        Update the image while dragging the mouse, default: False
    context:dict, optional
        A dictionary of (name:image), allows showing a pulldown of available images.
    zoom_factor: float, optional
        Allows showing the image larger (> 1) or smaller (<1)
    zoom_spline_order: int, optional
        Spline order used for interpolation (default=0, nearest-neighbor)
    context:dict
        dictionary of name, value pairs that can be selected from pulldowns, e.g.: globals()
    kwargs

    """
    import inspect
    import ipywidgets
    from ._utilities import parameter_is_image_parameter
    from ._context import Context

    exposable_parameters = []
    footprint_parameters = []
    image_parameters = []

    if context is not None:
        context = Context(context)

    image_passed = image is not None
    if context is not None and image is None:
        image = next(iter(context._images.values()))


    sig = inspect.signature(func)
    for key in sig.parameters.keys():
        exposable = False
        default_value = 0
        if isinstance(sig.parameters[key].default, int) or isinstance(sig.parameters[key].default, float):
            default_value = sig.parameters[key].default
        min_value, max_value, step = guess_range(key, sig.parameters[key].annotation)

        if min_value is not None:
            int_slider = ipywidgets.IntSlider
            float_slider = ipywidgets.FloatSlider
        else:
            int_slider = ipywidgets.IntText
            float_slider = ipywidgets.FloatText

        if sig.parameters[key].annotation is int:
            default_value = int_slider(min=min_value, max=max_value, step=step, value=default_value, continuous_update=continuous_update)
            exposable = True
        elif sig.parameters[key].annotation is float or 'sigma' in key or 'radius' in key:
            default_value = float_slider(min=min_value, max=max_value, step=step, value=default_value, continuous_update=continuous_update)
            exposable = True
        elif key.startswith("is_") or sig.parameters[key].annotation is bool:
            default_value = ipywidgets.Checkbox(value=default_value)
            exposable = True
        elif key == 'footprint' or key == 'selem' or key == 'structuring_element':
            footprint_parameters.append(key)
            default_value = ipywidgets.IntSlider(min=min_value, max=max_value, step=step, value=default_value, continuous_update=continuous_update)
            exposable = True
        elif parameter_is_image_parameter(sig.parameters[key]) and "destination" not in key and key != "out"  and key != "output":
            if context is not None:
                image_parameters.append(key)
                default_value = ipywidgets.Dropdown(
                    options=list(context._images.keys())
                    #options=[(k, v) for k, v in context._images.items()],
                )
                exposable = True

        if exposable:
            if key in kwargs.keys():
                default_value = kwargs[key]
            exposable_parameters.append(inspect.Parameter(key, inspect.Parameter.KEYWORD_ONLY, default=default_value))

    viewer = _SliceViewer(image, zoom_factor=zoom_factor, zoom_spline_order=zoom_spline_order)
    if viewer.slice_slider is not None:
        viewer.slice_slider.continuous_update=continuous_update
    command_label = ipywidgets.Label(value=func.__name__ + "()")

    from skimage import morphology

    def worker_function(*otherargs, **kwargs):

        command = func.__name__ + "("
        if image_passed:
            command = command + "..."

        for key in [e.name for e in exposable_parameters]:

            if key in footprint_parameters:
                if len(image.shape) == 2:
                    command = command + ", " + key + "=disk(" + str(kwargs[key]) + ")"
                    kwargs[key] = morphology.disk(kwargs[key])
                elif len(image.shape) == 3:
                    command = command + ", " + key + "=ball(" + str(kwargs[key]) + ")"
                    kwargs[key] = morphology.ball(kwargs[key])
            elif key in image_parameters:
                command = command + ", " + key + "=" + str(kwargs[key])
                kwargs[key] = context._images[kwargs[key]]
            else:
                command = command + ", " + key + "=" + str(kwargs[key])
        command = command + ")"
        command_label.value = command.replace("(,", "(")

        if image_passed:
            viewer.image = func(image, *args, **kwargs)
        else:
            viewer.image = func(*args, **kwargs)
        if viewer.slice_slider is not None:
            viewer.slice_slider.max = viewer.image.shape[0] - 1
        viewer.configuration_updated(None)


    worker_function.__signature__ = inspect.Signature(exposable_parameters)
    ipywidgets.interact(worker_function)

    #inter = ipywidgets.interactive(worker_function, dict(manual=False, auto_display=False))
    #inter.update()

    if viewer.slice_slider is not None:
        return ipywidgets.VBox([
            _no_resize(viewer.view),
            #ipywidgets.VBox(inter.result),
            viewer.slice_slider,
            command_label
        ])
    else:
        return ipywidgets.VBox([
            _no_resize(viewer.view),
            #ipywidgets.VBox(inter.result),
            command_label
        ])

def guess_range(name, annotation):
    if name == 'footprint' or name == 'selem' or name == 'structuring_element':
        return 0, 100, 1
    if 'sigma' in name:
        return 0, 10, 1
    if 'radius' in name:
        return 0, 100, 1
    if 'factor' in name:
        return 0, 100, 1
    if name == 'angle' or "degrees" in name:
        return 0, 360, 15
    return None, None, None

def picker(
        image,
        slice_number: int = None,
        display_width: int = None,
        display_height: int = None,
        continuous_update: bool = False,
        slider_text: str = "Slice",
        zoom_factor:float = 1.0,
        zoom_spline_order:int = 0
):
    """Shows an image with a slider to go through a stack plus a label with the current mouse position and intensity at that position.

    Parameters
    ----------
    image : image
        Image shown
    slice_number : int, optional
        Slice-position in the stack
    display_width : int, optional
        This parameter is obsolete. Use zoom_factor instead
    display_height : int, optional
        This parameter is obsolete. Use zoom_factor instead
    continuous_update : bool, optional
        Update the image while dragging the mouse, default: False
    zoom_factor: float, optional
        Allows showing the image larger (> 1) or smaller (<1)
    zoom_spline_order: int, optional
        Spline order used for interpolation (default=0, nearest-neighbor)

    Returns
    -------
    An ipywidget with an image display, a slider and a label showing mouse position and intensity.
    """

    import ipywidgets
    viewer = _SliceViewer(image,
                          slice_number=slice_number,
                          display_width=display_width,
                          display_height=display_height,
                          continuous_update=continuous_update,
                          slider_text=slider_text,
                          zoom_factor=zoom_factor,
                          zoom_spline_order=zoom_spline_order
                          )
    view = viewer.view
    slice_slider = viewer.slice_slider
    label = ipywidgets.Label("[]:")

    from ipyevents import Event
    event_handler = Event(source=view, watched_events=['mousemove'])

    def update_display(event):
        relative_position_x = event['relativeX'] / zoom_factor
        relative_position_y = event['relativeY'] / zoom_factor
        absolute_position_x = int(relative_position_x)
        absolute_position_y = int(relative_position_y)

        if slice_slider is not None:
            absolute_position_z = slice_slider.value
            intensity = image[absolute_position_z, absolute_position_y, absolute_position_x]
            label.value = "[z=" + str(absolute_position_z) + ", y=" + str(absolute_position_y) + ", x=" + str(
                absolute_position_x) + "] = " + str(intensity)
        else:
            intensity = image[absolute_position_y, absolute_position_x]
            label.value = "[y=" + str(absolute_position_y) + ", x=" + str(absolute_position_x) + "] = " + str(intensity)

    event_handler.on_dom_event(update_display)

    if slice_slider is not None:
        return ipywidgets.VBox([_no_resize(view), slice_slider, label], stretch=False)
    else:
        return ipywidgets.VBox([_no_resize(view), label])




