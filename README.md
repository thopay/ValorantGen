<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">ValorantGen</h3>

  <p align="center">
    Generates League/Twitch Accounts
    <br />
    <a href="https://github.com/thopay/ValorantGen/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/thopay/ValorantGen/">Report Bug</a>
    ·
    <a href="https://github.com/thopay/ValorantGen/">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

When Valorant initially released, they gave beta access randomly out to viewers that had their League accounts connected. So all this does is make League and Twitch accounts then connect them.

### Built With
* [Python](https://www.python.org)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python

### Installation

1. Clone the repo
```sh
git clone https://github.com/th-ms/ValorantGen.git
```
2. Download the <a href="https://chromedriver.chromium.org/downloads">Chrome WebDriver</a> that matches your version
3. Run the script
```sh
python valorant.py
```



<!-- USAGE EXAMPLES -->
## Usage

When you run the script you'll be prompted to enter your catchall domain. After that, it will open two browsers, one for the League sign up the other for Twitch. The reason two browsers are used is because eventually the Twitch browser blocks sign up attempts, so it's important that you use proxies on it, but I haven't put enough time into it to setup up automatic proxy rotation, so the user has to enter it manually. The League browser though doesn't need proxies, and ideally, you wouldn't want to use any because League uses reCaptcha and the best way to get faster captchas or one-clicks is by logging in with your Gmail on it and not changing the IP (Google flags proxies and selenium browsers very easily).

<!-- ROADMAP -->
## Roadmap

### I don't really have a reason to add anything, since Valorant is public now, but here's things I would look into if other games used the same general process
* Automatic proxy rotation
* Captcha API like 2captcha or anticaptcha so it's fully hands off (Unknown how I would handle Arkose Labs captcha for Twitch though)
* Saves results to txt file (This is pretty easy but I wrote this in a day or so and was lazy)
* Implement webdriver-manager so the user doesn't need to install webdriver themself

See the [open issues](https://github.com/thopay/ValorantGen/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License.



<!-- CONTACT -->
## Contact

Thomas - [@th___mas](https://twitter.com/th___mas) - contact@th-mas.dev

Project Link: [https://github.com/thopay/ValorantGen](https://github.com/thopay/ValorantGen)
