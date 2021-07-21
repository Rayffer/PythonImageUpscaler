import matplotlib.pyplot as plt
import cv2
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an image specified to upscale it via DL algorithms.")
    parser.add_argument("--filepath", required=True, help="The image filepath to upscale", type=str)
    parser.add_argument("--algorithm", required=True, help="the DL algorithm to use", type=str, choices=['EDSR_x2', "EDSR_x3", "EDSR_x4", "ESPCN_x2", "ESPCN_x3", "ESPCN_x4", "FSRCNN_x2", "FSRCNN_x3", "FSRCNN_x4", "LapSRN_x2", "LapSRN_x4", "LapSRN_x8"])
    parser.add_argument("--outputfilepath", required=True, help="The path in which to save the result", type=str)
    parser.add_argument("--showresults",default=False, required=False, help="Whether to show the image for comparison", type=bool)
    try:
        args = parser.parse_args()
    except argparse.ArgumentTypeError:
        sys.exit()

    image = cv2.imread(args.filepath)

    model_path = f"Models\{args.algorithm}.pb"
    algorithm_arguments = args.algorithm.split('_x')

    super_resolution_algorithm = cv2.dnn_superres.DnnSuperResImpl_create()
    super_resolution_algorithm.readModel(model_path)
    super_resolution_algorithm.setModel(algorithm_arguments[0].lower(),int(algorithm_arguments[1]))

    result = super_resolution_algorithm.upsample(image)

    cv2.imwrite(args.outputfilepath, result)

    if args.showresults:
        # Resized image
        resized = cv2.resize(image,dsize=None,fx=int(algorithm_arguments[1]),fy=int(algorithm_arguments[1]))
        plt.figure(figsize=(12,8))
        plt.subplot(1,3,1)
        # Original image
        plt.imshow(image[:,:,::-1])
        plt.subplot(1,3,2)
        # SR upscaled
        plt.imshow(result[:,:,::-1])
        plt.subplot(1,3,3)

        # OpenCV upscaled
        plt.imshow(resized[:,:,::-1])
        plt.show()  