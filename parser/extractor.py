import sys

def extract(file_name):
    pdf = file(file_name, "rb").read()

    startmark = "\xff\xd8"
    startfix = 0
    endmark = "\xff\xd9"
    endfix = 2
    i = 0

    return_str = ''

    print("*******")

    njpg = 0
    while True:
        istream = pdf.find("stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream+20)
        if istart < 0:
            i = istream+20
            continue
        iend = pdf.find("endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend-20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")
         
        istart += startfix
        iend += endfix

        return_str += ('JPG %d from %d to %d' % (njpg, istart, iend)) + '\n'

        jpg = pdf[istart:iend]
        jpgfile = file("extracted_images/jpg%d.jpg" % njpg, "wb")
        jpgfile.write(jpg)
        jpgfile.close()
         
        njpg += 1
        i = iend

    print(return_str)

extract(sys.argv[1])