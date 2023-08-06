import argparse
import cv2
import numpy as np

from doretta.dot_validator import DotDetectorParams, DotDetector

np.set_printoptions(threshold=np.inf)

def main():
    parser = argparse.ArgumentParser(
        description="This program could be used to run doretta against an image or test the doretta installation"
    )
    subparsers = parser.add_subparsers(dest="subcommand", description="subcommand can be either predict or test")
    subparsers.required = True

    # Predict subcommand
    predict_sub = subparsers.add_parser(name="predict")
    predict_sub.add_argument("filename", type=str, help="Path of the file you want to predict for")

    predict_sub.add_argument("--radius", type=int, help="Radius of the dots you are looking for", default=-1)

    predict_sub.add_argument("--no_mapping", help="Whether to generate raw pixel coordinates or relative distances in mm. Supply flag for the former",
                              action="store_true", default=False)
    predict_sub.add_argument("--scaling", type=float, help="Scaling of mm to pixel. Default value is 4mm for each pixel", default=4.0)
    
    # Add the train command
    test_sub = subparsers.add_parser(name="test")
    test_sub.add_argument("--episodes", type=int, help="Number of iterations to test the algorithms for", required=True, default=1000)

    args = parser.parse_args()

    if args.subcommand == "predict":
        dot_params = DotDetectorParams(args.radius, not args.no_mapping, args.scaling)
        detector = DotDetector(dot_params)

        img = cv2.imread(args.filename, 0)

        print(detector.detect_dot(img))

    elif args.subcommand == "test":
        detector = DotDetector()

        detector.test_module(args.episodes)

    else:
        raise ValueError("Invalid subcommand passed.")


if __name__ == "__main__":
    main()