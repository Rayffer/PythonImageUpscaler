# Python Image Upscaler

**PythonImageUpscaler** is a project that uses opencv super resolution functionality along with some deep learning algorithms to enhance image quality when upscaling.

The deep learning algorithms used are available at the following repositories:

- [EDSR in Tensorflow](https://github.com/Saafke/EDSR_Tensorflow)
- [ESPCN in Tensorflow](https://github.com/fannymonori/TF-ESPCN)
- [FSRCNN in Tensorflow](https://github.com/Saafke/FSRCNN_Tensorflow)
- [LapSRN in Tensorflow](https://github.com/fannymonori/TF-LapSRN)

## Dependencies

This project is based on python 3.8.5, and uses opencv for image processing and if requested for interactive visualization of results.

To install all dependencies, just run `pip install -r requirements.txt`

## Executing

The python script accepts 4 arguments:

- **filepath:** The filepath to the image desired to upscale.
- **algorithm:** The algorithm to use for image upscaling (f.e. EDSR_x2).
- **outputfilepath:** The filepath where the image will be saved.
- **showresults:** Whether to show a window with the result to interactively zoom to inspect them, optional.

The parameter **Algorithm** only accepts a collection of values, too see the available ones, use the `--help` command."# PythonImageUpscaler" 
