
<h1 align="center">
  <br>
  <img src="https://github.com/advaith-22/assets/blob/main/image-removebg-preview.png?raw=true" alt="Markdownify" width="200"></a>
  <br>
  HT (AMD Intel System)
  <br>
</h1>

<h4 align="center">A package that allows to track the x, y, z locations of specific points from 0-20 in your hands. (AMD Intel System)</h4>

<hr>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#Install">Install</a> •
</p>

![screenshot](https://github.com/advaith-22/assets/blob/main/Modern%20Gaming%20Cover%20YouTube%20Channel%20Art.png?raw=true)

## Key Features

* Tracks your hand
* The hand connections or lines can be show or hidden
* Works for almost all computers
* Quick and not much lag
* Simple code that is easy to understand and customize if needed

## How To Use

The following code gets the x, y locations of the index finger tip and moves the mouse accordingly

```python
import htamd
import cv2

cap = cv2.VideoCapture(0)

handt = htamd.ht()

while 1:
    success, img = cap.read()
    img = handt.findhand(img, show_lines=False)
    lml = handt.findpos()
    if len(lml) != 0:
        print(lml[8])
    
    cv2.imshow("Box", img)
    cv2.waitKey(1)
```

## Install

Install with pip

```bash
$ pip install htamd
```

## License

MIT

---

> [http://advaith.athenaserv.com](http://advaith.athenaserv.com) &nbsp;&middot;&nbsp;
> GitHub [@advaith-22](https://github.com/advaith-22) &nbsp;&middot;&nbsp;
> Twitter [@_Advaith_S](https://twitter.com/_Advaith_S)

