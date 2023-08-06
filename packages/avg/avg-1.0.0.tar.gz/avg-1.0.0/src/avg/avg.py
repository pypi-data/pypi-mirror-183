class shape:
    """
    Animation shape class.

    Attributes
    ----------
    x : float or array_like, default 0.0
        x values of the shape or the x-axis radius of an ellipse.
    y : float or array_like, default 0.0
        y values of the shape or the y-axis radius of an ellipse.
    stroke : float or array_like, default 1.0
        Stroke width or animated widths.
    color : float or array_like, default 0x000000
        Stroke or fill color or animated colors.  It is a fill color or
        colors if `stroke` is a scalar zero.
    alpha : float or array_like, default 1.0
        Opacity or animated opacity values.  0.0 means fully transparent and
        1.0 means fully opaque.
    dur : float, default 1.0
        Animation duration in seconds.
    """

    def __init__(self, x=0.0, y=0.0, stroke=1.0, color=0x000000,
            alpha=1.0, dur=0.0):
        # Reduce lists of length 1 to scalars.
        if not isinstance(x, (float, int)) and len(x) == 1:
            x = x[0]
        if not isinstance(y, (float, int)) and len(y) == 1:
            y = y[0]
        if not isinstance(stroke, (float, int)) and len(stroke) == 1:
            stroke = stroke[0]
        if not isinstance(color, (float, int)) and len(color) == 1:
            color = color[0]
        if not isinstance(alpha, (float, int)) and len(alpha) == 1:
            alpha = alpha[0]

        # Ensure if either x or y is an array, they both are.
        if isinstance(x, (float, int)) and not isinstance(y, (float, int)):
            x = [x for n in range(len(y))]
        elif isinstance(y, (float, int)) and not isinstance(x, (float, int)):
            y = [y for n in range(len(x))]

        # Add these parameters to the object.
        self.x = x
        self.y = y
        self.stroke = stroke
        self.color = color
        self.alpha = alpha
        self.dur = dur


class frame:
    """
    Animation shape class.

    Attributes
    ----------
    objs : shape or frame or list of such
        A single shape or frame object or a list of such objects.
    x : float or array_like, default 0.0
        x-axis values of translation of the objects within the frame.
    y : float or array_like, default 0.0
        y-axis values of translation of the objects within the frame.
    ang : float or array_like, default 0.0
        Angles of rotation of the objects within the frame in degrees.
    scale : float or array_like, default 1.0
        Scaling factors of the objects within the frame.
    dur : float, default 1.0
        Animation duration in seconds.
    """

    def __init__(self, objs, x=0.0, y=0.0, ang=0.0, scale=1.0, dur=0.0):
        # Reduce lists of length 1 to scalars.
        if not isinstance(x, (float, int)) and len(x) == 1:
            x = x[0]
        if not isinstance(y, (float, int)) and len(y) == 1:
            y = y[0]
        if not isinstance(ang, (float, int)) and len(ang) == 1:
            ang = ang[0]
        if not isinstance(scale, (float, int)) and len(scale) == 1:
            scale = scale[0]

        # Ensure objs is a list.
        if isinstance(objs, (shape, frame)):
            objs = [objs]

        # Ensure if either x or y is an array, they both are.
        if isinstance(x, (float, int)) and not isinstance(y, (float, int)):
            x = [x for n in range(len(y))]
        elif isinstance(y, (float, int)) and not isinstance(x, (float, int)):
            y = [y for n in range(len(x))]

        # Add these parameters to the object.
        self.objs = objs
        self.x = x
        self.y = y
        self.ang = ang
        self.scale = scale
        self.dur = dur


def animate(obj, filename='ani.svg', x_lim=None, y_lim=None, width=None,
            progress=False):
    """
    Create an svg (scalable vector graphics) animation file from the data stored
    in `obj`.

    Parameters
    ----------
    obj : shape object, frame object, or list of such objects
        The data to create an animation.
    filename : string, default 'ani.svg'
        The desired name of output file.  End it with '.svg' in order for
        your system to know which application to use to open it.
    x_lim : array_like, default [-1, 1]
        A list of the minimum and maximum x values to display in the animation.
    y_lim : array_like, default [-1, 1]
        A list of the minimum and maximum y values to display in the animation.
    width : float, default 640
        Desired width of the animation image in pixels.  This is also used in
        determining the scaling factor for the dimensions of the image.  If not
        specified, the image will actually automatically scale to fit the size
        of the browser window.
    progress : bool, default False
        Flag to show progress bar.
    """

    # Default the x and y limits to [-1, 1].
    if x_lim is None:
        x_lim = [-1, 1]
    if y_lim is None:
        y_lim = [-1, 1]

    # Get the pixel size of the window and the scaling factors.
    x_span = x_lim[1] - x_lim[0]
    y_span = y_lim[1] - y_lim[0]
    if width is None:
        px_span = 640
    else:
        px_span = int(width)
    py_span = round(px_span*y_span/x_span)
    p_scale = px_span/x_span

    # Open the file.
    fid = open(filename, 'w')
    fid.write('<svg xmlns=\"http://www.w3.org/2000/svg\"')
    px_left = int(x_lim[0]*p_scale)
    py_top = int(-y_lim[1]*p_scale)
    fid.write('\n  viewBox=\"%d %d %d %d\"' %
            (px_left, py_top, px_span, py_span))
    if width is not None:
        fid.write(' width=\"%d\"' % (px_span))
        fid.write(' height=\"%d\"' % (py_span))
    fid.write('>')

    # Crawl through the hierarchy of frames and objects and add them to the
    # animation.
    if isinstance(obj, (shape, frame)):
        obj = [obj]
    level = 1
    dur_max = 0.0
    for child in obj:
        dur = add_obj(fid, child, level, p_scale)
        if dur > dur_max:
            dur_max = dur

    # Add progress bar.
    if progress:
        stroke = x_span*0.01
        sbar = shape([-0.5, 0.5], [0.0, 0.0], stroke=stroke, alpha=0.1)
        xa = x_lim[0] + 0.01*x_span/2 + 0.25*stroke
        xb = x_lim[0] + x_span/2 - 0.25*stroke
        y = -(py_span + py_top)/p_scale + 0.25*stroke
        fbar = frame(sbar, x=[xa, xb], y=y,
                scale=[0.01*x_span, x_span], dur=dur_max)
        add_obj(fid, fbar, level, p_scale)

    # Close the file.
    fid.write('\n</svg>')
    fid.close()


def add_obj(fid, obj, level, p_scale):
    """
    Add the shape, frame, or list of such to the svg file.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : shape, frame, or list of such
        A shape or frame object or a list of such objects to be added to the
        svg file.
    level : int
        Indentation level.
    p_scale : float
        Scaling factor to pixels.

    Returns
    -------
    dur_max : float
        Maximum duration of animation objects.

    Notes
    -----
    If the object is a list, call this function on each of the members.

    If the object is a frame, create an group, specify any static translate,
    rotate, or scale properties, add the child objects, add any dynamic
    (animated) translate, rotate, or scale properties, and close the group.

    If the object is a shape, add the shape.
    """

    # Get the indent string.
    ind = '  '*level

    # Initialize the maximum duration.
    dur_max = 0.0

    if isinstance(obj, list):
        for child in obj:
            dur = add_obj(fid, child, level, p_scale)
            if dur > dur_max:
                dur_max = dur
    elif isinstance(obj, frame):
        # Open the group.
        fid.write('\n%s<g' % (ind))

        # Get static flags.
        trans_static = isinstance(obj.x, (float, int))
        rot_static = isinstance(obj.ang, (float, int))
        scale_static = isinstance(obj.scale, (float, int))

        # Get non-trivial flags.
        trans_nontrivial = True if not trans_static else \
                (abs(obj.x) > 1e-6 or abs(obj.y) > 1e-6)
        rot_nontrivial = True if not rot_static else \
                (abs(obj.ang) > 1e-6)
        scale_nontrivial = True if not scale_static else \
                (abs(obj.scale - 1.0) > 1e-6)

        # Write any static, non-trivial properties.  Static rotation should
        # be handled here only if translation is also static.  If there is
        # dynamic translation, the static rotation should be handled by the
        # dynamic rotation so that rotation always comes before translation.
        if (trans_static and trans_nontrivial) or \
                (trans_static and rot_static and rot_nontrivial) or \
                (scale_static and scale_nontrivial):
            fid.write(' transform=\"')
            if trans_static and trans_nontrivial:
                xs = '0' if abs(obj.x*p_scale) < 1e-3 else \
                        "%.3f" % (obj.x*p_scale)
                ys = '0' if abs(obj.y*p_scale) < 1e-3 else \
                        "%.3f" % (-obj.y*p_scale)
                fid.write(' translate(%s,%s)' % (xs, ys))
            if trans_static and rot_static and rot_nontrivial:
                angs = '0' if abs(obj.ang) < 1e-3 else "%.3f" % (-obj.ang)
                fid.write(' rotate(%s)' % (angs))
            if scale_static and scale_nontrivial:
                ss = '0' if abs(obj.scale*p_scale) < 1e-3 else \
                        "%.3f" % (obj.scale*p_scale)
                fid.write(' scale(%s)' % (ss))
            fid.write('\"')
        fid.write('>')

        # Add the objects in this group.
        for child in obj.objs:
            dur = add_obj(fid, child, level + 1, p_scale)
            if dur > dur_max:
                dur_max = dur

        # Add dynamic settings.
        if not trans_static:
            dynamic_translate(fid, obj, level + 1, p_scale)
            if rot_static and rot_nontrivial:
                obj.ang = [obj.ang]
                dynamic_rotate(fid, obj, level + 1)
        if not rot_static:
            dynamic_rotate(fid, obj, level + 1)
        if not scale_static:
            dynamic_scale(fid, obj, level + 1)
        if obj.dur > dur_max:
            dur_max = obj.dur

        # Close the group.
        fid.write('\n%s</g>' % (ind))
    elif isinstance(obj, shape):
        add_shape(fid, obj, level, p_scale)
        if obj.dur > dur_max:
            dur_max = obj.dur

    return dur_max


def add_shape(fid, obj, level, p_scale):
    """
    Add shape object details: the shape itself as defined by (`x`,`y`),
    `stroke` width, stroke or fill `color`, and `alpha`.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : shape
        Shape object.
    level : int
        Indentation level.
    p_scale : float
        Scaling factor to pixels.

    Notes
    -----
    First, the type of shape needs to be determined.  If (`x`,`y`) is a
    single pair of scalar values, then this is either a circle or and
    ellipse where `x` is the x-axis radius and `y` is the y-axis radius.  If
    `x` equals `y` then it is a circle, and if not, then it is an ellipse.
    If (`x`,`y`) is a pair of vectors, then a generic path is created.

    Second, any static properties of the shape are specified.

    Third, the shape itself is defined.

    Finally, any dynamic properties are specified.
    """

    # Get static flags.
    x_scalar = isinstance(obj.x, (float, int))
    stroke_static = isinstance(obj.stroke, (float, int))
    color_static = isinstance(obj.color, (float, int))
    alpha_static = isinstance(obj.alpha, (float, int))

    # Get non-trivial flags.
    stroke_nontrivial = True if not stroke_static else \
            (abs(obj.stroke) > 1e-6)
    alpha_nontrivial = True if not alpha_static else \
            (abs(obj.alpha - 1) > 1e-6)

    # Open the shape.
    ind = '  '*level
    if x_scalar:
        if abs(obj.x - obj.y) < 1e-6:
            fid.write('\n%s<circle' % (ind))
            rs = '0' if abs(obj.x*p_scale) < 1e-3 else \
                    "%.3f" % (abs(obj.x*p_scale))
            fid.write('\n%s  r=\"%s\"' % (ind, rs))
        else:
            fid.write('\n%s<ellipse' % (ind))
            xs = '0' if abs(obj.x*p_scale) < 1e-3 else \
                    "%.3f" % (abs(obj.x*p_scale))
            ys = '0' if abs(obj.y*p_scale) < 1e-3 else \
                    "%.3f" % (abs(obj.y*p_scale))
            fid.write('\n%s  rx=\"%.3f\" ry=\"%.3f\"' % (ind, xs, ys))
    else:
        fid.write('\n%s<path' % (ind))

    # Write the static stroke, color, and alpha.
    if stroke_static and not stroke_nontrivial:
        do_fill = True
    else:
        do_fill = False
    if do_fill:
        fid.write('\n%s  fill=\"#%s\"' % (ind, hex(obj.color)[2:].zfill(6)))
    else:
        fid.write('\n%s  vector-effect=\"non-scaling-stroke\"' % (ind))
        fid.write('\n%s  fill-opacity=\"0\"' % (ind))
        fid.write('\n%s  stroke-linecap=\"round\"' % (ind))
        fid.write('\n%s  stroke-linejoin=\"round\"' % (ind))
        if stroke_static:
            ss = '0' if abs(obj.stroke*p_scale) < 1e-3 else \
                    "%.3f" % (obj.stroke*p_scale)
            fid.write('\n%s  stroke-width=\"%s\"' % (ind, ss))
        if color_static:
            fid.write('\n%s  stroke=\"#%s\"' %
                    (ind, hex(obj.color)[2:].zfill(6)))
    if alpha_static and alpha_nontrivial:
        alphas = '0' if abs(obj.alpha) < 1e-3 else "%.3f" % (obj.alpha)
        fid.write('\n%s  opacity=\"%s\"' % (ind, alphas))

    # Write the x and y values.
    if not x_scalar:
        # Get keypoints in (x,y) path.
        px = [ x_n*p_scale for x_n in obj.x]
        py = [-y_n*p_scale for y_n in obj.y]
        nx_keys = keypoints(px, 0.2)
        ny_keys = keypoints(py, 0.2)
        nn_keys = sorted(list(set(nx_keys).union(set(ny_keys))))
        px = [px[n] for n in nn_keys]
        py = [py[n] for n in nn_keys]
        # Write points.
        txt = '\n%s  d=\"M %.3f,%.3f L' % \
                (ind, px[0], py[0])
        for n in range(1, len(px)):
            txt_new = '%.3f,%.3f' % (px[n], py[n])
            if len(txt) + 1 + len(txt_new) >= 80:
                fid.write(txt + '\n')
                txt = ind + '   '
            txt += ' ' + txt_new
        if do_fill:
            txt += ' z'
        txt += '\"'
        fid.write(txt)

    # Write any dynamics and close the shape.
    if stroke_static and color_static and alpha_static:
        fid.write('/>') # hard close
    else:
        fid.write('>') # soft close
        if not stroke_static:
            dynamic_stroke(fid, obj, level + 1, p_scale)
        if not color_static:
            dynamic_color(fid, obj, level + 1)
        if not alpha_static:
            dynamic_alpha(fid, obj, level + 1)
        if x_scalar:
            if obj.x == obj.y:
                fid.write('\n%s</circle>' % (ind))
            else:
                fid.write('\n%s</ellipse>' % (ind))
        else:
            fid.write('\n%s</path>' % (ind))


def dynamic_stroke(fid, obj, level, p_scale):
    """
    Add stroke width animation.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : shape
        Shape object with `stroke` width array and `dur` animation duration.
    level : int
        Indentation level.
    p_scale : float
        Scaling factor to pixels.
    """

    # Skip if the duration is zero.
    if obj.dur < 1e-9:
        return

    # Introduce the animation.
    ind = '  '*level
    fid.write('\n%s<animate' % (ind))
    fid.write('\n%s  attributeName=\"stroke-width\"' % (ind))
    fid.write('\n%s  repeatCount=\"indefinite\"' % (ind))
    fid.write('\n%s  dur=\"%.3fs\"' % (ind, obj.dur))

    # Get the scaled animation values and key-point indices.
    strokes = [s*p_scale for s in obj.stroke]
    nn_keys = keypoints(strokes, 0.1)

    # Write the values at key points or write all the values.
    if len(nn_keys) < len(strokes)/2:
        write_times(fid, nn_keys, level + 1, len(strokes))
        strokes = [strokes[n] for n in nn_keys]
    write_list(fid, strokes, level + 1)
    fid.write('/>')


def dynamic_color(fid, obj, level):
    """
    Add stroke or fill color animation.  Which is determined by the `stroke`
    value.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : shape
        Shape object with `color` and `stroke` width arrays and `dur` animation
        duration.
    level : int
        Indentation level.
    """

    # Skip if the duration is zero.
    if obj.dur < 1e-9:
        return

    # Introduce the animation.
    ind = '  '*level
    fid.write('\n%s<animate' % (ind))
    if isinstance(obj.stroke, float) and (obj.stroke <= 0):
        fid.write('\n%s  attributeName=\"fill\"' % (ind))
    else:
        fid.write('\n%s  attributeName=\"stroke\"' % (ind))
    fid.write('\n%s  repeatCount=\"indefinite\"' % (ind))
    fid.write('\n%s  dur=\"%.3fs\"' % (ind, obj.dur))

    # Get the scaled animation values and key-point indices.
    R = [(c & 0xff0000) >> 16 for c in obj.color]
    G = [(c & 0x00ff00) >> 8 for c in obj.color]
    B = [(c & 0x0000ff) for c in obj.color]
    R_keys = keypoints(R, 5)
    G_keys = keypoints(G, 5)
    B_keys = keypoints(B, 5)
    nn_keys = sorted(list(set(R_keys).union(set(G_keys)).union(set(B_keys))))

    # Write the values at key points or write all the values.
    colors = obj.color.copy()
    if len(nn_keys) < len(colors)/2:
        write_times(fid, nn_keys, level + 1, len(colors))
        colors = [colors[n] for n in nn_keys]
    txt = '\n%s  values=\"#%s' % \
            (ind, hex(colors[0])[2:].zfill(6))
    for n in range(1, len(colors)):
        txt_new = '#%s' % (hex(colors[n])[2:].zfill(6))
        if len(txt) + 3 + len(txt_new) >= 80:
            fid.write(txt + ';\n')
            txt = ind + '    ' + txt_new
        else:
            txt += '; ' + txt_new
    fid.write(txt + '\"')
    fid.write('/>')


def dynamic_alpha(fid, obj, level):
    """
    Add alpha (opacity) animation.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : shape
        Shape object with `alpha` array and `dur` animation duration.
    level : int
        Indentation level.
    """

    # Skip if the duration is zero.
    if obj.dur < 1e-9:
        return

    # Introduce the animation.
    ind = '  '*level
    fid.write('\n%s<animate' % (ind))
    fid.write('\n%s  attributeName=\"opacity\"' % (ind))
    fid.write('\n%s  repeatCount=\"indefinite\"' % (ind))
    fid.write('\n%s  dur=\"%.3fs\"' % (ind, obj.dur))

    # Get the scaled animation values and key-point indices.
    alphas = obj.alpha.copy()
    nn_keys = keypoints(alphas, 0.1)

    # Write the values at key points or write all the values.
    if len(nn_keys) < len(alphas)/2:
        write_times(fid, nn_keys, level + 1, len(alphas))
        alphas = [alphas[n] for n in nn_keys]
    write_list(fid, alphas, level + 1)
    fid.write('/>')


def dynamic_translate(fid, obj, level, p_scale):
    """
    Add translation (x or y movement) animation.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : frame
        Frame object with `x` and `y` position arrays and `dur` animation
        duration.
    level : int
        Indentation level.
    p_scale : float
        Scaling factor to pixels.
    """

    # Skip if the duration is zero.
    if obj.dur < 1e-9:
        return

    # Introduce the animation.
    ind = '  '*level
    fid.write('\n%s<animateTransform' % (ind))
    fid.write('\n%s  attributeName=\"transform\"' % (ind))
    fid.write('\n%s  type=\"translate\"' % (ind))
    fid.write('\n%s  additive=\"sum\"' % (ind))
    fid.write('\n%s  repeatCount=\"indefinite\"' % (ind))
    fid.write('\n%s  dur=\"%.3fs\"' % (ind, obj.dur))

    # Get the scaled animation values and key-point indices.
    px = [ x_n*p_scale for x_n in obj.x]
    py = [-y_n*p_scale for y_n in obj.y]
    nx_keys = keypoints(px, 0.1)
    ny_keys = keypoints(py, 0.1)
    nn_keys = sorted(list(set(nx_keys).union(set(ny_keys))))

    # Write the values at key points or write all the values.
    if len(nn_keys) < len(px)/2:
        write_times(fid, nn_keys, level + 1, len(px))
        px = [px[n] for n in nn_keys]
        py = [py[n] for n in nn_keys]
    pxs = '0' if abs(px[0]) < 1e-3 else "%.3f" % (px[0])
    pys = '0' if abs(py[0]) < 1e-3 else "%.3f" % (py[0])
    txt = '\n%s  values=\"%s,%s' % (ind, pxs, pys)
    for n in range(1, len(px)):
        pxs = '0' if abs(px[n]) < 1e-3 else "%.3f" % (px[n])
        pys = '0' if abs(py[n]) < 1e-3 else "%.3f" % (py[n])
        txt_new = '%s,%s' % (pxs, pys)
        if len(txt) + 3 + len(txt_new) >= 80:
            fid.write(txt + ';\n')
            txt = ind + '    ' + txt_new
        else:
            txt += '; ' + txt_new
    fid.write(txt + '\"')
    fid.write('/>')


def dynamic_rotate(fid, obj, level):
    """
    Add rotation animation.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : frame
        Frame object with `ang` rotation array and `dur` animation duration.
    level : int
        Indentation level.

    Notes
    -----
    Although this is meant for dynamic rotation only, if there is also
    dynamic translation, a static rotation cannot be performed in the group
    opening instructions because that will cause the rotation to occur after
    the translation.  We always want the rotation to occur before the
    translation.  So, only this dynamic also handles some static cases.
    """

    # Skip if the duration is zero.
    if obj.dur < 1e-9:
        return

    # Introduce the animation.
    ind = '  '*level
    fid.write('\n%s<animateTransform' % (ind))
    fid.write('\n%s  attributeName=\"transform\"' % (ind))
    fid.write('\n%s  type=\"rotate\"' % (ind))
    fid.write('\n%s  additive=\"sum\"' % (ind))
    fid.write('\n%s  repeatCount=\"indefinite\"' % (ind))
    fid.write('\n%s  dur=\"%.3fs\"' % (ind, obj.dur))

    # Get the scaled animation values and key-point indices.
    ang = obj.ang.copy()
    ang_shift = 0.0
    for n in range(1, len(ang)):
        if (ang[n] + ang_shift) - ang[n-1] > 180.0:
            ang_shift -= 360.0
        elif (ang[n] + ang_shift) - ang[n-1] < -180.0:
            ang_shift += 360.0
        ang[n] += ang_shift
    nn_keys = keypoints(ang, 0.1)

    # Write the values at key points or write all the values.
    if len(nn_keys) < len(ang)/2:
        write_times(fid, nn_keys, level + 1, len(ang))
        ang = [ang[n] for n in nn_keys]
    angs = '0' if abs(ang[0]) < 1e-3 else "%.3f" % (-ang[0])
    txt = '\n%s  values=\"%s' % (ind, angs)
    for n in range(1, len(ang)):
        # Write value.
        angs = '0' if abs(ang[n]) < 1e-3 else "%.3f" % (-ang[n])
        if len(txt) + 3 + len(angs) >= 80:
            fid.write(txt + ';\n')
            txt = ind + '    ' + angs
        else:
            txt += '; ' + angs
    fid.write(txt + '\"')
    fid.write('/>')


def dynamic_scale(fid, obj, level):
    """
    Add scaling factor animation.

    Parameters
    ----------
    fid : file ID
        File ID to write the graphic to.
    obj : frame
        Frame object with `scale` factor array and `dur` animation duration.
    level : int
        Indentation level.
    """

    # Skip if the duration is zero.
    if obj.dur < 1e-9:
        return

    # Introduce the animation.
    ind = '  '*level
    fid.write('\n%s<animateTransform' % (ind))
    fid.write('\n%s  attributeName=\"transform\"' % (ind))
    fid.write('\n%s  type=\"scale\"' % (ind))
    fid.write('\n%s  additive=\"sum\"' % (ind))
    fid.write('\n%s  repeatCount=\"indefinite\"' % (ind))
    fid.write('\n%s  dur=\"%.3fs\"' % (ind, obj.dur))

    # Get the scaled animation values and key-point indices.  This does not need
    # the additional `p_scale` because the shape being scaled dynamically will
    # have already been scaled statically in its coordinates by `p_scale`.
    scales = obj.scale.copy()
    nn_keys = keypoints(scales, 0.05)

    # Write the values at key points or write all the values.
    if len(nn_keys) < len(scales)/2:
        write_times(fid, nn_keys, level + 1, len(scales))
        scales = [scales[n] for n in nn_keys]
    write_list(fid, scales, level + 1)
    fid.write('/>')


def write_times(fid, k, level, K):
    """Write the list of key times to the file `fid`."""

    # Get the precision.
    if K <= 100:
        prc = 2
    elif K <= 1000:
        prc = 3
    elif K <= 10000:
        prc = 4
    elif K <= 100000:
        prc = 5
    else:
        prc = 6

    # Write the key times.
    k_scale = 1.0/(K - 1)
    ind = '  '*level
    txt = '\n%skeyTimes=\"%.*f' % (ind, prc, k[0]*k_scale)
    for n in range(1, len(k)):
        txt_new = '%.*f' % (prc, k[n]*k_scale)
        if len(txt) + 3 + len(txt_new) >= 80:
            fid.write(txt + ';\n')
            txt = ind + '  ' + txt_new
        else:
            txt += '; ' + txt_new
    fid.write(txt + '\"')


def write_list(fid, x, level):
    """Write the list of `x` values to the file `fid`."""
    ind = '  '*level
    xs = '0' if abs(x[0]) < 1e-3 else "%.3f" % (x[0])
    txt = '\n%svalues=\"%s' % (ind, xs)
    for n in range(1, len(x)):
        xs = '0' if abs(x[n]) < 1e-3 else "%.3f" % (x[n])
        if len(txt) + 3 + len(xs) >= 80:
            fid.write(txt + ';\n')
            txt = ind + '  ' + xs
        else:
            txt += '; ' + xs
    fid.write(txt + '\"')


def keypoints(y, tol):
    """Including the end points, find where `y` curves."""
    #nn = [n for n in range(1, len(y)-1)
    #        if abs(y[n+1] - 2*y[n] + y[n-1]) > 1e-6]
    #nn.insert(0, 0)
    #nn.append(len(y) - 1)
    #return nn

    n_pin = 0
    nn = [n_pin]
    for n in range(1, len(y)):
        if n == n_pin + 1:
            continue
        slope = (y[n] - y[n_pin])/(n - n_pin)
        for m in range(n_pin + 1, n):
            y_m = slope*(m - n_pin) + y[n_pin]
            if abs(y_m - y[m]) > tol:
                n_pin = n - 1
                nn.append(n_pin)
                break
    nn.append(len(y) - 1)
    return nn
