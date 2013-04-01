import os
import sys
from  PIL import Image

SIZE_MAP = {
    'ipad_retina_landscape':'2048x1496',
    'ipad_retina_portrait':'1536x2008',
    'ipad_landscape':'1024x748',
    'ipad_portrait':'768x1004',
    'iphone_landscape':'480x320',
    'iphone_portrait':'320x480',
    'iphone_retina_landscape':'960x640',
    'iphone_retina_portrait':'640x960'
}
MASTER_SIZE = 2048
MASTER_INNER = 1496

def main(argv):
    path = os.getcwd()
    print path
    print argv[0]
    master_image = Image.open(argv[0])
    # find and store the center of the master image

    center = (master_image.size[0]/2,master_image.size[1]/2)
    # get the master image size
    # find the center of the master image
    # start iterating the size values from the SIZE_MAP
    for size in SIZE_MAP:
        print SIZE_MAP[size]
        dimensions = (int(SIZE_MAP[size].split('x')[0]),int(SIZE_MAP[size].split('x')[1]))
        # crop
        # im.crop(box) => image
        # Returns a rectangular region from the current image. The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate.
        # while cropping, first thing that needs to be ensured is, the smallest dimension (times some multiple) should be >= 1496
        print MASTER_INNER%min(dimensions)
        if (float(MASTER_INNER)/float(min(dimensions))).is_integer():
            sf = scaling_factor = MASTER_INNER/min(dimensions)
        else:
            sf = scaling_factor = MASTER_INNER/min(dimensions)+1
        box = [center[0]-sf*dimensions[0]/2,center[1]-sf*dimensions[1]/2,center[0]+sf*dimensions[0]/2,center[1]+sf*dimensions[1]/2]
        if min(box)<0:
            sf-=1
        box = [center[0]-sf*dimensions[0]/2,center[1]-sf*dimensions[1]/2,center[0]+sf*dimensions[0]/2,center[1]+sf*dimensions[1]/2]
        print sf
        print box
        new_image = master_image.crop(box)
        new_image.resize(dimensions).show()
        print path+"/"+size+".png" 
        new_image.resize(dimensions).save(path+"/"+size+".png","PNG")
        # import pdb
        # pdb.set_trace()
    # import pdb
    # pdb.set_trace()

if __name__=="__main__":
    main(sys.argv[1:])
