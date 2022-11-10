[![PyPI - Python](https://img.shields.io/pypi/pyversions/iconsdk?logo=pypi)](https://pypi.org/project/iconsdk)
<a name="readme-top"></a>

<!-- PROJECT DETAIL -->
<br />
<div align="center">
  <h1 align="center">Koi Fish Farm Simulator</h1>
  <a href="https://github.com/OnePotatoCat/Procedural_Generation_Practice">
    <img src="/assets/icon_koi.png" alt="Logo" width="512" height="256">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An artificial koi fish farm inspired <a href="https://jobtalle.itch.io/koifarm"> Job Talle's Koi Farm Simulator </a>
    <br />
    <a href="https://github.com/OnePotatoCat/Procedural_Generation_Practice"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/OnePotatoCat/Procedural_Generation_Practice/issues">Report Bug</a>
    .
    <a href="https://github.com/OnePotatoCat/Procedural_Generation_Practice/issues">Request Feature</a>
  </p>
</div>
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li>
      <a href="#koi_fish_generation">Koi Fish Generation</a>
      <ol>
        <li><a href="#shape_and_size">Shape and Size</a></li>
        <li><a href="#pigment_Pattern">Pigment Pattern</a></li>
        <li><a href="#eye_position">Eye Position</a></li>
        <li><a href="#image_generation">Image Generation</a></li>
        <li><a href="#showcasing_and_swimming">Showcasing and Swimming</a></li>
      </ol>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- INTRODUCTION -->
##  Introduction
<a name="introduction"></a>
<div align="center">
  <img src="/assets/koi_fishes.gif" alt="Logo" width="512" height="256">
</div>

The Koi Fish Generator can create up to 350 unique koi fishes and will swim around the window randomly is a soothing fashion.:relaxed:
<br />

<!--- Koi Fish Generation --->
## <ins>Koi Fish Generation</ins>
<a name="koi_fish_generation"></a>
Each koi fishes is uniquely generated with three distinct feature:
* Shape and size
* Pigment pattern
* Eye position (barely noticeable)
<br />

<!--- Shape and Size --->
### <ins>Shape and Size</ins> <a name="shape_and_size"></a>
A koi fish (or a fish in general) with the fins is closely resemble the shape of a airfoil.

Therefore, to generate the shape of a fish, [NACA 4 Series Airfoils (symmetrical)](https://www.fxsolver.com/browse/formulas/NACA+4+Series+Airfoils+%28symmetrical%29) equation is used. The c constant is randomized to create different thickness of airfoil shape, hence different size of koi fishes.

<div align="center">
  <img src="/assets/naca4_symmetric_test.png" alt="airfoil" width="320" height="240">
</div>
<br />
<br />

<!--- Pigment Pattern --->
### <ins>Pigment Pattern</ins> <a name="pigment_Pattern"></a>
The general method of pigment pattern generation is discussed in Job Talle's [blog](https://jobtalle.com/digital_koi_breeding.html).
In summary, Job Talle uses 3D noise for pigment generation. For this project 2D noise is used instead for simplicity and 2D noise map offer enough unique patterns for this scale of the project.

[Perlin Noise](https://pypi.org/project/perlin-noise/) library is used to make my day a little more simple. 
<div align="center">
  <img src="/assets/perlin_noise.png" alt="perlin noise" width="251" height="251">
</div>
Each koi fish has a minimum of 1 to 3 pigment colors. Each color pigment is create and store as a layer.

<br />
<br />

<!--- Eye Position --->
### <ins>Eye Position</ins> <a name="eye_position"></a>
Next, the eye position is simply a lump of black pixels randomly place on the fixed range of position on the shape of the airfoil. The eye is treat at an individual layer similar to pigment color.
<br />
<br />

<!--- Image Generation --->
### <ins>Image Generation</ins> <a name="image_generation"></a>
A png image of each koi fish is generated with the shape, pigment layers and eye layer informtion with matplolib.
Due to the shear number of pigment layer calculation, multiprocessing with producer and consumer pattern in implemented to speed up the koi fish information and then passed on to matplotlib in the main process for image generation.

<sub>Just learned that, matplotlib is only able to work in the main thread and for some reason, it is unable to generate more then 300~350 images. :confused:</sub>
<br />
<br />

<!--- Showcasing and Swimming --->
### <ins>Showcasing and Swimming</ins> <a name="showcasing_and_swimming"></a>
Lastly, to display the koi fishes, tkinter canvas is used. Each koi fishes will first spawn on the the canvas at a random position. Right after the fishes are spawn, each of them will start swimming towards a given target location. After small period of time passes, regardless of reaching the current target location, each fishes is given a new target location to swim towards. I used queue and threading to randomize the when each fishes will has a new location to swim toward to make the swimming pattern looks more natural. 

<sub>Threading seem like an overkill here, but I want to familiarized threading and queue :stuck_out_tongue_winking_eye:</sub>
<br />
<br />

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contributing -->
## Contributing

Any suggestion, any contributions are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Heng, Kien Leong [Leon]: [@oPotatoCat](https://twitter.com/oPotatoCat)

Linkedin: [www.linkedin.com/in/kien-leong-heng-007223156/](https://www.linkedin.com/in/kien-leong-heng-007223156/)

itch.io : [realpotatocat.itch.io/](https://realpotatocat.itch.io/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

