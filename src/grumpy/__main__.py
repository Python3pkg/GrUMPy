from coinor.grumpy import BBTree
import sys
import io

try:
    from PIL import Image as PIL_Image
except ImportError:
    PIL_INSTALLED = False
else:
    PIL_INSTALLED = True

if __name__ == '__main__':
    bt = BBTree()
    bt.set_display_mode('pygame')
    line_number = 0
    for line in sys.stdin:
        bt.ProcessLine(line)
        print('line', line_number, 'processed.')
        line_number = line_number+1
        if line_number%10 != 0:
            continue
        bt.display_all()
