# README

The purpose of this README is to provide example python scripts to get started with using Terabee 3Dcam 80x60 with OpenNI 2 framework. We provide here both Linux and Windows instructions.

For more information about the Terabee 3Dcam 80x60, please click [here](https://www.terabee.com/portfolio-item/terabee-3dcam-80x60).

# Requirements
In order to use those sample you will need the following requirements:

* Python3 with the following python modules
    * openni
    * numpy
    * platform
    * cv2
        * On linux this module is automatically installed when installing OpenCV
        * On windows you need the pip package named *opencv_python*

    In both Linux and windows those modules can be installed using pip with the folowing command with elevated privileges:
    > pip install \<module name\>

* On linux
    * libopenni2 library
        >sudo apt-get install libopenni2-dev
    * OpenCV
        >**Important note**:
        > The right OpenCV version is mandatory in order to use the SDK. We recommend following the OpenCV installation for linux available [here](https://github.com/Terabee/linux_openni2_samples#install-opencv).
        >
    * Terabee OpenNI2 SDK for Linux (available in the Downloads section of Terabee 3Dcam [here](https://www.terabee.com/portfolio-item/terabee-3dcam-80x60/#downloads))

* On Windows
    * Terabee OpenNI2 SDK for Windows (available in the Downloads section of Terabee 3Dcam [here](https://www.terabee.com/portfolio-item/terabee-3dcam-80x60/#downloads))
    * You will need to copy the following files from "C:/Program Files/TERABEEToF" to "C:/Program Files/OpenNI2/Redist/OpenNI2/Drivers"
        * DeviceModules2.dll
        * RvcLib.dll