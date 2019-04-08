# README

The purpose of this README is to provide example python scripts to get started with using Terabee 3Dcam 80x60 with OpenNI 2 framework. We provide here both Linux and Windows instructions.

For more information about the Terabee 3Dcam 80x60, please click [here](https://www.terabee.com/shop/3d-tof-cameras/terabee-3dcam/).

# Requirements
In order to use those sample you will need the following requirements:

* On linux, you will need:
    * To install the **OpenNI 2 library**
        >sudo apt-get install libopenni2-dev
    * To install **OpenCV**
        >**Important note**:
        > The right OpenCV version is mandatory in order to use the SDK. We recommend following the OpenCV installation for linux available [here](https://github.com/Terabee/linux_openni2_samples#install-opencv).
        >
    * To Install the **Terabee OpenNI 2 SDK for Linux** following these steps:
        *  Download the SDK from the Downloads section of Terabee 3Dcam [here](https://www.terabee.com/shop/3d-tof-cameras/terabee-3dcam/)
        * Extract the content of the archive (relevant to your system architecture and desired OpenNI version) in the directory of your choice

        * Enter the SDK folder and install the SDK with root permission
            >sudo ./install.sh

* On Windows, you will need:
    * To install the **Terabee OpenNI2 SDK for Windows** following these steps:
        *  Download the SDK from the Downloads section of Terabee 3Dcam [here](https://www.terabee.com/shop/3d-tof-cameras/terabee-3dcam/)
        
        * Once downloaded, install the SDK by running the file relevant to your system architecture and desired OpenNI version.

    * To copy the following files from "C:/Program Files/TERABEEToF" to "C:/Program Files/OpenNI2/Redist/OpenNI2/Drivers"
        * DeviceModules2.dll
        * RvcLib.dll

* In both Linux and Windows, you will need **Python 3** with the following python modules:
    * openni
    * numpy
    * platform
    * cv2
        * On Linux this module is automatically installed when installing OpenCV
        * On Windows you need the pip package named **opencv_python**

    Those modules can be installed using pip with the folowing command with elevated privileges:
    > pip install \<module name\>

    **Important Note:** The Python architecture (64 or 32 bits) must match the architecture of the SDK.
