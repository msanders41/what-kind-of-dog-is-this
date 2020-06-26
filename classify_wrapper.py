# PROGRAMMER:   Mitchell S.
# DATE CREATED: 06/22/2020                        
# REVISED DATE: 06/25/2020
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
##
#
# Import modules
#
# Import functions from user defined functions
#
##

# Main program function defined below
def main():

	# Access image file location given as pathname in cmd line, specified with "--dir"
	in_arg = get_input_args()

	# 


# Call to main function to run the program
if __name__ == "__main__":
    main()