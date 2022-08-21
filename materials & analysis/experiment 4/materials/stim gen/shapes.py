import numpy as np 


from matplotlib.patches import Circle, Wedge, Polygon, RegularPolygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.path as mpath




# # # # # # # # # # # # # # # # 
# 
#       Squares
# 
# # # # # # # # # # # # # # # # 

def generate_square(dim1, dim2, filename):
    lab_monitor = 1440/41 #<-- pixel info about lab monitor ensuring correct sizes
    res_w = lab_monitor

    # get correct dims
    dim1 = ( (dim1) * (230 - 25) ) + 25
    dim2 = ( (dim2) * (7.1 - 2.5) ) + 2.5


    d = dim2 * res_w
    s = int(np.round(dim1))

    # size of image
    v=650
    canvas = (v,v)

    # something for saving it (idk i didn't write these next parts)
    thumb = canvas[0], canvas[1]

    # init canvas
    im = Image.new('RGBA', canvas, (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)

    # draw rectangles
    x1 = canvas[0]/2 - d/2
    y1 = canvas[0]/2 + d/2
    x2 = canvas[0]/2 + d/2
    y2 = canvas[0]/2 - d/2

    draw.rectangle([x1, y1, x2, y2],
        outline = (0, 0, 0, 255), 
        fill = (s,s,s,255))

    # make thumbnail
    im.thumbnail(thumb)

    # save image
    im.save(filename)



# # # # # # # # # # # # # # # # 
# 
#       Iris-Ish Flowers
# 
# # # # # # # # # # # # # # # # 
def generate_flower(dim1, dim2, filename, compress_edge = True):
    min_ = .6
    max_ = 2.5

    dim1 = min_ + (max_ - min_) * dim1
    dim2 = min_ + (max_ - min_) * dim2

    fig, ax = plt.subplots(
        figsize = [8,8]
    )

    ## add circle
    ax.add_patch(
        Circle([0,0], radius = .2, alpha = 1, zorder = 100, color = 'yellow')
    )

    for r in np.linspace(.001,.2035,100):
        ax.add_patch(
            Circle(
                [0,0], 
                radius = r, zorder = 100, facecolor = 'None', edgecolor = 'brown',
                alpha = 1 - np.exp(-.2 * (r/.2)),
            )
        )

    # surround circle
    ax.add_patch(
        Circle(
            [0,0], 
            radius = max(dim1, dim2) if compress_edge == True else max_, 
            alpha = 1, zorder = 0, facecolor = 'None', edgecolor = 'black', linewidth = 2)
    )

    sw_ = .322
    sy_ = .5

    sw = .522
    sy = .5

    offset = -22.5

    a = 1

    for petal_orientation in (0, 120, 240):
        
        # outside
        x = [
            [0,0],
            [-sw,sy],
            [0,dim1],
            [sw,sy],
            [0,0],
        ]

        codes = [
            mpath.Path.MOVETO,
            mpath.Path.CURVE3,
            mpath.Path.LINETO,
            mpath.Path.CURVE3,
            mpath.Path.LINETO,
            # mpath.Path.CLOSEPOLY,
        ]

        p_verts = mpath.Path(x, codes)
        p = mpl.patches.PathPatch(p_verts, color = '#3c268c', alpha = a, zorder = 20) # these are the best colors i could find for color blindness: #9c59ff  |  #3c268c  |  'purple'
        r = mpl.transforms.Affine2D().rotate_deg_around(0,0, petal_orientation + offset) + ax.transData
        p.set_transform(r)

        ax.add_patch(p)


        # inside
        x = [
            [0,.3],
            [-.05,.3],
            [0,.5],
            [.05,.3],
            [0,.3],
        ]

        codes = [
            mpath.Path.MOVETO,
            mpath.Path.CURVE3,
            mpath.Path.LINETO,
            mpath.Path.CURVE3,
            mpath.Path.LINETO,
        ]

        p_verts = mpath.Path(x, codes)
        p = mpl.patches.PathPatch(p_verts, color = 'yellow', alpha = .7, zorder = 20)
        r = mpl.transforms.Affine2D().rotate_deg_around(0,0, petal_orientation + offset) + ax.transData
        p.set_transform(r)

        ax.add_patch(p)





    for leaf_orientation in (60, 180, 300):

        # outside
        x = [
            [0,dim2],
            [-sw,sy],
            [0,0],
            [sw,sy],
            [0,dim2],
        ]

        codes = [
            mpath.Path.MOVETO,
            mpath.Path.CURVE3,
            mpath.Path.CURVE3,
            mpath.Path.CURVE3,
            mpath.Path.LINETO,
        ]

        p_verts = mpath.Path(x, codes)
        p = mpl.patches.PathPatch(p_verts, color = 'green', alpha = a)
        r = mpl.transforms.Affine2D().rotate_deg_around(0,0, leaf_orientation + offset) + ax.transData
        p.set_transform(r)

        ax.add_patch(p)

        y11 = .3
        y12 = .4
        y13 = .32
        y21 = .4
        y22 = .47
        y23 = .42




        # inside
        x = [
            [0, y21],
            [-.1, y22],
            [0, y23],

            [0, y23],
            [.1, y22],
            [-0, y21],
        ]

        codes = [
            mpath.Path.MOVETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
        ]

        p_verts = mpath.Path(x, codes)
        p = mpl.patches.PathPatch(p_verts, color = '#005e1b', alpha = 1)
        r = mpl.transforms.Affine2D().rotate_deg_around(0,0, leaf_orientation + offset) + ax.transData
        p.set_transform(r)

        ax.add_patch(p)

        x = [
            [0, y11],
            [-.15, y12],
            [0, y13],
            
            [0, y13],
            [.15, y12],
            [0, y11],
            
        ]

        codes = [
            mpath.Path.MOVETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
        ]

        p_verts = mpath.Path(x, codes)
        p = mpl.patches.PathPatch(p_verts, color = '#005e1b', alpha = 1)
        r = mpl.transforms.Affine2D().rotate_deg_around(0,0, leaf_orientation + offset) + ax.transData
        p.set_transform(r)

        ax.add_patch(p)






    fig.patch.set_visible(False)
    ax.axis('off')

    l1, l2 = [-(max_+.1), (max_+.1)]
    plt.xlim([l1,l2])
    plt.ylim([l1,l2])
    plt.xticks([]); plt.yticks([])

    # plt.savefig('test.png') # <-- test it out before full run
    # exit()

    plt.savefig(filename)
    plt.close()





# # # # # # # # # # # # # # # # 
# 
#       FISH
# 
# # # # # # # # # # # # # # # # 

def generate_fish(dim1, dim2, filename):
    try:
        from oct2py import octave
    except:
        print('need to install *oct2py*, aborting...')
        exit()
    # octave.addpath('./')
    # octave.graphics_toolkit('gnuplot')

    d1r = [11, 36] # tail
    # % [11,13,16,19,24,29,35,42,51]
    
    d2r = [14, 164] # dorsal (i think)
    # % [14,23,33,46,62,80,103,131,164]

    octave.feval(
        './make_fish.m', 
        131, 
        d1r[0] + (d1r[-1] - d1r[0]) * dim1, 
        d2r[0] + (d2r[-1] - d2r[0]) * dim2, 
        50, [.9,.9,.9], [.9,.9,.9], filename,
        plot_dir = './',
        plot_name = 'test',
        plot_format = 'png'
    )













