![contributer](https://img.shields.io/github/contributors/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![last commit](https://img.shields.io/github/last-commit/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![size](https://img.shields.io/github/repo-size/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![license](https://img.shields.io/github/license/BitterOcean/Digit-Recognition-Using-Tesseract?style=for-the-badge)
![pytesseract](https://img.shields.io/pypi/pyversions/pytesseract?style=for-the-badge)

# Digit-Recognition-Using-Tesseract
This project uses Tesseract, an open-source OCR engine, to recognize digits from an image. Tesseract is trained on a dataset of images containing digits and used to extract the digits from a given image. The output is a set of recognized digits that can be used for further processing or analysis.

### Digit-Recognition-Using-Deep-Learning
<a href="https://colab.research.google.com/drive/1HfauhJPX467NgyHY4QpjuiyO-hcU7lE_?usp=sharing" target="_blank"> <img src="https://img.shields.io/badge/Google%20Colab-Source%20Code-%23F9AB00?style=for-the-badge&logo=googlecolab" /> </a>

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

### Step Four: Installing Tesseract on Ubuntu
```code
$ sudo apt install tesseract-ocr -y
```

### Step Five: Installing Fonts
In order to make the app's gui look good, you will have to install the Montserrat font. From the `assets` folder, install all three fonts (with `.ttf` format) by double clicking them.

### Step Six: It's done 🎉 | Run the app
```code
(env)$ python main.py
```

## Demo 🎥

![demo](https://user-images.githubusercontent.com/60509979/236934728-8f191d67-2b75-490e-8b16-e217b04ae0db.gif)
