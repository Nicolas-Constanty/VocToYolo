#!/usr/bin/python

import sys, getopt
import lib.voctoyololib

def main(argv):
    folder = '.'
    annotations = '/Annotations/*.xml'
    label_file = '/pascal_label_map.pbtxt'
    project_name = 'obj'
    root_folder = 'data'
    try:
        opts, args = getopt.getopt(argv,"hs:n:o:l:",["sfolder=","name=","output=","label="])
    except getopt.GetoptError:
        print ('voctoyolo.py -s <src_folder> -l <label_file> -n <project_name> -o <output_folder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('voctoyolo.py -s <src_folder> -l <label_file> -n <project_name> -o <output_folder>')
            sys.exit()
        elif opt in ("-s", "--sfolder"):
            folder = arg
        elif opt in ("-l", "--label"):
            label_file = arg
        elif opt in ("-n", "--name"):
            project_name = arg
        elif opt in ("-o", "--output"):
            root_folder = arg
    labels = lib.voctoyololib.parse_label_pbtxt(folder + label_file)
    lib.voctoyololib.voc_to_yolo(folder + annotations, labels, project_name, root_folder)
        
if __name__ == "__main__":
    main(sys.argv[1:])
