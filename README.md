# Epi_Helper

![Epi_Helper logo](image.png)

Version: 0.1 (Beta)

Beta Version This pipeline is currently in Beta testing and issues could appear during data processing, use at your own risk. Feedback and suggestions are welcome!

## Overview

Epi_Helper was created to help local health departments in MI quickly and easily create communicable disease surveillance reports from MDSS output csv data files. The tool includes two parts:

1. Query Assistant - remembers the case status and investigation status settings for groups of reportable diseases of interest. Guides the user through MDSS report queries
2. Automated Pipeline - intakes MDSS-generated csv files, extracts relevent disease data, cleans & preprocesses, then inputs data  into a master dataset.csv

The pipeline is dynamic in that the user creates a config file to select case and investigation status settings for groups of reportable diseases. The Query Assistant checks MDSS output csv files case and investigation status metadata against the config file, and rejects csv files that do not match the config settings for that particular group of diseases. 

The output dataset.csv is optimized for use in PowerBI. Once PowerBI is configured to generate surveillance reports from output Epi_Helper data, the user only has to refresh PowerBI after generating dataset.csv for each new surveillance data period moving forward

Epi_helper is designed for 5-year MDSS surveillance reports, and has only been tested on Kent County data. 

## Installation

- **TODO**

## License Standard Notice

The repository utilizes code licensed under the terms of the Apache Software License and therefore is licensed under ASL v2 or later.

This source code in this repository is free: you can redistribute it and/or modify it under the terms of the Apache Software License version 2, or (at your option) any later version.

This source code in this repository is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Apache Software License for more details.

You should have received a copy of the Apache Software License along with this program. If not, see http://www.apache.org/licenses/LICENSE-2.0.html

The source code forked from other open source projects will inherit its license.

## Privacy Notice

This repository contains only non-sensitive, publicly available data and information.

## Records Management Notice

This repository is not a source of government records, but is a copy to increase collaboration and collaborative potential. All government records will be published through the Kent County Health Department website.

## Notes

- The project expects a `config.json` file in the working directory.
- This project relies on tkinter and is only tested on Windows.
