![contributer](https://img.shields.io/github/contributors/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![last commit](https://img.shields.io/github/last-commit/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![size](https://img.shields.io/github/repo-size/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![license](https://img.shields.io/github/license/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![pytesseract](https://img.shields.io/pypi/pyversions/pytesseract?style=for-the-badge)

- [Digit-Recognition-Using-Tesseract](#digit-recognition-using-tesseract)
  - [How to run?](#how-to-run)
    - [Step Zero: Clone the repo](#step-zero-clone-the-repo)
    - [Step One: Cd to the folder](#step-one-cd-to-the-folder)
    - [Step Two: Create a virtual enviroment and activate it](#step-two-create-a-virtual-enviroment-and-activate-it)
    - [Step Three: Install the PIP packages/dependencies](#step-three-install-the-pip-packages-dependencies)
    - [Step Four: Installing Fonts](#step-four-installing-fonts)
    - [Step Five: It's done 🎉 | Run the app](#step-five-it-s-done------run-the-app)
  - [VSCode + Win10 Configuration](#vscode--win10-configuration)
    - [Step Zero: Clone the repo](#step-one-clone-the-repo)
    - [Step Two: Install the PIP packages/dependencies](#step-two-install-the-pip-packagesdependencies)
    - [Step Three: Install the tesseract.exe and config pytesseract.py](#step-three-install-the-tesseractexe-and-config-pytesseractpy)
    - [Step Four: Run the app](#step-four-run-the-app)
  - [Additional](#additional)
  - [Demo 🎥](#demo-)

# Digit-Recognition-Using-Tesseract
This project uses Tesseract, an open-source OCR engine, to recognize digits from an image. Tesseract is trained on a dataset of images containing digits and used to extract the digits from a given image. The output is a set of recognized digits that can be used for further processing or analysis.

## How to run?

### Step Zero: Clone the repo
```code
git clone https://github.com/BitterOcean/Digit-Recognition-Using-Tesseract.git
```

### Step One: Cd to the folder
```code
cd Digit-Recognition-Using-Tesseract
```

### Step Two: Create a virtual enviroment and activate it
```code
python3 -m venv env
source ./env/bin/activate
```

### Step Three: Install the PIP packages/dependencies
```code
(env)$ pip install -r requirements.txt
```

### Step Four: Installing Fonts
In order to make the app's gui look good, you will have to install the Montserrat font. From the `assets` folder, install all three fonts (with `.ttf` format) by double clicking them.

### Step Five: It's done 🎉 | Run the app
```code
(env)$ python main.py
```
## VSCode + Win10 Configuration

### Step One: Clone the repo
```code
git clone https://github.com/BitterOcean/Digit-Recognition-Using-Tesseract.git
```

### Step Two: Install the PIP packages/dependencies
```code
(env)$ pip install -r requirements.txt
```

### Step Three: Install the tesseract.exe and config pytesseract.py
download and install tesseract.exe at [tesseract official library](https://digi.bib.uni-mannheim.de/tesseract/?C=M;O=D)
notice that, by clicking the `Last modified` at the bottom line, you can fast locate the updated version.
and revise the path line in `pytesseract.py` (if you have performed the step two correctly)
```code
#tesseract_cmd = 'tesseract'  # original style in the pytesseract.py
tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe' #change to your tesseract.exe path
```
### Step Four: Run the app
double click `main.py` in the left column in VSCode, press F5 to run.

## Additional
Just put .jpg or .png image that you want to recognize in the `views\dashboard\assets\pic\` folder, then all images will load automatically on loading the GUI. 

## Demo 🎥
![demo](https://user-images.githubusercontent.com/60509979/236934728-8f191d67-2b75-490e-8b16-e217b04ae0db.gif)

