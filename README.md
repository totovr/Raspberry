# Open Kinect for ARM6

For more information check the Github of [Shiffman](https://github.com/shiffman/OpenKinect-for-Processing)

This repository contains programs for different applications in Ubuntu Xelenial and Processing 3.3.6

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/#buy-now-modal)

I will supposed that you already setup all the system if you did not check this [README.dm](https://github.com/totovr/Raspberry/blob/master/README.md)

* Kinect V1

* [Processing 3.3.6 for ARM6](http://download.processing.org/processing-3.3.6-linux-armv6hf.tgz)

  Also you can install it running the next command:

      curl https://processing.org/download/install-arm.sh | sudo sh


### Installing the library

  1. Download the [OpenKinect library for ARM6](https://github.com/totovr/Raspberry/archive/OpenKinect.zip)

  2. Unzip it and past it inside of:

    /home/"your user"/sketchbook/libraries

  3. Add the next [51-kinect.rules](https://github.com/totovr/Raspberry/blob/OpenKinect/51-kinect.rules) in:

    /etc/udev/rules.d

## Run one example of the library

## Contributing

Please read [CONTRIBUTING.md](https://github.com/totovr/Processing/blob/master/CONTRIBUTING.md) for details of the code of conduct, and the process for submitting pull requests to us.

## Versioning

I use [SemVer](http://semver.org/) for versioning.

## Author

[Processing](https://github.com/processing/processing/wiki/Supported-Platforms#library-openkinect)

## Suporter

Antonio Vega Ramirez:

* [Github](https://github.com/totovr)
* [Twitter](https://twitter.com/SpainDice)

## License

This project is licensed under The MIT License (MIT) - see the [LICENSE.md](https://github.com/totovr/Raspberry/blob/master/LICENSE.md) file for details
